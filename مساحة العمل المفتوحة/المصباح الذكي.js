
var value = Environment.getTimeInSeconds();
var hour=Math.floor(value/3600);
var minute=Math.floor(((value%86400)%3600)/60)

function loop(){

	var Battery=digitalRead(0)

	if (Battery>0 && ((hour>=8) && (hour<17))){
		setComponentOpacity("black",0);
	}
	else{
		setComponentOpacity("black",1);
	}
	delay(1000);
}
