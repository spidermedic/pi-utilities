#!/usr/bin/python3

import requests
import subprocess
import paho.mqtt.client as mqtt
from time import sleep

# Get CPU temp
t = str(subprocess.check_output(["vcgencmd", " measure_temp"]))
cpuTemp = t[7:11] +  " °C"
# print(cpuTemp)

# Get free memory
with open("/proc/meminfo", "r") as f:
    m = float(f.readline().split()[1])
    memFree = str(round(m/1000)) + " mb"
    # print(memFree)

# Get free disk space
d = str(subprocess.check_output(["df", "-h", "/"])).split()[7]
diskFree = str(d[:-1]) + " gb"
# print(diskFree)



# Send MQTT message for the Magic Mirror
client = mqtt.Client("playground") # Create a new instance
client.connect("playground.local") # Connect to the broker
client.loop_start()
client.publish("playground/cpuTemp", cpuTemp) # Publish CPU temp
client.publish("playground/memFree", memFree) # Publish Free Memory
client.publish("playground/diskFree", diskFree) # Publish Free Disk Space
client.loop_stop()
