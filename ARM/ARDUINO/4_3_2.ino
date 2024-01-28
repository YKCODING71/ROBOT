#include <Servo.h>
#define SERVO_PIN 12

Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("SERVO=") != -1)
    {
      int servoDigree = strRead.substring(6,strRead.length()).toInt();
      
      if(servoDigree <= 180)
      {
        myservo.write(servoDigree);
        Serial.println("OKSERVO");
      }
      else Serial.println("error digree");
    }
  }
}
//4_3_2.ino
