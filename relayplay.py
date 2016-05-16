#!/usr/bin/env python
import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) ## GPIO pin 7 to OUT

def Play(playTime):
    GPIO.output(7, True) ## Turn on GPIO pin 7
    time.sleep(playTime) ## Wait
    GPIO.output(7, False) ## Switch off GPIO pin 7
    GPIO.cleanup()

## Prompt user for input
duration = raw_input("Enter play time: ")

Play(int(duration))
        