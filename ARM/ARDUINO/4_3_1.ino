void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("SERVO=") != -1)
    {
      int servoDigree = strRead.substring(6,strRead.length()).toInt();
      if(servoDigree <= 180)
      {
        Serial.print("SERVO DIGREE:");
        Serial.println(servoDigree);
      }
      else Serial.println("error digree");
    }
  }
}
//4_3_1.ino
