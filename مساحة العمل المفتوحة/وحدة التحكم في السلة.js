
var wastLevel=0;
function setup(){
	
	pinMode(0,INPUT);
	pinMode(1,OUTPUT);
	
	addSound('sound1', 'sound/email.mp3');
	EmailClient.setup(
			"said@moneim.com",
			"moneim.com",
			"said",
			"123"
		);
}
function loop() {

	if (digitalRead(0)==1023){
		analogWrite(1,HIGH);
		wastLevel++;
		Serial.println(wastLevel);
		delay(500);
		}
	else{
		analogWrite(1,LOW);
		
	}
	if(wastLevel==3){
		
		EmailClient.onSend = function(status) {
			Serial.println("Sent: " + status);
		};
		EmailClient.send(
			"souilhi@moneim.com", 
			"السلة رقم 01",
			"السلة رقم 01 ممتلئة"
		);
		playSound('sound1', 1);
		wastLevel=0;
		}
	delay(500);
}
