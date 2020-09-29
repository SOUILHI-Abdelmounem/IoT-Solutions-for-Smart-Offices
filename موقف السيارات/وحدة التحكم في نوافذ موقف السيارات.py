
from time import *
from gpio import *
from ioeclient import *

def onInputReceive(input):
	if input == "1":
		
		for i in range(1,5):
			customWrite(i,HIGH)
	
	else:
		
		for i in range(1,5):
			customWrite(i,LOW)

def main():
	for i in range(1,5):
		pinMode(i, OUT)
		
	# Setup Registration Server	
	IoEClient.setup({
		"type": "WinControl",
		"states": [{
			"name": "State",
			"type": "options",
			"options": {
				"0" : "closed",
				"1" : "open"
			},
			"controllable": True
		}]
	});
	IoEClient.onInputReceive(onInputReceive)
	while True:
		delay(500)
if __name__ == "__main__":
	main()

