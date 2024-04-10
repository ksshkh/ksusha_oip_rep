import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        val = dec2bin(i)
        GPIO.output(dac, val)
        time.sleep(0.1)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            return i
    return 0

try:
    while True:
        i = adc()
        print (i)
        voltage = i * (3.3 / 256.0)
        print("{:.2f}V".format(voltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()