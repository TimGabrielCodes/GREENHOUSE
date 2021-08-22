from flask import Flask, render_template, jsonify
import serial
import datetime


app = Flask(__name__, template_folder="../web")
app.debug = True
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

@app.route("/index")
def index():
   return render_template("index.html")

@app.route("/update")
def update():
    

   
    print(ser.in_waiting)
    
    
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        humidity = line[0:5]
        temperature = line[6:11]
        lightintensity = line[12:15]
        soilwater = line[16:19]
        now = datetime.datetime.now()
        
        # print(line)
        # print(temperature)
        # print(humidity)
        # print(lightintensity)
        # print(soilwater)
        # templateData = {temperature}
        templateData = {'time' : now.strftime('%m-%d-%y %H:%M:%S'),'Temperature' : temperature, 'Humidity' : humidity , 'Light Intensity' : lightintensity, 'Soil Water Level': soilwater, 'Status' : 200}
        return jsonify(templateData)
        
    else: 
            return "No Data", 400
        
if __name__ == "__main__":
    app.run()