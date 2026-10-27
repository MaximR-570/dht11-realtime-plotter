#include <DHT.h>

DHT dht(2, DHT11);

void setup() {

  Serial.begin(9600);
  dht.begin();

}

void loop() {

  float t = dht.readTemperature();
  float h = dht.readHumidity();
  //Serial.println("Temperatur: ");
  Serial.print(t);
  Serial.print(",");
  Serial.println(h);
  // Serial.println("°C");
  delay(1000);
// Wenn hier der delay geändert wird, muss er im python Skript auch geändert werden
}
