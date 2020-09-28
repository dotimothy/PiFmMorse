#Author: Timothy Do
try:
	import RPi.GPIO as GPIO
except ModuleNotFoundError:
	print("Abort. No GPIO Pins.")
	exit()

import os

print("Welcome to PiFmMorse for Python 3!\n")
print("*******Compiling the FM Transmitter Executable*******\n")
os.system("make")
print("\n*******Finish Compiling the FM Transmitter Executable*******\n")