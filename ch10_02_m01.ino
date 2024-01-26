#include <Servo.h>

#define MIN 100
#define MAX 1000
#define REF 512
#define SW 2

Servo myservo;

void setup(){
 Serial.begin(9600); 
 pinMode(SW, INPUT_PULLUP); 
 myservo.attach(9);
}

void loop(){
  int x = analogRead(A0);
  int y = analogRead(A1);
  int s = digitalRead(SW);
  Serial.print(x);
  Serial.print('\t');
  Serial.print(y);
  Serial.print('\t');
  Serial.println(s);

  if(x >= MAX) myservo.write(180);
  else if(x <= MIN) myservo.write(0);
  delay(100);
}
