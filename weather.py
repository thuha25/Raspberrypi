import requests
import RPi.GPIO as GPIO
import time

INTERVAL = 1
THRESHOLD = 25

GPIO. setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

key = '5af21e4aab63472a8ff41909242604'
location = 'Da Nang'
ApiUrl = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}"
while True:
    r = requests.get(ApiUrl)
    forecast = r.json()
    popValue = forecast['current']['temp_c']
    print(f'Temperature: {popValue}')
    # print(r.json())
    # popValue = int(popValue)
    if popValue >= THRESHOLD:
        GPIO.output(25, GPIO.HIGH)
    else:
        GPIO.output(25, GPIO.LOW)
    time. sleep(INTERVAL)
