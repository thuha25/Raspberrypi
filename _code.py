import RPi.GPIO as GPIO
import time
import keyboard

# Set up GPIO pin 25 as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

# Blink the LED every 1 second
while not keyboard.is_pressed('Q'):
    GPIO.output(25, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(25, GPIO.LOW)
    time.sleep(1)

# Clean up GPIO resources
GPIO.cleanup()
