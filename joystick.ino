// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  pinMode(25, INPUT); //button
  digitalWrite(25, HIGH);
}

int past = -1;
void loop() {
  // read the input on analog pin GPIO36:
  // this is opposite of the pins on the joystick because we rotate the joystick 
  int y = analogRead(27);
  int x = analogRead(26);
  int button = analogRead(25);

  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  if (!button){
    Serial.print(1);
  } else {
    Serial.print(0);
  }
  
  Serial.print("\n");
  delay(40);

}

      