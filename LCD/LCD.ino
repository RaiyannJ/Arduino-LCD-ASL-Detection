#include <LiquidCrystal.h> // Include the library for LCD

int Contrast = 75;

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
    char letter = Serial.read(); // Read the letter from serial input
    if (isAlpha(letter)) { // Check if the received byte is a letter
      lcd.clear(); // Clear the previous message
      lcd.print("Letter: "); // Display label
      lcd.print(letter); // Display the letter
      Serial.print("Received letter: "); // Debugging message
      Serial.println(letter); // Debugging message
    }
  }
}
