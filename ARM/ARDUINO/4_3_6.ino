#include<Servo.h>

int servoParallelControl (int thePos, Servo theServo, int speed);

Servo bottom,arm1,arm2,arm3;

void setup(){
  Serial.begin(9600);
  delay(1000);
#define SERVOS_PER_TIMER       10000
 
  bottom.attach(12);
  arm1.attach(13);
  arm2.attach(16);
  arm3.attach(17);
#define SERVOS_PER_TIMER       12  
  
  Serial.println(bottom.read());
  Serial.println(arm1.read());
  Serial.println(arm2.read());
  Serial.println(arm3.read());
  delay(1000);
}

void loop(){
  while(!servoParallelControl(30,arm1,50));
  while(!servoParallelControl(150,arm1,50));
  while(!servoParallelControl(30,arm2,50));
  while(!servoParallelControl(150,arm2,50));
  while(!servoParallelControl(30,arm3,50));
  while(!servoParallelControl(150,arm3,50));
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
      Serial.println(theServo.read());
      return 1;
    }  
}
