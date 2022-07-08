#include <Keyboard.h>
#define buttonGND A2
#define buttonPin A0

bool buttonCheck(int pin){
    return !digitalRead(pin);
}

void mainloop(){
      <DUCKY_SCRIPT_THERE>
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