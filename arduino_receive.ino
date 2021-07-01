byte character = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
  character = Serial.read();
  Serial.println((char)character);
}
}
