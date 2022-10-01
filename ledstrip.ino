#include <Adafruit_NeoPixel.h>

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1:
#define LED_PIN    6

// How many NeoPixels are attached to the Arduino?
#define LED_COUNT 30

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
// Argument 1 = Number of pixels in NeoPixel strip
// Argument 2 = Arduino pin number (most are valid)
// Argument 3 = Pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
char userInput;
char incomingByte;
uint32_t color = strip.Color(0, 150, 0);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  strip.begin();
}

void loop() {
  strip.clear();
  Serial.println("sup1" + String(color));
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
    //strip.setPixelColor(i, color);
    // strip.fill(color, 1, 30);
    // strip.show();   // Send the updated pixel colors to the hardware.
      }
  }
  
