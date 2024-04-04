void setup() {
    Serial.begin(115200);
    pinMode(13, OUTPUT); 
}void loop() {
    float temp = random(10, 40);
    Serial.println(temp);
    delay(1000);
}
