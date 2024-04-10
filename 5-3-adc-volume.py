import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7,-1, -1):
        k += 2**i
        val = dec2bin(k)
        GPIO.output(dac, val)
        time.sleep(0.1)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            k -= 2**i
    return k

try:
    while True:
        i = adc()
        res = dec2bin(i)
        voltage = i * (3.3 / 256.0)
        print("{:.2f}V".format(voltage))
        GPIO.output(leds, res)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()