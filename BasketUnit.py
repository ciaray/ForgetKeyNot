#include <SoftwareSerial.h>
#include <RCSwitch.h>
RCSwitch mySwitch = RCSwitch();
SoftwareSerial rfid(7, 8);
void parse(void);
void seek(void);
int flag = 0;
int Str1[11];

void setup()
{
  Serial.begin(9600);
  Serial.println("Start");
  rfid.begin(19200);
  pinMode(2, OUTPUT);
  mySwitch.enableTransmit(5);
  delay(10);
}

void loop()
{
  digitalWrite(2, HIGH);
  seek();
  parse();
  if(Str1[2] == 6){
    flag = 1;
  }
  if(Str1[2] == 2){
    flag = 0;
  }
  Serial.print(flag);
  mySwitch.send(flag, 24);
  delay(100);
}

void parse()
{
  while(rfid.available()){
    if(rfid.read() == 255){
      for(int i=1;i<11;i++){
        Str1[i]= rfid.read();
      }
    }
