import os, time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:

        GPIO.wait_for_edge(23, GPIO.RISING)
	subprocess.call(["sudo", "shutdown", "-h","now"])
        break

