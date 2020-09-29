function setup(){
	pinMode(0,INPUT);
	pinMode(1,INPUT);
	pinMode(2,OUTPUT);
	pinMode(3,OUTPUT);
}
function loop(){
	var SensorIn=digitalRead(0);
	var SensorOut=digitalRead(1);
	if (SensorIn==1023 || SensorOut==1023){
		customWrite(2,HIGH);
		customWrite(3,HIGH);
	}
	else{
		customWrite(2,LOW);
		delay(1000);
		customWrite(3,LOW);
	}
 	delay(500);
}
