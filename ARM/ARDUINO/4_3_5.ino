#include<Servo.h>

Servo bottom, arm1, arm2, arm3;
Servo servo[4] = {bottom, arm1, arm2, arm3};

int pin[4] = {12,13,16,17};
int pre_angle[4] = {90,90,90,90}; 
int servoSpeed = 20;

void setup() {
  for(int i=0; i<4; i++){
    servo[i].attach(pin[i]);
  }
  Serial.begin(9600);
}

void loop() {
  int motorAngle[4]={30,30,30,30};
  while(!servoParallelControl(motorAngle[0],bottom,servoSpeed));
  while(!servoParallelControl(motorAngle[1],arm1,servoSpeed));
  while(!servoParallelControl(motorAngle[2],arm2,servoSpeed));
  while(!servoParallelControl(motorAngle[3],arm3,servoSpeed));
  while(!servoParallelControl(180-motorAngle[0],bottom,servoSpeed));
  while(!servoParallelControl(180-motorAngle[1],arm1,servoSpeed));
  while(!servoParallelControl(180-motorAngle[2],arm2,servoSpeed));
  while(!servoParallelControl(180-motorAngle[3],arm3,servoSpeed));
  while(1);
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
