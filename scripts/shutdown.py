import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(3, GPIO.RISING)
    time.sleep(10)
    if GPIO.input(3):
        subprocess.call(['shutdown', '-h', 'now'], shell=False)

