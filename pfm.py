#Author: Timothy Do
try: 
	import RPi.GPIO
except ModuleNotFoundError:
	print("You Don't Have GPIO Pins. Terminating...")
	exit()

import os
import wave

print("Welcome to PiFmMorse for Python 3!\n")
print("*******Compiling the FM Transmitter Executable*******\n")
os.system("sudo make")
print("\n*******Finish Compiling the FM Transmitter Executable*******\n")

sequence = []
frames = []