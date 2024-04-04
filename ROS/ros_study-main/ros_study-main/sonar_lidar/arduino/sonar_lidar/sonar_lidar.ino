#include "Adafruit_VL53L0X.h"
#include <Servo.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();
Servo sv;

uint8_t uga[100] ={0,};


void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  sv.attach(2);
  sv.write(0);
  uga[99] = '\n';
  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }
  
  //Serial.println("Adafruit VL53L0X test");
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  // power 
  Serial.println(F("VL53L0X API Simple Ranging example\n\n")); 
}


void loop() {
  for(int i=0;i<99;i++){
    VL53L0X_RangingMeasurementData_t measure;
    sv.write(i); 
    //Serial.print("Reading a measurement... ");
    lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
    if (measure.RangeStatus != 4) {  // phase failures have incorrect data
      //Serial.println(measure.RangeMilliMeter);
      uga[i] = (uint8_t)measure.RangeMilliMeter;
    }
  }
  Serial.write(uga, 100);
  delay(100);
}
