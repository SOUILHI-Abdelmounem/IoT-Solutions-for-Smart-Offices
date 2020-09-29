
var dstService = "{00000000-0000-0000-0000-000000000001}";
var dstMac = "FFFF.FFFF.FFFF";
var service;

function setup() {
	
	setDeviceProperty(getName(), 'IR', 900);
	service = new BluetoothService();
	
	// when receiving data
	service.onReceive = function(srcMac, srcService, dstMac, dstService, data) {
		Serial.println(data);
		
		switch (data){
			case "UP"   : moveBy(0,-20);
				 	      break;
		 	case "RIGHT": moveBy(60,0);
		 			      break;
		 	case "DOWN" : moveBy(0,20);
		 			      break;
		 	default :     moveBy(-60,0);
		 			      break;
		}
	};
	// start service
	Serial.println(service.start(dstService));
}

