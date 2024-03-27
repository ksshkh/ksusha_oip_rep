import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("enter a number from 0 to 255")
        try:
            num = int(num)
            if 0 <= num <= 255:
                voltage = float(num) / 256 * 3.3
                print(f"expected voltage is about {voltage:.4} volt")
                GPIO.output(dac, dec2bin(num))
            elif num < 0:
                num = input("the number must be more than 0")
            else:
                num = input("the number must be less than 255")
        except Exception:
            if num == "q":
                break


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
