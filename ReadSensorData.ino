/* IOT Based Greenhouse Monitoring System
*/

//Libraries
#include <DHT.h>
#include <LiquidCrystal.h>


//Constants
#define DHTPIN 7     // what pin we're connected to
#define  DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
LiquidCrystal lcd (12, 11, 5, 4, 3, 2);

//Define light bulbs
const int  statusLED =  6;
const int lightLED = 10;
const int coolerLED =   8;
const int soilLED =  9;



//Variables
int chk;
int lightIntensity;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16, 2);
  lcd.print("Hello Tim!!!");


  //Initialize bulb pins
  pinMode(statusLED, OUTPUT);
  pinMode(lightLED, OUTPUT);
  pinMode(coolerLED, OUTPUT);
  pinMode(soilLED, OUTPUT);

  delay(2000);
}

void loop()
{  
  turnOn(statusLED);
  lcd.clear();

  //Read Light Intensity
  lightIntensity = analogRead(A0);

    if(lightIntensity < 400) {
     turnOn(lightLED);
  } else{
    turnOff(lightLED);
  }




  //Read data and store it to variables hum and temp
  hum = dht.readHumidity();
  temp = dht.readTemperature();

  if(temp > 29.90) {
     turnOn(coolerLED);
  } else{
    turnOff(coolerLED);
  }
  //Print temp and humidity values to serial monitor
  Serial.print(hum);
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.println(lightIntensity);
  
//  Serial.print("Humidity: ");
//  Serial.print(hum);
//  Serial.print(" %,");
//  Serial.print("Temp: ");
//  Serial.print(temp);
//  Serial.println(" *C");
//  Serial.print("Light Intensity :");
//  Serial.println(lightIntensity);

  lcdPrint(temp, hum, lightIntensity);

  delay(1000); //Delay 3 sec.

}

void turnOn( int pinNumber) {
  digitalWrite(pinNumber, HIGH);
 
}

void turnOff( int pinNumber) {
  digitalWrite(pinNumber, LOW);

}

int checkTemp( int pinNumber) {

}

void lcdPrint(float temp, float hum, int lightIntensity){

  
  lcd.print("T:"  );
  lcd.print(temp);
  lcd.print(" H:");
  lcd.print(hum);
  lcd.setCursor(0, 2);
  lcd.print("L.I:");
  lcd.print(lightIntensity);
}
