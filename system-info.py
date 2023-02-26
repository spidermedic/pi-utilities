#!/usr/bin/python

import subprocess
import paho.mqtt.client as mqtt


def cpu_temp():
    try:
        temp = str(subprocess.check_output(["vcgencmd", " measure_temp"]))
        return f"{temp[7:11]} °C"
    except:
        return "-"


def free_memory():
    try:
        with open("/proc/meminfo", "r") as f:
            memory = float(f.readline().split()[1])
            return f"{str(round(memory/1000))} mb"
    except:
        return "-"
    

def free_disk_space():
    try:
        disk_free = str(subprocess.check_output(["df", "-h", "/"])).split()[7]
        return f"{str(disk_free[:-1])} gb"
    except:
        return "-"

def send_mqtt_data():
    client = mqtt.Client("playground") # Create a new instance
    client.connect("playground.local") # Connect to the broker
    
    client.loop_start()
    client.publish("playground/cpuTemp", cpu_temp()) # Publish CPU temp
    client.publish("playground/memFree", free_memory()) # Publish Free Memory
    client.publish("playground/diskFree", free_disk_space()) # Publish Free Disk Space
    client.loop_stop()


def main():
    send_mqtt_data()


if __name__ == "__main__":
    main()