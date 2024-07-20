#include <LiquidCrystal.h> // Include the library for LCD

int Contrast=75;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; // Pin configuration for LCD
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600); // Start serial communication
  analogWrite(6, Contrast);
    lcd.begin(16, 2); // Initialize the LCD (16 columns and 2 rows)
    lcd.setCursor(0, 0);
    lcd.print("Ready"); // Display initial message
    Serial.println("LCD initialized and ready."); // Debugging message
}

void loop() {
  if (Serial.available() > 0) {
    int number = Serial.parseInt(); // Read the number from serial input
    lcd.clear(); // Clear the previous message
    lcd.print("Number: "); // Display label
    lcd.print(number); // Display the number
    Serial.print("Received number: "); // Debugging message
    Serial.println(number); // Debugging message
  }
}


/*#include <LiquidCrystal.h> 
int Contrast=75;
 LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 

 void setup()
 {
    analogWrite(6,Contrast);
     lcd.begin(16, 2);
 } 
     void loop()
 {
   
     lcd.setCursor(0, 0);
     lcd.print("HELLO WORLD!");
   
    lcd.setCursor(0, 1);
     lcd.print("SUBSCRIBE :]");

   /*lcd.scrollDisplayLeft();
   delay(400);
   

   
}*/
