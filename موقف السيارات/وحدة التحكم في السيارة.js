
var dstService = "{00000000-0000-0000-0000-000000000001}";
var dstMac = "FFFF.FFFF.FFFF";
var service;
function setup() {
	
	pinMode(0,INPUT);
	pinMode(1,INPUT);
	pinMode(2,INPUT);
	pinMode(3,INPUT);
	
	service = new BluetoothService();
	// start service
	Serial.println(service.start(dstService));
}

function loop() {
	
	if (digitalRead(0)==1023){
		service.send(dstMac, dstService, "UP");
	}
	if (digitalRead(1)==1023){
		service.send(dstMac, dstService, "RIGHT");
	}
	if (digitalRead(2)==1023){
		service.send(dstMac, dstService, "DOWN");
	}
	if (digitalRead(3)==1023){
		service.send(dstMac, dstService, "LEFT");
	}
	
}
