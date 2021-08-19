from flask import Flask, render_template, jsonify
import serial


app = Flask(__name__)
app.debug = True
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

@app.route("/main")
def main():
   return "Hello WOrld"

@app.route("/update")
def update():
    

   
    print(ser.in_waiting)
    
    
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        humidity = line[0:5]
        temperature = line[6:11]
        lightintensity = line[12:15]
        soilwater = line[16:19]
        print(line)
        print(temperature)
        print(humidity)
        print(lightintensity)
        print(soilwater)
        templateData = {'temperature' : temperature, 'humidity' : humidity , 'Light Intensity' : lightintensity, 'Soil Water Level': soilwater}
        return jsonify(templateData), 200
        
    else: 
            return "here"
        
if __name__ == "__main__":
    app.run()