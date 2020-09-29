
var value = Environment.getTimeInSeconds();
var hour=Math.floor(value/3600);
var minute=Math.floor(((value%86400)%3600)/60)

function setup() {
	pinMode(0, INPUT);
	pinMode(1, INPUT);
	pinMode(2, OUTPUT);
	pinMode(3, OUTPUT);
}

function loop() {

	var light=digitalRead(0);
	var wind=digitalRead(1);
	
	Serial.println("light = "+light);
	Serial.println("wind = "+wind);

	if ((hour>=8 && hour<17) && (light===1023 && wind===0)){

		customWrite(2,HIGH);
		customWrite(3,HIGH);
	
	}
	else {
		
		customWrite(2,LOW);
		customWrite(3,LOW);
		}
		
	delay(1000);
}
