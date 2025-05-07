'''import RPi.GPIO as GPIO
import time

LED= 10
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
PWM_LED= GPIO.PWM(LED, 50)
PWM_LED.start(0)
while True:
	Duty_led= input('Enter Brightness (0 to 100):')
	duty= int(Duty_led)
	print('Duty rate: ',duty)
	PWM_LED.ChangeDutyCycle(duty)
PWM_LED.stop()
print('Cleaning up!')
GPIO.cleanup()'''


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 10
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
while True:
	GPIO.output(LED, GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(LED, GPIO.LOW)
	time.sleep(0.01)

