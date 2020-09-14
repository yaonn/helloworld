from RPi import GPIO
#import time
from threading import Timer


def off():
	try:
		GPIO.output(7, GPIO.LOW)
		GPIO.cleanup()
	except Exception as e:
		print(e)

def on():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7, GPIO.OUT)
		GPIO.output(7, GPIO.HIGH)
		#time.sleep(20)
		offLED = Timer(20, off)
		offLED.start()
	except Exception as e:
		print(e)