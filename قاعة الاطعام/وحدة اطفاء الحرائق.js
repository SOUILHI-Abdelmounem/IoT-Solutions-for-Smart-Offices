
function setup(){
	
	pinMode(0,INPUT);
	pinMode(1,OUTPUT);		
}
function loop(){
	
	if (digitalRead(0)==1023){
		customWrite(1,1);
	}
	else{
		customWrite(1,0);
	}
	delay(500);
}
