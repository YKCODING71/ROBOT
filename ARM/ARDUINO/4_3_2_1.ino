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
        while(!servoParallelControl(servoDigree,myservo,10));
        Serial.println("OKSERVO");
      }
      else Serial.println("error digree");
    }
  }
}

int servoParallelControl (int thePos, Servo theServo, int speed){
    int startPos = theServo.read();      
    int newPos = startPos;   
   
    if (startPos < (thePos)){
       newPos = newPos + 1;               
       theServo.write(newPos);
       delay(speed);
       return 0;                            
    }
    else if (newPos > (thePos)){
      newPos = newPos - 1;
      theServo.write(newPos);
      delay(speed);
      return 0;  
    }  
    else {
      return 1;
    }  
}
