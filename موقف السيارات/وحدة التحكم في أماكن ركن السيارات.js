
var i;
function setup(){
	for (i=0;i<=3;i++){
		pinMode(i,INPUT);
	}
	for (i=4;i<=7;i++){
		pinMode(i,OUTPUT);
	}
}
function loop(){
	
	if (digitalRead(0)==1023){
		digitalWrite(4,HIGH);
	}
	else{
		analogWrite(4,LOW);
	}
	if (digitalRead(1)==1023){
		digitalWrite(5,HIGH);
	}
	else{
		digitalWrite(5,LOW);
	}
	if (digitalRead(2)==1023){
		digitalWrite(6,HIGH);
	}
	else{
		digitalWrite(6,LOW);
	}
	if (digitalRead(3)==1023){
		digitalWrite(7,HIGH);
	}
	else{
		digitalWrite(7,LOW);
	}
	delay(500);
}
