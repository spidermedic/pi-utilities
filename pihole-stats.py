#!/usr/bin/env python3

import requests
import subprocess
import paho.mqtt.client as mqtt

pub_addr = "pihole/1/"

# Get CPU temp
t = str(subprocess.check_output(["vcgencmd", " measure_temp"]))
cpuTemp = t[7:11] + "°C"

# Get the data from PiHole
r = requests.get("http://192.168.1.10/admin/api.php?summary")

# Exit with an error code if the date isn't retrieved
if r.status_code > 301:
    print("\nUnable to fetch data. HTTP: " + str(r.status_code))
    exit(1)

# Parse the json data
status = r.json().get("status")
dns_queries_today = r.json().get("dns_queries_today")
ads_blocked_today = r.json().get("ads_blocked_today")

# Get the uptime days and hours and report as a decimal value
days = r.json().get("gravity_last_updated").get("relative").get("days")
hours = r.json().get("gravity_last_updated").get("relative").get("hours")
upTime = round((int(days) + int(hours)/24), 1) + " days"


# Send MQTT message for the Magic Mirror
client = mqtt.Client("pihole") # Create a new instance
client.connect("192.168.1.10") # Connect to the broker
client.loop_start()
client.publish(pub_addr + "status", status) # Publish Door A status
client.publish(pub_addr + "queries", dns_queries_today) # Publish Door B status
client.publish(pub_addr + "blocked", ads_blocked_today) # Publish Door B status
client.publish(pub_addr + "cpuTemp", cpuTemp) # Publish CPU temp
client.publish(pub_addr + "upTime", upTime) # Publish uptime
client.loop_stop()

exit(0)