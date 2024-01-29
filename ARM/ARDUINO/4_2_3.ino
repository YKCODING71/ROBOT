void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("RGB=") != -1)
    {
      int commaIndex1 = strRead.indexOf(",");
      int commaIndex2 = strRead.indexOf(",",commaIndex1 + 1);

      int redValue = strRead.substring(4,commaIndex1).toInt();
      int greenValue = strRead.substring(commaIndex1 + 1,commaIndex2).toInt();
      int blueValue = strRead.substring(commaIndex2 + 1,strRead.length()).toInt();

      Serial.println(commaIndex1);
      Serial.println(commaIndex2);
      Serial.println(commaIndex1+1);
      Serial.println(commaIndex2+1);
      Serial.println(strRead.length());
      
      Serial.print("red:"); Serial.println(redValue);
      Serial.print("green:"); Serial.println(greenValue);
      Serial.print("blue:"); Serial.println(blueValue);
    }
  }
}
//4_2_3.ino
