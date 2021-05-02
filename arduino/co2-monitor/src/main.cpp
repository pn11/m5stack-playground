#include <M5Stack.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <MHZ19.h>
#include <Wire.h> 
#include <DHT12.h>

//#define LGFX_M5STACK
#include <LovyanGFX.hpp>
static LGFX lcd;

// Pressure sensor
static const uint8_t BMP280_I2C_ADDRESS = 0x76;
//static const uint8_t BMP280_I2C_ADDRESS = 0x77;
static Adafruit_BMP280 bmp280;

// temperature and humidity sensor
DHT12 dht12(&Wire);

// CO2 sensor
HardwareSerial mySerial(1);
MHZ19 mhz19;

// Serial.println(__FILE__);
// Serial.print("DHT12 LIBRARY VERSION: ");
// Serial.println(DHT12_LIB_VERSION);
// Serial.println();

#define RX_PIN 16
#define TX_PIN 17
#define BAUDRATE 9600

#define DELAY 2000
#define GRAPH_MAX 3000
#define GRAPH_MIN 1
#define GRAPH_X 0
#define GRAPH_Y 100
#define GRAPH_HEIGHT 100
#define GRAPH_WIDTH 320
#define GRAPH_WARN_HEIGHT 132
const unsigned long background_color = 0x000000U;
const unsigned long message_text_color = 0xFFFFFFU;
TFT_eSprite graph = TFT_eSprite(&M5.Lcd);

void setup() {
    M5.begin();
    M5.Power.begin();
    Wire.begin(); // I2Cの初期化
    dht12.begin();
    lcd.init();
    lcd.setFont(&fonts::lgfxJapanGothic_36);
    lcd.setTextSize(0.5);
    lcd.setTextColor(message_text_color, background_color);
    lcd.setBrightness(10);


    while (!bmp280.begin(BMP280_I2C_ADDRESS)){  
      Serial.println("Could not find a valid BMP280 sensor, check wiring!");
      M5.Lcd.println("Could not find a valid BMP280 sensor, check wiring!");
      delay(1000);
    }

    // setup for CO2 sensor
    mySerial.begin(BAUDRATE, SERIAL_8N1, RX_PIN, TX_PIN);
    mhz19.begin(mySerial);
    mhz19.autoCalibration();

    graph.setColorDepth(8);
    graph.createSprite(GRAPH_WIDTH, GRAPH_HEIGHT + 1);
    graph.fillSprite(TFT_BLACK);
    graph.fillRect(0, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(0, 0, 0));
    graph.pushSprite(GRAPH_X, GRAPH_Y);
}


void loop(){
    lcd.setCursor(0, 0);

    int CO2 = mhz19.getCO2();
    float humidity = dht12.readHumidity();
    float temp = dht12.readTemperature();  
    float pressure = bmp280.readPressure() / 100.0;

    lcd.printf("CO2: %d ppm\n", CO2);
    lcd.printf("Temp.: %0.2f °C\n", temp);
    lcd.printf("humidity: %0.2f %%\n", humidity);
    lcd.printf("気圧: %0.2f hPa\n", pressure);

    // CO2 graph
    graph.pushSprite(GRAPH_X, GRAPH_Y);
    graph.scroll(-1, 0);
    if (CO2 < 800){
        graph.fillRect(GRAPH_WIDTH -1, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(0, 200, 0));
    }
    else if (CO2 < 1200){
        graph.fillRect(GRAPH_WIDTH -1, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(152, 152, 0));
    }
    else {
        graph.fillRect(GRAPH_WIDTH -1, 0, GRAPH_WIDTH, GRAPH_WARN_HEIGHT, M5.Lcd.color565(200, 0, 0));
    }
    
    int p = CO2 / (GRAPH_MAX / GRAPH_HEIGHT);
    graph.drawPixel(GRAPH_WIDTH -1, GRAPH_HEIGHT - p, TFT_WHITE);

    delay(DELAY);
}
