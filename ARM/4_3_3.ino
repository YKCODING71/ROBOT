#include<Servo.h>

Servo bottom, arm1, arm2, arm3;
Servo servo[4] = {bottom, arm1, arm2, arm3};

int pin[4] = {12,13,16,17};
int pre_angle[4] = {90,90,90}; 
int servoSpeed = 5;

void setup() {
  Serial.begin(9600);
  for(int i=0; i<4; i++){
    servo[i].attach(pin[i]);
    servo[i].write(pre_angle[i]);
  }
}

void loop() {
  if (Serial.available() > 0){
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("SERVO=") != -1){
      int servoDigree = strRead.substring(7,strRead.length()).toInt();
      Serial.println(servoDigree);
      
      if(strRead.indexOf('a') != -1) bottom.write(servoDigree);
      else if(strRead.indexOf('b') != -1) arm1.write(servoDigree);   
      else if(strRead.indexOf('c') != -1) arm2.write(servoDigree);   
      else if(strRead.indexOf('d') != -1) arm3.write(servoDigree);   

      if(servoDigree > 180){
        Serial.println("error digree");
        return;
      }
      
      Serial.println(strRead);
      
    }
  }
}
