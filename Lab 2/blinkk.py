import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(21, GPIO.OUT) # output rf
GPIO.output(21, True)
time.sleep(1)
GPIO.output(21, False)
print("clean up")
GPIO.cleanup() # cleanup all GPIO
