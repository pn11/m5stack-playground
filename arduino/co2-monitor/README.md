# M5Stack CO2 monitor (Arduino / Platform IO)

## ソースコード参照元

- [M5Stack + MH-Z19B でCO2モニタ作成(ソースコードあり) | Violet Mist](https://swada.net/monitoring-co2-by-mhz19b/)  
  MH-Z19 の読み取りとグラフ作成。
- [DHT12 by Rob Tillaart · Libraries · PlatformIO](https://platformio.org/lib/show/5554/DHT12)  
  DHT12 の読み方の例をそのまま利用した。
- [M5Stack Core2にSWITCHSCIENCE BME280モジュールをGrove端子に接続して温度/湿度/気圧の測定をしてみる。](https://ak1211.com/7702/)
  - 最初参考にしたけど M5Stack Core2 で新しかったので動かなかった。LovyanGFX の使い方は参考になった。
- [M5-ProductExampleCodes/ENV.ino at master · m5stack/M5-ProductExampleCodes](https://github.com/m5stack/M5-ProductExampleCodes/blob/master/Core/m5go/m5go_lite/Arduino/ENV/ENV.ino)

## 使用ライブラリ

- [WifWaf/MH-Z19: For Arduino Boards (&ESP32). Additional Examples/Commands., Hardware/Software Serial](https://github.com/WifWaf/MH-Z19)
  - Platform IO では → [MH-Z19 by Jonathan Dempsey · Libraries · PlatformIO](https://platformio.org/lib/show/6091/MH-Z19)
- [xreef/DHT12_sensor_library: DHT12 complete library](https://github.com/xreef/DHT12_sensor_library)
  - Platform IO では → [DHT12 sensor library by Renzo Mischianti · Libraries · PlatformIO](https://platformio.org/lib/show/11158/DHT12%20sensor%20library)
- [adafruit/Adafruit_BMP280_Library: Arduino Library for BMP280 sensors](https://github.com/adafruit/Adafruit_BMP280_Library)  
  BMP280 と BME280 でややこしいけど、使っている M5Stack の ENV ver.1 は BMP280 っぽい。
  - Platform IO では → - [Adafruit BMP280 Library by Adafruit · Libraries · PlatformIO](https://platformio.org/lib/show/528/Adafruit%20BMP280%20Library)
