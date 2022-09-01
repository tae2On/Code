
int ENB = 10;
int Ina3 = 8;
int Ina4 = 9;

void setup() {
  Serial. begin ( 9600);
  pinMode (ENB, OUTPUT);
  pinMode (Ina3, OUTPUT);
  pinMode (Ina4, OUTPUT);
}

void loop() {
  int val = Serial.parseInt();

  
    digitalWrite (Ina3, HIGH);
    digitalWrite (Ina4, LOW);
    analogWrite (ENB, val);
}
