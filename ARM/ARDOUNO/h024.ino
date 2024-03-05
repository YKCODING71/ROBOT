#define MOTOR_SP  100
#define INTERVAL  1000
int A_IA = 10;
int A_IB = 9;
int B_IA = 6;   
int B_IB = 5;
int A_ENCODER = 2;

volatile int A_cnt = 0;
int A_speed=0;
unsigned long oldTime = 0;
unsigned long newTime = 0;

void A_ISR(){
  A_cnt++;
}

void setup() {
  Serial.begin(115200);
  pinMode(A_ENCODER,INPUT_PULLUP);
  attachInterrupt(INT0,A_ISR,FALLING);
}

void loop() {
  if (Serial.available()>0){
    char c = Serial.read();
    if(c=='f') A_speed = MOTOR_SP;
    
    else if(c=='s')A_speed = 0;
  }  
  
  newTime = millis();
  if(newTime-oldTime > INTERVAL){
    oldTime = newTime;
    noInterrupts();
    Serial.print("cnt : ");
    Serial.println(A_cnt);
    A_cnt = 0;
    analogWrite(A_IA,A_speed);
    analogWrite(A_IB,0);
    interrupts();
  }
 }
