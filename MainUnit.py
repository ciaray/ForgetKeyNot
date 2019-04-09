#include <RCSwitch.h>
#include <PCM.h>

const unsigned char sample[] PROGMEM = {
---------- 8Bit Audio info -------------
 };

int PIR;
int State;
int RF;
RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on interrupt 0 => that is pin #2
  pinMode(8, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
  digitalWrite(3, HIGH); //Power PIR
  PIR = digitalRead(4);
  digitalWrite(8, HIGH); //Power RF
}

void loop() {
  RF = mySwitch.getReceivedValue();
  mySwitch.resetAvailable();
  PIR = digitalRead(4);
  Serial.print("RF = ");
  Serial.println(RF);
  Serial.print("PIR = ");
  Serial.println(PIR);
  Serial.println(" ");
  delay(250);

  if (PIR == 1 && RF ==1){
      Serial.println("Play Audio");
      startPlayback(sample, sizeof(sample));
      delay(10000);
  }
  }
