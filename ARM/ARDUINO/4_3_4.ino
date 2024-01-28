#include<Servo.h>

Servo bottom, arm1, arm2, arm3;
Servo servo[4] = {bottom, arm1, arm2, arm3};

int pin[4] = {12,13,16,17};
int pre_angle[4] = {90,90,90,90}; 
int servoSpeed = 30;

void setup() {
  Serial.begin(9600);
  for(int i=0; i<4; i++){
    servo[i].attach(pin[i]);
  }
}

void loop() {
  
  if (Serial.available() > 0){
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("SERVO=") != -1){
      int servoDigree = strRead.substring(7,strRead.length()).toInt();
      
      if(strRead.indexOf('a') != -1) servoParallelControl(servoDigree,bottom,servoSpeed);
      else if(strRead.indexOf('b') != -1) servoParallelControl(servoDigree,arm1,servoSpeed);
      else if(strRead.indexOf('c') != -1) servoParallelControl(servoDigree,arm2,servoSpeed);
      else if(strRead.indexOf('d') != -1) servoParallelControl(servoDigree,arm3,servoSpeed);
      
      if(servoDigree > 180){
        Serial.println("error digree");
        return;
      }
      
      Serial.println(strRead);
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
