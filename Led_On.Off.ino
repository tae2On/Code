int led = 8;


void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);
  
}

void loop() {
  digitalWrite (led, HIGH);
  delay (1000) ;
  digitalWrite ( led, LOW);
  delay (1000) ;

}
