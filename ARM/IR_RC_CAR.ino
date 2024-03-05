int A_IA = 9;
int A_IB = 6;
int B_IA = 3;
int B_IB = 5;
int IR = 10;
int IR2 = 11;

void forward1() {
  analogWrite(B_IA, 0); //
  analogWrite(B_IB, 180);
  analogWrite(A_IA, 180);
  analogWrite(A_IB, 0); //
}

void backward1() {
  analogWrite(B_IA, 150);
  analogWrite(B_IB, 0);
  analogWrite(A_IA, 0);
  analogWrite(A_IB, 150);
}

void turnleft() {
  analogWrite(B_IA, 0);
  analogWrite(B_IB, 180);
  analogWrite(A_IA, 0);
  analogWrite(A_IB, 0);
}

void turnright() {
  analogWrite(B_IA, 0);
  analogWrite(B_IB, 0);
  analogWrite(A_IA, 180);
  analogWrite(A_IB, 0);
}

void stopall() {
  analogWrite(9, 0);
  analogWrite(6, 0);
  analogWrite(3, 0);
  analogWrite(5, 0);
}

void setup() {
  pinMode(A_IA, OUTPUT);
  pinMode(A_IB, OUTPUT);
  pinMode(B_IA, OUTPUT);
  pinMode(B_IB, OUTPUT);
  pinMode(IR, INPUT);
  pinMode(IR2, INPUT);
  Serial.begin(9600);
}

void loop() {

  int IRsensor= digitalRead(IR);
  int IRsensor2= digitalRead(IR2);
  Serial.println(IRsensor);
  Serial.println(IRsensor2);
  if(IRsensor == LOW && IRsensor2 ==LOW) {
    forward1();
  }
  else if(IRsensor == HIGH && IRsensor2 == LOW){
    turnright();
  }
  else if(IRsensor == LOW && IRsensor2 == HIGH){
    turnleft(); 
  }
  else if(IRsensor == HIGH && IRsensor2 == HIGH){
    stopall();
  }
}
