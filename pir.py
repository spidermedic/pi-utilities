#!/usr/bin/python

# Import Modules
from time import sleep
import subprocess
import RPi.GPIO as GPIO


# Initialize Variables
PIR = 22          # Data pin that the PIR sensor is connected to
timeout = 30      # How long to wait after no movement is detected to turn off the screen
display_on = True # Defaults the screen to "on"

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(PIR, GPIO.IN)

# Main Function
while True:

    if display_on and not GPIO.input(PIR):
        subprocess.run("vcgencmd display_power 0 > /dev/null 2>&1", shell=True)
        display_on = False

    if not display_on and GPIO.input(PIR):
        subprocess.run("vcgencmd display_power 1 > /dev/null 2>&1", shell=True)
        display_on = True
        sleep(timeout)

    sleep(0.5)