import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from datetime import datetime
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
from time import sleep

#button input
GPIO.setmode(GPIO.BCM)
sleepTime = .1

#GPIO Pin of the component
lightPin = 21
buttonPin = 26

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Image Formatting
def image_formatting(imagef, width, height):
    imagef = imagef.convert('RGB')
    imagef = imagef.resize((240, 135), Image.BICUBIC)

    return imagef


# Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py
    x = 4
    y = 10

    if GPIO.input(buttonPin):
        GPIO.output(lightPin, True)
        sleep(.1)
    else:
        GPIO.output(lightPin, False)


    if buttonA.value and buttonB.value: #without any button pressed
        image3 = Image.open("Schrodingercat00.jpg")
        image3 = image_formatting(image3, width, height)

        draw = ImageDraw.Draw(image3)

        draw.text((x, y), strftime("%H:%M:%S%p"), font=font, fill="#000000")


    elif buttonB.value and not buttonA.value:  # press button A
        image3 = Image.open("Schrodingercat11.jpg")
        image3 = image_formatting(image3, width, height)

        draw = ImageDraw.Draw(image3)

        draw.text((4, 0), "Time A: Cat Alive", font=font1, fill="#FFFF00")
        draw.text((x, y), strftime("%H:%M:%S%p"), font=font, fill="#000000")


    elif buttonA.value and not buttonB.value:  # press button B
        image3 = Image.open("Schrodingercat2.jpg")
        image3 = image_formatting(image3, width, height)

        draw = ImageDraw.Draw(image3)

        draw.text((4, 0), "Time B: Cat Dead", font=font1, fill="#FFFF00")
        draw.text((x, y), strftime("%H:%M:%S%p"), font=font, fill="#000000")


    else: #press both button A and B
        image3 = Image.open("Schrodingercat33.jpg")
        image3 = image_formatting(image3, width, height)

        draw = ImageDraw.Draw(image3)

        draw.text((4, 0), "Cat Alive & Dead at once", font=font1, fill="#FFFFFF")
        draw.text((x, y), strftime("%H:%M:%S%p"), font=font, fill="#000000")


    # Display image.
    disp.image(image3, rotation)
    time.sleep(1)
