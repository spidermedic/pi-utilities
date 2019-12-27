#!/usr/bin/env python3

import requests
import subprocess
import paho.mqtt.client as mqtt

# Get CPU temp
t = str(subprocess.check_output(["vcgencmd", " measure_temp"]))
cpuTemp = t[7:11] + "°C"

# Get uptime
with open('/proc/uptime', 'r') as f:
    u = float(f.readline().split()[0])
    upTime = str(round(u/86400, 1)) + " days" # Converts seconds into days

# Send MQTT message for the Magic Mirror
client = mqtt.Client("mirror") # Create a new instance
client.connect("192.168.1.10") # Connect to the broker
client.loop_start()
client.publish("mirror/cpuTemp", cpuTemp) # Publish CPU temp
client.publish("mirror/upTime", upTime) # Publish uptime
client.loop_stop()
