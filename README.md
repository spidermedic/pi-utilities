## pir
IR sensor software for Raspberry Pi
PIR is a simple python program that can be run via crontab. It will turn on the screen attached to a Raspberry Pi when motion is detected and will turn off the screen after a period of no movement.

The easiest way to run pir is via `crontab -e` and adding the line `@reboot python3 /home/pi/pir.py`

I use this for my Magic Mirror and it works great!

## pihole-stats
pihole-stats will query your PiHole for the latest information and send the data via MQTT. I use this to send information to my Magic Mirror. Requires `paho.mqtt.client`.

## system-info
system-info collects information about your RPi and broadcasts it via MQTT. Requires `paho.mqtt.client`.

## DHT11
Contains small programs that use the DHT11 temp/humitidy sensor and stand-alone moisture sensors.