#include <SoftwareSerial.h>

#define IN1 5
#define IN2 6
#define IN3 9
#define IN4 10
#define ENCODER_A 3
#define ENCODER_B 2

#define DIAMETER      65.0
#define CIRCUMFERENCE (DIAMETER * PI) //원둘레(지름*3.14)


#define RESOLUTION 20.0

volatile int encoderA = 0;
volatile int encoderB = 0;
void drive(int pwmA, int pwmB);
void move(int distance, int pwm = 150);


SoftwareSerial mySerial(RX, TX);

void setup() {
  Serial.begin(115200);
  mySerial.begin(57600);
  
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(ENCODER_A, INPUT_PULLUP);
  pinMode(ENCODER_B, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(ENCODER_A), ISR_encoderA, FALLING);
  attachInterrupt(digitalPinToInterrupt(ENCODER_B), ISR_encoderB, FALLING);
}

float Kp = 0.0;

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'G' || command == 'g') {
      int distance = Serial.parseInt();
      int pwm = Serial.parseInt();
      move(distance, pwm);
    } 
    else if (command = 'S' || command == 's') {
      Kp = Serial.parseFloat();
      Serial.print("set Kp = ");
      Serial.println(Kp);
    }
  }
}


void ISR_encoderA() {
  encoderA++;
}

void ISR_encoderB() {
  encoderB++;
}

void drive(int pwmA, int pwmB) {
  if (pwmA > 0) {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
  } else if (pwmA < 0) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
  }

  if (pwmB > 0) {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
  } else if (pwmB < 0) {
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
  } else {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
  }

  analogWrite(ENA, abs(pwmA));
  analogWrite(ENB, abs(pwmB));
}

int ticksForDistance(int distance) {
  return (int)(distance * RESOLUTION / CIRCUMFERENCE);
}

void move(int distance, int pwm) {
  int ticksToMove = ticksForDistance(distance);

  noInterrupts();
  encoderA = 0;
  encoderB = 0;
  interrupts();

  mySerial.print("Running ");
  mySerial.print(distance);
  mySerial.print(" with PWM = ");
  mySerial.println(pwm);
  mySerial.print(" and Kp = ");
  mySerial.print(Kp);
  
  while (encoderB <= ticksToMove) {
    int error = encoderB - encoderA;
    int pwmB = pwm;
    int pwmA = (int)(pwmB + Kp * error);

    mySerial.print(error);
    mySerial.print(", ");
    mySerial.print(pwmA);
    mySerial.print(", ");
    mySerial.println(pwmB);
    
    drive(pwmA, pwmB);
    delay(200);
  }
  drive(0, 0);
}
