import RPi.GPIO as GPIO
import time 



GPIO.setmode(GPIO.BOARD)

#pin_nos=[8,10,12,16,22,18,24,26]
pin_nos=[22,18,24,26,8,10,12,16]
# Motor 1 pin mode
GPIO.setup(pin_nos[0],GPIO.OUT)
GPIO.setup(pin_nos[1],GPIO.OUT)

# Motor 2 pin mode
GPIO.setup(pin_nos[2],GPIO.OUT)
GPIO.setup(pin_nos[3],GPIO.OUT)

# Motor 3 pin mode
GPIO.setup(pin_nos[4],GPIO.OUT)
GPIO.setup(pin_nos[5],GPIO.OUT)

# Motor 4 pinmode
GPIO.setup(pin_nos[6],GPIO.OUT)
GPIO.setup(pin_nos[7],GPIO.OUT)

def stop():
	# Motor 1 in clockwise
	GPIO.output(pin_nos[0] ,GPIO.LOW)
	GPIO.output(pin_nos[1] ,GPIO.LOW)
	
	# Motor 2 in clockwise
	GPIO.output(pin_nos[2] ,GPIO.LOW)
	GPIO.output(pin_nos[3] ,GPIO.LOW)
	
	# Motor 3 in clockwise
	GPIO.output(pin_nos[4] ,GPIO.LOW)
	GPIO.output(pin_nos[5] ,GPIO.LOW)
	
	# Motor 4 in clockwise
	GPIO.output(pin_nos[6] ,GPIO.LOW)
	GPIO.output(pin_nos[7] ,GPIO.LOW)

def move_fwd():
	# Motor 1 in clockwise direction
	GPIO.output(pin_nos[0] ,GPIO.HIGH)
	GPIO.output(pin_nos[1] ,GPIO.LOW)
	# Motor 3 in anti-clockwise direction
	GPIO.output(pin_nos[4] ,GPIO.LOW)
	GPIO.output(pin_nos[5] ,GPIO.HIGH)
	
	GPIO.output(pin_nos[2] ,GPIO.LOW)
	GPIO.output(pin_nos[3] ,GPIO.LOW)
	
	GPIO.output(pin_nos[6] ,GPIO.LOW)
	GPIO.output(pin_nos[7] ,GPIO.LOW)
	
def move_backward():
	# Motor 1 in anti-clockwise direction
	GPIO.output(pin_nos[0] ,GPIO.LOW)
	GPIO.output(pin_nos[1] ,GPIO.HIGH)
	# Motor 3 clockwise direction
	GPIO.output(pin_nos[4] ,GPIO.HIGH)
	GPIO.output(pin_nos[5] ,GPIO.LOW)
	
	GPIO.output(pin_nos[2] ,GPIO.LOW)
	GPIO.output(pin_nos[3] ,GPIO.LOW)
	
	GPIO.output(pin_nos[6] ,GPIO.LOW)
	GPIO.output(pin_nos[7] ,GPIO.LOW)
	

def move_left():
	# Motor 2 in clockwise direction
	GPIO.output(pin_nos[2] ,GPIO.HIGH)
	GPIO.output(pin_nos[3] ,GPIO.LOW)
	# Motor 4 anti-clockwise direction
	GPIO.output(pin_nos[6] ,GPIO.LOW)
	GPIO.output(pin_nos[7] ,GPIO.HIGH)
	
	GPIO.output(pin_nos[0] ,GPIO.LOW)
	GPIO.output(pin_nos[1] ,GPIO.LOW)
	
	GPIO.output(pin_nos[4] ,GPIO.LOW)
	GPIO.output(pin_nos[5] ,GPIO.LOW)
	
def move_right():
	# Motor 2 in anti-clockwise direction
	GPIO.output(pin_nos[2] ,GPIO.LOW)
	GPIO.output(pin_nos[3] ,GPIO.HIGH)
	# Motor 4 clockwise direction
	GPIO.output(pin_nos[6] ,GPIO.HIGH)
	GPIO.output(pin_nos[7] ,GPIO.LOW)
	
	GPIO.output(pin_nos[0] ,GPIO.LOW)
	GPIO.output(pin_nos[1] ,GPIO.LOW)
	
	GPIO.output(pin_nos[4] ,GPIO.LOW)
	GPIO.output(pin_nos[5] ,GPIO.LOW)
	
def move_clockwise():
	# Motor 1 in clockwise
	GPIO.output(pin_nos[0] ,GPIO.HIGH)
	GPIO.output(pin_nos[1] ,GPIO.LOW)
	
	# Motor 2 in clockwise
	GPIO.output(pin_nos[2] ,GPIO.HIGH)
	GPIO.output(pin_nos[3] ,GPIO.LOW)
	
	# Motor 3 in clockwise
	GPIO.output(pin_nos[4] ,GPIO.HIGH)
	GPIO.output(pin_nos[5] ,GPIO.LOW)
	
	# Motor 4 in clockwise
	GPIO.output(pin_nos[6] ,GPIO.HIGH)
	GPIO.output(pin_nos[7] ,GPIO.LOW)
	
def move_anticlockwise():
	# Motor 1 in anti-clockwise
	GPIO.output(pin_nos[0] ,GPIO.LOW)
	GPIO.output(pin_nos[1] ,GPIO.HIGH)
	
	# Motor 2 in anti-clockwise
	GPIO.output(pin_nos[2] ,GPIO.LOW)
	GPIO.output(pin_nos[3] ,GPIO.HIGH)
	
	# Motor 3 in anti-clockwise
	GPIO.output(pin_nos[4] ,GPIO.LOW)
	GPIO.output(pin_nos[5] ,GPIO.HIGH)
	
	# Motor 4 in anti-clockwise
	GPIO.output(pin_nos[6] ,GPIO.LOW)
	GPIO.output(pin_nos[7] ,GPIO.HIGH)



while True:
	
	try :
		inp = str(input(""))
		if inp == "e" :
			move_clockwise()
			time.sleep(4)
		elif inp == "w" :
			move_fwd()
			time.sleep(4)
		elif inp == "s" :
			move_backward()
			time.sleep(4)
		elif inp == "a" :
			move_left()
			time.sleep(4)
		elif inp=="d"	:
			move_right()
			time.sleep(4)
		elif inp=="r"	:
			move_anticlockwise()
			time.sleep(4)
		else:
			stop()
			GPIO.cleanup()
			print("over")
			break

	except :
		GPIO.cleanup()
		print("here")
		break

# # Tele-OP


