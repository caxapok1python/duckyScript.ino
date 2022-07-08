#include <Keyboard.h>
#define buttonGND A2
#define buttonPin A0

bool buttonCheck(int pin){
    return !digitalRead(pin);
}

void mainloop(){
      
    // ----Title: Hello World ducky script
    // ----Description: This is a simple of ducky script that opens notepad and prints "Hello World".
    // ----Author: caxapok
    // ----Date: 08-07-2022
    // ----Version: 1.0
    // ----Instructions:
    // ----1. Open notepad.
    Keyboard.press(KEY_LEFT_GUI);
    Keyboard.press(r);
    delay(100);
    Keyboard.releaseAll();
    delay(250);
    Keyboard.print("notepad");
    delay(250);
    Keyboard.press(KEY_RETURN);
    delay(100);
    Keyboard.releaseAll();
    delay(250);
    // ----2. Print "Hello World" in the notepad.
    Keyboard.print("Hello World");
    delay(250);
    Keyboard.press(KEY_RETURN);
    delay(100);
    Keyboard.releaseAll();
    delay(250);
}

void setup() {
  Keyboard.begin();

  pinMode(buttonGND, OUTPUT);
  digitalWrite(buttonGND, LOW);

  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  while (!buttonCheck(buttonPin)){
    delay(50);
  }
  mainloop();
}