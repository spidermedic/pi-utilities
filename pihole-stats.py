
import requests
import paho.mqtt.client as mqtt

topic = "pihole/"

# Query the pihole
try:
    r = requests.get("http://192.168.1.10/admin/api.php?summary")
    r.raise_for_status()  # raise an exception if the HTTP status code is not 2xx
except requests.exceptions.RequestException as e:
    print(f"\nUnable to fetch data. Error: {str(e)}")
    exit(1)

# Parse the JSON data
try:
    data = r.json()
    status = data.get("status")
    dns_queries_today = data.get("dns_queries_today")
    ads_blocked_today = data.get("ads_blocked_today")
    days = data.get("gravity_last_updated").get("relative").get("days")
    hours = data.get("gravity_last_updated").get("relative").get("hours")
    upTime = f"{round((int(days) + int(hours)/24), 1)} days"
except (ValueError, KeyError) as e:
    print(f"\nUnable to parse JSON data. Error: {str(e)}")
    exit(1)

# Send the data using MQTT
client = mqtt.Client("pihole") # Create a new instance
client.connect("192.168.1.10") # Connect to the broker

client.loop_start()
client.publish(f"{topic}status", status) # Publish Door A status
client.publish(f"{topic}queries", dns_queries_today) # Publish Door B status
client.publish(f"{topic}blocked", ads_blocked_today) # Publish Door B status
client.publish(f"{topic}upTime", upTime) # Publish uptime
client.loop_stop()

exit(0)