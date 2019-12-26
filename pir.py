#!/usr/bin/python

# Imported Modules
from time import sleep
import subprocess
import RPi.GPIO as GPIO


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(22, GPIO.IN)

PIR = 22
display_on = True

while True:

    if display_on and not GPIO.input(PIR):
        subprocess.run("vcgencmd display_power 0 > /dev/null 2>&1", shell=True)
        display_on = False

    if not display_on and GPIO.input(PIR):
        subprocess.run("vcgencmd display_power 1 > /dev/null 2>&1", shell=True)
        display_on = True
        sleep(30)

    sleep(0.5)