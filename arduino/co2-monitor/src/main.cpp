#include <M5Stack.h>
#include "MHZ19.h"                                        

#define RX_PIN 16
#define TX_PIN 17
#define BAUDRATE 9600

#define DELAY 2000
#define GRAPH_MAX 3000
#define GRAPH_MIN 1
#define GRAPH_X 0
#define GRAPH_Y 40
#define GRAPH_HEIGHT 200
#define GRAPH_WIDTH 320
#define GRAPH_WARN_HEIGHT 132

MHZ19 myMHZ19;
HardwareSerial mySerial(1);
TFT_eSprite graph = TFT_eSprite(&M5.Lcd);

void setup(){
    M5.begin();
    M5.Lcd.setTextSize(3);
    Serial.begin(9600);

    mySerial.begin(BAUDRATE, SERIAL_8N1, RX_PIN, TX_PIN);
    myMHZ19.begin(mySerial);
    myMHZ19.autoCalibration();

    graph.setColorDepth(8);
    graph.createSprite(GRAPH_WIDTH, GRAPH_HEIGHT + 1);
    graph.fillSprite(TFT_BLACK);
    graph.fillRect(0, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(152, 152, 0));
    graph.pushSprite(GRAPH_X, GRAPH_Y);
}

void loop(){
    M5.Lcd.setCursor(0, 0);

    int CO2 = myMHZ19.getCO2();
    M5.Lcd.print("CO2: ");
    M5.Lcd.print(CO2);
    M5.Lcd.println("ppm ");

    graph.pushSprite(GRAPH_X, GRAPH_Y);
    graph.scroll(-1, 0);
    graph.fillRect(GRAPH_WIDTH -1, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(152, 152, 0));
    int p = CO2 / (GRAPH_MAX / GRAPH_HEIGHT);
    graph.drawPixel(GRAPH_WIDTH -1, GRAPH_HEIGHT - p, TFT_WHITE);

    delay(DELAY);
}