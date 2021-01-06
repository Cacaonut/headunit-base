import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(24, GPIO.FALLING)
    time.sleep(10)
    if GPIO.input(24):
        subprocess.call(['shutdown', '-h', 'now'], shell=False)

