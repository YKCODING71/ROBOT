#include <Wire.h>
#include <MPU6050.h>
#include <Tone.h>

MPU6050 mpu;
Tone buzzer;

const int threshold = 5000;  // 충격을 감지하기 위한 임계값
const int buzzerPin = 9;     // 부저가 연결된 핀

int16_t gx, gy, gz;

void setup() {
  Serial.begin(9600);
  mpu.initialize();
  buzzer.begin(buzzerPin);
}

void loop() {
  // MPU6050의 자이로스코프 데이타 읽기
  mpu.getRotation(&gx, &gy, &gz);
  //Serial.println(sqrt(gx^2 + gy^2 + gz^2));

  // 충격 감지 로직
  if (abs(gx) > threshold || abs(gy) > threshold || abs(gz) > threshold) {
    Serial.println("Impact detected!");
    
    // 충격이 감지되면 부저 울리기
    buzzer.play(500, 100);  // 주파수 1000Hz, 지속시간 100ms

    delay(50);  // 중복 감지 방지를 위한 딜레이
  }
}
