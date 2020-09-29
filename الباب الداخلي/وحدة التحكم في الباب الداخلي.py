
from time import *
from gpio import *
from ioeclient import *

def onInputReceive(input):

	if input=="0":
		digitalWrite(0,HIGH)
	else :
		digitalWrite(0,LOW)
	if input=="1":
		digitalWrite(1,HIGH)
	else:
		digitalWrite(1,LOW)
	if input=="2":
		digitalWrite(2,HIGH)
	else:
		digitalWrite(2,LOW)
		
def main():
	
	# Setup Registration Server	
	IoEClient.setup({
		"type": "SOUND",
		"states": [{
			"name": "official",
			"type": "options",
			"options": {
				"0" : "SAID",
				"1" : "MOHAMED IMAD",
				"2" : "STRANGE"
			},
			"controllable": False
		}]
	});

	IoEClient.onInputReceive(onInputReceive)

	while True:
		delay(500)

if __name__ == "__main__":
	main()
