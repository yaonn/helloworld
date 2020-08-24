import sys
from RPi import GPIO
import time
import requests

try:
	if sys.argv[1]:
		order = sys.argv[1]
		if order != 'on' and order != 'off':
			print('arg must be on/off')
		else:
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(7, GPIO.OUT)
			if order == 'on':
				GPIO.output(7, GPIO.HIGH)
				input('enter')
			else:
				GPIO.output(7, GPIO.Low)
				input('enter')
	else:
		print('call with arg on/off')
		x = requests.get('192.168.5.27:5000/listen')
		print(x)
		order = x.text
		print(order)
except Exception as e:
	print(e)
finally:
	GPIO.cleanup()
