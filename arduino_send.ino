#include <SoftwareSerial.h>
char a = 'a';

void setup()
{
	Serial.begin(9600);
}

void loop()                     
{
	Serial.println(a);
	a++;
	delay(1000);
}