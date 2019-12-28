#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from send_email import sendmail

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Set GPOI channel
channel = 17

# Define the GPIO pin that we have our digital output from our sensor connected to
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

def main():
    """Main function"""
    quit()

def callback(channel):
    """Query GPIO pin"""

    subject = "Humidifer bucket at 50%"
    message = "Time to empty the bucket!"

    if GPIO.input(channel):
        print("Water detected")
        sendmail(subject, message)

# This is an infinte loop to keep our script running
while True:
    time.sleep(3600)
