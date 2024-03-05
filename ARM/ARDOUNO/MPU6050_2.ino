#include <Wire.h>
#include <MPU6050_tockn.h>

MPU6050 mpu6050(Wire);

const int numReadings = 10;
int readings[numReadings];  // 저장할 가속도 값의 배열
int readingsIndex = 0;      // 배열 인덱스
int totalReadings = 0;      // 배열 값의 합계

float threshold = 1.0;      // 걸음을 감지하기 위한 임계값
int steps = 0;              // 걸음 수

void setup() {
  Serial.begin(115200);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
}

void loop() {
  mpu6050.update();

  float accMagnitude = sqrt(pow(mpu6050.getAccX(), 2) + pow(mpu6050.getAccY(), 2) + pow(mpu6050.getAccZ(), 2));

  // 가속도 값을 배열에 저장하고 합계 계산
  totalReadings -= readings[readingsIndex];
  readings[readingsIndex] = accMagnitude;
  totalReadings += accMagnitude;
  readingsIndex = (readingsIndex + 1) % numReadings;

  // 최근 몇 번의 가속도 평균 계산
  float averageAcc = totalReadings / numReadings;

  // 걸음을 감지하는 조건 확인
  if (accMagnitude > threshold * averageAcc) {
    steps++;
    Serial.print("Step Count: ");
    Serial.println(steps);
    delay(500);  // 임계값을 충족할 때 한 번만 측정하도록 지연
  }
}
