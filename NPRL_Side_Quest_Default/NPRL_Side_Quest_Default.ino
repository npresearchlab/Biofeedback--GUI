/*
 Example using the SparkFun HX711 breakout board with a scale
 By: Nathan Seidle
 SparkFun Electronics
 Date: November 19th, 2014
 License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).
  Modified by; Hyungjun Park
  Date: 8/25/2022
  
 This example demonstrates basic scale output. See the calibration sketch to get the calibration_factor for your
 specific load cell setup.

 This example code uses bogde's excellent library:"https://github.com/bogde/HX711"
 bogde's library is released under a GNU GENERAL PUBLIC LICENSE

 The HX711 does one thing well: read load cells. The breakout board is compatible with any wheat-stone bridge
 based load cell which should allow a user to measure everything from a few grams to tens of tons.
 Arduino pin 2 -> HX711 CLK
 3 -> DAT
 5V -> VCC
 GND -> GND

 The HX711 board can be powered from 2.7V to 5V so the Arduino 5V power should be fine.

*/

#include "HX711.h"
#include <Adafruit_NeoPixel.h>

#define LED_PIN    6

#define LED_COUNT 30

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
#define calibration_factor -100000.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2

HX711 scale;
char userInput;
uint32_t color = strip.Color(0, 150, 0);
void setup() {
  Serial.begin(112500);
  // Serial.println("HX711 scale demo");
  strip.begin();
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0

  // Serial.println("Readings:");
}

void loop() {
  Serial.println(abs(scale.get_units())); // units in kg
  // Serial.println(abs(scale.get_units()/22.0462)); //we divide by 22.0462 as the physical load cell is rated for 10 kg of force detection- allows us to output a precentage directly to python
  strip.clear();
  // put your main code here, to run repeatedly:
   userInput = Serial.read();               // read user input
      if(userInput == 'o'){                
        color = strip.Color(255, 0, 255);
        strip.fill(color, 0, 30);
    strip.show();
      }
      if(userInput == 'x'){
        color = strip.Color(0, 150, 0);
        strip.fill(color, 0, 30);
    strip.show();
      }
      if(userInput == 'z'){
        color = strip.Color(27, 49, 247);
        strip.fill(color, 0, 30);
    strip.show();
      }
      if(userInput == 'v'){
        color = strip.Color(242, 21, 10);
        strip.fill(color, 0, 30);
    strip.show();
      }
      if(userInput == 'c'){
        for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256) {
    for(int i=0; i<strip.numPixels(); i++) { 
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show();
      }
      }
}