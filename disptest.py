# Imported Modules
from time import sleep
import subprocess
import RPi.GPIO as GPIO


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(22, GPIO.IN)

PIR_GPIO = 22
display_on = True

while True:

    subprocess.run("xrandr --display :0 --output HDMI-1 --off > /dev/null 2>&1", shell=True)

    sleep(0.5)

    subprocess.run("xrandr --display :0 --output HDMI-1 --auto > /dev/null 2>&1", shell=True)

    sleep(0.5)