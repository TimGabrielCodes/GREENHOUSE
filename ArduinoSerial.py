#!/usr/bin/env python3.7.3

import serial
import urllib
import http.client as httplib
from flask import Flask, app, render_template, jsonify
 
thingspeakwritekey ="GINQ9FW2MPP1XPLS"
humidity = ""
temperature = ""
lightintensity = ""
soilwater = ""

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
  
while True:
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
        
        
                    
        params = urllib.parse.urlencode({'field1': temperature, 'field2' : humidity, 'field3' : lightintensity, 'field4' : soilwater, 'key':thingspeakwritekey }) 
        headers = {"content-typzze": "application/x-www-form-urlencoded","accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("post", "/update", params, headers)
            response = conn.getresponse()
            
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")

            
                

    
