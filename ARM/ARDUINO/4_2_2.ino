void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');

    Serial.print("read:");
    Serial.print(strRead);
  }
}
//4_2_2.ino
