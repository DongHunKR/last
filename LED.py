import RPi.GPIO as GPIO
from time import sleep
LED= 8
Switch= 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)
try:
	while True:
		if GPIO.input(Switch) == GPIO.HIGH:
			print("LED ON")
			GPIO.output(LED, GPIO.HIGH)
			sleep(0.1)
		else:
			print("LED OFF")
			GPIO.output(LED, GPIO.LOW)
			sleep(0.1)
finally:
	GPIO.cleanup()
