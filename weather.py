import requests
import RPi.GPIO as GPIO
import time

GPIO. setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

key = 'b76982d2c00b478192520802240705'
location = 'Da Nang'
ApiUrl = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}"
while True:
    r = requests.get(ApiUrl)
    forecast = r.json()
    popValue = forecast['current']['temp_c']
    print(f'Temperature: {popValue}')
    # print(r.json())
    # popValue = int(popValue)
    if popValue >= 25:
        GPIO.output(25, GPIO.HIGH)
    else:
        GPIO.output(25, GPIO.LOW)
    time. sleep(180)
