'''Class to run servo motor.'''

import RPi.GPIO as gpio
import time

class Servo():

# Configures servoPin as output pin for servo.
	def __init__(self,servoPin):
		self.servoPin = servoPin
		gpio.setwarnings(False)
		gpio.setmode(gpio.BCM)
		gpio.setup(self.servoPin,gpio.OUT)

# Starts pwm for servo control at servoPin.
	def start(self,pwmFreq):
		self.pwmFreq = int(pwmFreq)
		self.pwm = gpio.PWM(self.servoPin,self.pwmFreq)
		self.pwm.start(1)

# Sends servo rotor to specified angle.
	def goto(self,angle):
		self.duty = angle/15
		self.pwm.ChangeDutyCycle(self.duty)

# Continuously runs servo between two angles.
	def run(self,startAngle,endAngle,stepDelay): #Angles in multiples of 15 degrees
		self.sAngle = startAngle/15
		self.eAngle = endAngle/15
		self.delay = stepDelay
		while True:
			for i in range(self.sAngle,self.eAngle):
				self.pwm.ChangeDutyCycle(i)
				time.sleep(self.delay)
			for j in range(self.eAngle,self.sAngle,-1):
				self.pwm.ChangeDutyCycle(j)
				time.sleep(self.delay)



if __name__ == "__main__":
	servo1 = Servo(18)
	servo1.start(60)
	servo1.run(60,120,0.05)

