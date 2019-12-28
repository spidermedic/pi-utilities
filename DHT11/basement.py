#!/usr/bin/python

# Imported Modules
import sys
import RPi.GPIO as GPIO
import time
import dht11
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

def main():

    check_bucket()
    if check_bucket() != "":
        message = (check_bucket() + "\n" + check_temp() + "\n\n")
        sendmail("", message)


def check_bucket():
    """ Reads status of water sensor on pin 4 """

    GPIO.setup(4, GPIO.IN)

    if GPIO.input(4):
        return("Water detected, empty bucket now!")
    else:
        return("")


def check_temp():
    """ Reads DHT11 temp/humidity sensor on pin 17 """

    instance = dht11.DHT11(pin = 17)

    # initialize variables
    t_ave = []
    h_ave = []
    x = 0

    while  x < 10:

        result = instance.read()

        if result.is_valid():
            t_ave.append(result.temperature)
            h_ave.append(result.humidity)
            print(x)
            x += 1

    t_result = sum(t_ave) / len(t_ave) * 1.8 + 32
    h_result = sum(h_ave) / len(h_ave)

    return("Temp: {:.1f}f, Humidity {:.1f}% ".format(t_result, h_result))


def sendmail(subject_line, message_body):
    """ Sends site status to the specified email address """

    # Email Constants
    EMAIL_PASSWORD = ""
    EMAIL_FROM = ""
    EMAIL_TO = ""
    EMAIL_HOST = ""
    EMAIL_PORT = # Integer


    # create message object instance
    msg = MIMEMultipart()

    # setup messge parameters
    password = EMAIL_PASSWORD
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject_line

    # add in the message body
    msg.attach(MIMEText(message_body, 'plain'))

    # create and start server
    server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    server.starttls()

    # login credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # close the server
    server.quit()

if __name__ == '__main__':
    main()
