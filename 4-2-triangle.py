import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
x = 0
t = 0

try:
    period = float(input("type a period for sygnal"))
    while True:
        GPIO.output(dac, dec2bin(x))

        voltage = float(x) / 256 * 3.3
        print(f"expected voltage is about {voltage:.4} volt")

        if x == 0:
            inc_flag = 1
        elif x == 255:
            inc_flag = 0
        
        if inc_flag == 0:
            x = x - 1
        elif inc_flag == 1:
            x = x + 1
        
        time.sleep(period/512)
        t += 1
    
except ValueError:
    print("wrong period")
        


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()