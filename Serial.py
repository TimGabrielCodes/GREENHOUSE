#!/usr/bin/env python3

import serial
import urllib
import httplib

if __name__ == '__main__':
    thingSpeakWriteKey ="VB7HT14R9VZ9HAX8"
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            humidity = line[0:5]
            temperature = line[6:11]
            lightIntensity = line[12:15]
            
            print(line)
            print(temperature)
            print(humidity)
            print(lightIntensity)
            
                     
            params = urllib.urlencode({'field1': temperature, 'field2' : humidity, 'field3' : lightIntensity, 'key':thingSpeakWriteKey }) 
            headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
               
                print (response.status, response.reason)
                data = response.read()
                conn.close()
            except:
                print ("connection failed")
            