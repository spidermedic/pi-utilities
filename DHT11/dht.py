import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin = 17)

# initialize variables
t_ave = []
h_ave = []
x = 0

while  x < 20:

    result = instance.read()

    if result.is_valid():
        t_ave.append(result.temperature)
        h_ave.append(result.humidity)
        print(x)
        x += 1

print(sum(t_ave) / len(t_ave) * 1.8 + 32)
print(sum(h_ave) / len(h_ave))
