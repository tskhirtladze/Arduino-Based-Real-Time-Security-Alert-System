// პინები LED-ებისთვის
int detectedLED = 13;
int readyLED = 12;
int waitLED = 11;

// ინფუთი მოძრაობის სენსორიდან 
int pirPin = 7;

// პინი Active Buzz-ისთვის
int buzzPin = 8;

// ცვლადი მოძრაობის დეტექტირებისთვის
int motionDetected = 0;

// ცვლადი იმისათვის, რომ ჩაიწეროს მოძრაობის დეტექტირება
int pirValue;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // LED-ების განსაზღვრა, როგორც აუთფუთი
  pinMode(detectedLED, OUTPUT);
  pinMode(readyLED, OUTPUT);
  pinMode(waitLED, OUTPUT);
  pinMode(buzzPin, OUTPUT);

  
  // PIR -ის განსაზღვრა, როგორც ინფუთი
  pinMode(pirPin, INPUT); 

  // სენსორის სტაბილიზაციისათვის განსაზღვრული დრო (6 წმ)
  digitalWrite(detectedLED, LOW);
  digitalWrite(readyLED, LOW);
  digitalWrite(waitLED, HIGH);  
  delay(6000);

  digitalWrite(readyLED, HIGH);  
  digitalWrite(waitLED, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  pirValue = digitalRead(pirPin);

  // მოძრაობის დეტექტირების ნახვა
  if (pirValue == 1){
    // დეტექტირების LED ანთება 3 წამით
    digitalWrite(detectedLED, HIGH);
    motionDetected = 1;
        
    digitalWrite(buzzPin, HIGH);    
    delay(3000);
    Serial.println("The motion is detected ");
    
  } else {
    digitalWrite(detectedLED, LOW);
    digitalWrite(buzzPin, LOW); 
  }

  if (motionDetected == 1){
    // 6 წამის შემდეგ, დეტექტირების ხელახლა განხორციელება
    digitalWrite(detectedLED, LOW);
    digitalWrite(buzzPin, LOW); 
    digitalWrite(readyLED, LOW);
    digitalWrite(waitLED, HIGH);    
    delay(6000);

    digitalWrite(readyLED, HIGH);
    digitalWrite(waitLED, LOW);    
    motionDetected = 0;
  }

}
