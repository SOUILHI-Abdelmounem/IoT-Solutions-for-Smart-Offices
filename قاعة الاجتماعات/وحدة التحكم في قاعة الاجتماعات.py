	

from gpio import *
from time import *
from http import *
from bluetooth import *

dstService = "{00000000-0000-0000-0000-000000000001}"
dstMac = "FFFF.FFFF.FFFF"
service = BluetoothService()

def onRouteRoot(url, res) :
	print("Request for /");
	res.send(getPage());

# ------------------------------------------------------------
def led1On(url, res) :
	print("led1 On");
	digitalWrite(0, HIGH);

def led1Off(url, res) :
	print("led1 Off");
	digitalWrite(0, LOW);
# ------------------------------------------------------------
def led2On(url, res) :
	print("led2 On");
	digitalWrite(1, HIGH);

def led2Off(url, res) :
	print("led2 Off");
	digitalWrite(1, LOW);
# ------------------------------------------------------------
def win1On(url, res) :
	print("window1 on");
	analogWrite(2, HIGH);

def win1Off(url, res) :
	print("window1 off");
	analogWrite(2, LOW);
# ------------------------------------------------------------
def win2On(url, res) :
	print("window2 on");
	digitalWrite(3, HIGH);

def win2Off(url, res) :
	print("window2 off");
	digitalWrite(3, LOW);
# ------------------------------------------------------------
def slideOn(url, res) :
	print("slide on");
#	service = BluetoothService()
	print(service.start(dstService))
	service.send(dstMac, dstService, "SHOW")

def slideOff(url, res) :
	print("slide off");
#	service = BluetoothService()
	print(service.start(dstService))
	service.send(dstMac, dstService, "HIDING")
# ------------------------------------------------------------
def fanLow(url, res) :
	print("fan N-Low");
	customWrite(4, "1");

def fanHigh(url, res) :
	print("fan N-High");
	customWrite(4, "2");
	
def fanShutdown(url, res) :
	print("fan Shut Down");
	customWrite(4, "0");
# ------------------------------------------------------------

# Setup for the root, on and off actions.
def setup() :
	HTTPServer.route("/", onRouteRoot)
	HTTPServer.route("/led1On", led1On)
	HTTPServer.route("/led1Off", led1Off)
	
	HTTPServer.route("/led2On", led2On)
	HTTPServer.route("/led2Off", led2Off)
	
	HTTPServer.route("/win1On", win1On)
	HTTPServer.route("/win1Off", win1Off)
	
	HTTPServer.route("/win2On", win2On)
	HTTPServer.route("/win2Off", win2Off)
	
	HTTPServer.route("/slideOn", slideOn)
	HTTPServer.route("/slideOff", slideOff)
	
	HTTPServer.route("/fanLow", fanLow)
	HTTPServer.route("/fanHigh", fanHigh)
	HTTPServer.route("/fanShutdown", fanShutdown)
	
	# start server on port 80
	HTTPServer.start(80);

