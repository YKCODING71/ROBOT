#include <Servo.h>
 
Servo myservo;
int increase = 1;
int min_angle = 15;
int max_angle = 165;
int pos = min_angle;
 
int TrigPin = 12;
int EchoPin = 13;
 
void setup(){
  Serial.begin(9600);
  myservo.attach(10);
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
}
 
void loop(){
  myservo.write(pos);
  Serial.print(pos);
  Serial.print(",");
  Serial.print(distance());
  Serial.print(".");
 
  pos += increase;
  if(pos <= min_angle || pos >= max_angle)
    increase *= -1;
 
  delay(30);
}
 
unsigned long distance(){
  unsigned long d;
   
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
   
  d = pulseIn(EchoPin, HIGH)/58.2;      //또는 *0.034/2
   
  return d;
}
