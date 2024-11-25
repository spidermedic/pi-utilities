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

    if display_on and not GPIO.input(PIR_GPIO):
        # subprocess.run(["xset dpms force off"], shell=True)
        # subprocess.run("xrandr --display :0 --output HDMI-1 --off > /dev/null 2>&1", shell=True)
        subprocess.run("vcgencmd display_power 0 > /dev/null 2>&1", shell=True)
        display_on = False
        print("Force Off Sent")

    if not display_on and GPIO.input(PIR_GPIO):
        # subprocess.run(["xset dpms force on"], shell=True)
        # subprocess.run("xrandr --display :0 --output HDMI-1 --mode 1920x1080 --rate 60 > /dev/null 2>&1", shell=True)
        subprocess.run("vcgencmd display_power 1 > /dev/null 2>&1", shell=True)
        display_on = True
        print("Force On Sent")
        sleep(60)

    sleep(0.5)
