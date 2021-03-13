import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
sleepTime = .1

#GPIO Pin of the component
lightPin = 21
buttonPin = 26

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.output(lightPin, GPIO.input(buttonPin))
    sleep(.1)
