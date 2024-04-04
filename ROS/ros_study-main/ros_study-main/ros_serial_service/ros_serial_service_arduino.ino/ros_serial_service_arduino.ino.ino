void setup() {
    Serial.begin(115200);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT); 
    pinMode(13, OUTPUT); 
}void loop() {
    if(Serial.available()>0){
        char a = Serial.read();
        if(a == 'a'){
            digitalWrite(2, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(13, HIGH);
        }else if(a == 'b'){
            digitalWrite(2, LOW);
            digitalWrite(3, LOW);
            digitalWrite(13, LOW);
        }
    }
}
