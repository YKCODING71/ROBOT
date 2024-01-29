#define LED_RED 5
#define LED_GREEN 6
#define LED_BLUE  11

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    String strRead = Serial.readStringUntil('\n');
    if(strRead.indexOf("RGB=") != -1)
    {
      int commaIndex1 = strRead.indexOf(","); //7(위치)
      int commaIndex2 = strRead.indexOf(",",commaIndex1 + 1); //11(위치)
      int redValue = strRead.substring(4,commaIndex1).toInt();
      int greenValue = strRead.substring(commaIndex1 + 1,commaIndex2).toInt();
      int blueValue = strRead.substring(commaIndex2 + 1,strRead.length()).toInt();
      redLedSet(redValue,greenValue,blueValue);
      Serial.println("OKRGB");
    }
  }
}

void redLedSet(int red, int green, int blue)
{
  analogWrite(LED_RED,red);
  analogWrite(LED_GREEN,green);
  analogWrite(LED_BLUE,blue);
}
//4_2_4.ino
