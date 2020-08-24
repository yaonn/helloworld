import requests
from RPi import GPIO

x = requests.get('http://192.168.5.27/listen')
print(x)
