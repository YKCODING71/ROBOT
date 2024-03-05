// 서보 모션 간소화 + OLED
#include <Servo.h>
#include <U8x8lib.h>  // U8g2 library 설치할 것

#define PIN1  12
#define PIN2  13
#define PIN3  16
#define PIN4  17
#define SPEED 10


#define SCREEN_WIDTH 128 // 너비(픽셀)
#define SCREEN_HEIGHT 64 // 높이(픽셀)

Servo servoA, servoB, servoC, servoD;
Servo servos[4] = {servoA, servoB, servoC, servoD};
int angleA, angleB, angleC, angleD;
int angles[4] = {0,0,0,0};
String angA_str = "a";
String angB_str = "b";
String angC_str = "c";
String angD_str = "d";
U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);
int cnt =0;
// 모터 이동 속도 줄이기

int servoSlower(int servoNum, int targetAngle, int dragger){
  Servo this_servo = servos[servoNum];
  int curAngle = this_servo.read();
  int newPos = curAngle;
  angles[servoNum] = newPos;

  // 서보 1도씩 전후 가동
  if (curAngle < targetAngle){
    newPos += 1;
    this_servo.write(newPos);
    delay(dragger);
    return 0;
  }
  else if (newPos > targetAngle){
    newPos -= 1;
    this_servo.write(newPos);
    delay(dragger);
    return 0;
  }
  else{     //목표점에 도착하면 1 리턴
    cnt++;
    return 1;
  }
}

// 각도 추출 프로토콜 구현
int extractNumber(String str, char identifier){
  int startIdx = str.indexOf(identifier) + 1; //헤더 다음 위치
  int endIdx = str.indexOf('s', startIdx); // 다음 's' 위치
  String angleStr = str.substring(startIdx, endIdx);
  int angle = angleStr.toInt(); //정수 형변환
  return angle;
}

// OLED 화면 지우기
void clear_oled() {
  u8x8.setFont(u8x8_font_chroma48medium8_r);
  for(int i=0; i<=5; i++){
    u8x8.drawString(0, i, "                   ");
  }
}

void setup() {
  Serial.begin(9600);
  servoA.attach(PIN1); 
  servoB.attach(PIN2); 
  servoC.attach(PIN3);
  servoD.attach(PIN4);
  servoA.write(90);
  servoB.write(90);
  servoC.write(90);
  servoD.write(90);
  angleA =90;
  angleB =90;
  angleC =90;
  angleD =90;
  u8x8.begin();
  clear_oled();
}

int status_ = 0;
int done1 = 0;
int done2 = 0;
int done3 = 0;
int done4 = 0;
void loop() {
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // 한 줄 끝까지 읽기
    inputString.trim(); // 앞뒤 공백 제거
//    Serial.println("fromArdu"+inputString); //a23sb101sc56sd120s
// 함수 호출 전에 extractNumber를 정의해야 함
    angleA = extractNumber(inputString, 'a');
    angleB = extractNumber(inputString, 'b');
    angleC = extractNumber(inputString, 'c');
    angleD = extractNumber(inputString, 'd');
    done1 = 0;done2=0;done3 = 0;done4=0;cnt =0;
    Serial.print(angleA);
    Serial.print('\t');
    Serial.print(angleB);
    Serial.print('\t');
    Serial.print(angleC);
    Serial.print('\t');
    Serial.println(angleD);
    
    u8x8.drawString(0, 2,"                   ");
    u8x8.drawString(0, 2,String(angleA).c_str() );
    u8x8.drawString(0, 3,"                   ");
    u8x8.drawString(0, 3,String(angleB).c_str() );
    u8x8.drawString(0, 4,"                   ");
    u8x8.drawString(0, 4,String(angleC).c_str() );
    u8x8.drawString(0, 5,"                   ");
    u8x8.drawString(0, 5,String(angleD).c_str() );
  }
// 로봇암 구동
  if(cnt==0 && !done1 && servoSlower(0, angleA, SPEED)) done1 = 1;
  else if(cnt==1 && !done2 && servoSlower(1, angleB, SPEED)) done2 = 1;
  else if(cnt==2 && !done3 && servoSlower(2, angleC, SPEED)) done3 = 1;
  else if(cnt==3 && !done4 && servoSlower(3, angleD, SPEED)) done4 = 1;
}  
