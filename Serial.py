#!/usr/bin/env python3

import serial
if __name__ == '__main__':
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