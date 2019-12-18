#/usr/bin/env python
import RPi.GPIO as GPIO
import PCF8591 as ADC
import time

GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)

def loop():
    status = 1
    while True:
        value = ADC.read(0)
        print 'Value: ', value
        outvalue = value * (255 - 125) / 255 + 125
        ADC.write(outvalue)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