def getPage():
	html="""<head>
        <style>
            body{
                background-color: #323232;
                font-family: GE SS Two Light ,Traditional Arabic;
            }
            .div1{
                margin-top: 50px;
                background-color: #323232;
                width: 800px;
                height: 400px;
            }
            .div11{
                background-color:white;
                width: 300px;
                height: 400px;
                float: left;
            }
            .div12{
                background-color:#009dff;
                width: 500px;
                height: 400px;
                float: left;
            }
            .div111{
                margin-top: 150px;
            }
            input{
                margin: 5px;
                height: 30px;
                border-radius: 15px;
                border-color: #bababa;
                border-style: solid;
                text-align: center;
            }
            button{
                width: 80px;
                height: 30px;
                margin-top:  5px;
                border-radius: 15px;
                border-style: solid;
                background-color:#009dff; 
                font-family: GE SS Two Light ,Traditional Arabic;
            }
            button:hover{
                background-color: white;
                border-bottom-color: #009dff;
                border-style: solid;
            }
            #p{
                color: red;
                font-family: GE SS Two Light ,Traditional Arabic;
            }
            .p2{
                color: white;
                font-family: GE SS Two Light ,Traditional Arabic;
                margin-top: 190px;
                font-size: 30;
                border-style: solid;
                width: 300px;
                padding: 5px;
                border-radius: 30px;
            }
        </style>
    </head>
    <body>
        <center>
            <div class="div1">
                <div class="div11">
                    <div class="div111">
                        <center>
                            <p id="p"></p>
                            <p class="p0">u\تسجيل الدخول</p>
                            <input id="in1"><br>
                            <input id="in2" type="password"><br>
                            <button onclick="Login()"> إرسال</button>
                        </center>
                    </div>
                </div>
                <div class="div12">
                    <center>
                        <p class="p2">المكتب الذكي</p>
                    </center>
                </div>
                </div>
        </center>
        <script>
         function Login(){
                var i,d;
                var s=" ";
                var i1=document.getElementById("in1").value;
                var i2=document.getElementById("in2").value;
                
                for(i=0;i<(i1+i2).length;i++){ 
                     
                  s+=(i2+i1).charCodeAt(i)
                }
                  d=(i2.length+parseInt(s+i2)).toString(16);
                  if (d==="1997f266644667000000000"){
                    Home();
                }
                else{
                    document.getElementById("p").innerHTML="خطأ في عملية التسجيل";
                }
                }
            function Home(){
                var s='';
           s+=' <style>'
    s+='   body {'
    s+='       font-family: GE SS Two Light ,Traditional Arabic;'
         s+='   color: white;'
        s+='}'
        s+='.div1a {'
            s+='background-color: #323232;'
            s+='height: 500px;'
            s+='width: 900px;'
            s+='margin: 0px;'
            s+='padding: 0px;'
        s+='}'
        s+='.div2a {'
            s+='background-color: #c8c7c9;'
            s+='height: 500px;'
            s+='width: 400px;'
            s+='float: left;'
            s+='margin: 0px;'
            s+='padding: 0px;'
        s+='}'
      s+='  .div4a {'
          s+='  background-color: #323232;'
            s+='height: 60px;'
        s+='    width: 370px;'
        s+='    float: left;'
            s+='margin: 15px;'
            s+='padding: 0px;'
        s+='}'
        s+='.div3a {'
            s+='background-color: #323232;'
            s+='height: 500px;'
            s+='width: 500px;'
            s+='float: right;'
            s+='margin: 0px;'
            s+='padding: 0px;'
            s+='background-image: url(moneimB0.png);'
            s+='background-position: center;'
            s+='background-size: cover'
        s+='}'
        s+='li {'
            s+='float: right;'
            s+='display: block;'
            s+='margin: 15px;'
            s+='width: 60px;'
            s+='height: 60px;'
            s+='text-align: center;'
            s+='margin-top: 20px;'
        s+='}'
        s+='.btn0 {'
            s+='font-family: GE SS Two Light ,Traditional Arabic;'
            s+='background-color: #323232;'
            s+='border: none;'
            s+='width: 60px;'
            s+='height: 90px;'
            s+='color: white;'
        s+='}'
        s+='.btn0:hover {'
            s+='background-color: #0093ff;'
        s+='}'
    s+='</style>'
            s+='<body>'
   s+=' <center>'
      s+='  <div class="div1a">'
          s+='  <div class="div2a">'
              s+='  <div class="div4a">'
                  s+='  <p>المكتب الذكي</p>'
                s+='</div>'
                s+='<ul>'
                    s+='<li>'
                        s+='<form method="get" action="/led1On"><button type="submit" class="btn0">فتح المصباح<p>1</p></button></form>'
                    s+='</li>'
                s+='    <li>'
                    s+='    <form method="get" action="/led1Off"><button type="submit" class="btn0">غلق المصباح<p>1</p></button></form>'
                    s+='</li>'
                    s+='<li><form method="get" action="/led2On"><button type="submit" class="btn0">فتح المصباح<p>2</p></button></form></li>'
                    s+='<li><form method="get" action="/led2Off"><button type="submit" class="btn0">غلق المصباح<p>2</p></button></form></li>'
                s+='</ul>'
            s+='    <ul>'
                s+='    <li>'
                    s+='    <form method="get" action="/win1On"><button type="submit" class="btn0">رفع الستار<p>1</p></button></form>'
                    s+='</li>'
                    s+='<li>'
                        s+='<form method="get" action="/win1Off"><button type="submit" class="btn0">اسدال الستار<p>1</p></button></form>'
                    s+='</li>'
                    s+='<li><form method="get" action="/win2On"><button type="submit" class="btn0">رفع الستار<p>2</p></button></form></li>'
                    s+='<li><form method="get" action="/win2Off"><button type="submit" class="btn0">اسدال الستار<p>2</p></button></form></li>'
                s+='</ul>'
                s+='<ul >'
                s+='<li><form method="get" action="/slideOn"><button type="submit" class="btn0">إظهار شاشة العرض</button></form></li>'
                    s+='<li><form method="get" action="/slideOff"><button type="submit" class="btn0">إخفاء شاشة العرض</button></form></li>'
                s+='<li><form method="get" action="/fanLow"><button type="submit" class="btn0">المروحة<p>N-Low</p></button></form></li>'
                 s+='<li><form method="get" action="/fanHigh"><button type="submit" class="btn0">المروحة<p>N-High</p></button></form></li>'
                    s+='<li><form method="get" action="/fanShutdown"><button type="submit" class="btn0">المروحة<p>Shut-D</p></button></form></li>'
                    s+='<li><button type="submit" class="btn0">.</button></li>'
                    s+='<li><button type="submit" class="btn0">.</button></li>'
                    s+='<li><button type="submit" class="btn0">.</button></li>'
                s+='</ul>'
            s+='</div>'
            s+='<div class="div3a">'
            s+='<p style="margin-top: 200; font-size: 40; font-family: sans-serif" >SmartOffice</p>'
            s+='<p style="margin-top: 200; font-size: 20; font-family: sans-serif" >IoT</p>'
            s+='</div>'
        s+='</div>'
    s+='</center>'
s+='</body>'
            document.write(s);
        }
        </script>
    </body>"""

	return html;
    
def main():
	for i in range(5):
		pinMode(i,OUT)
		
	setup()
	while True:
		delay(2000)
if __name__ == "__main__":
	main()
