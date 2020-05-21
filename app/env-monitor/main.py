from m5stack import *
from m5ui import *
from uiflow import *
import unit
import network
import utime
import json
import time

import ambient
import ntptime_custom

setScreenColor(0x000000)
env0 = unit.get(unit.ENV, unit.PORTA)

NTRIAL = 100
wlan = network.WLAN()

with open('settings.json') as f:
    settings = json.load(f)

ssid = settings['ssid']
password = settings['password']
am = ambient.Ambient(settings['ambient channel id'], settings['ambient write key'])

if not wlan.active():
    for _ in range(NTRIAL):
        wlan.active(True)
        if wlan.active():
            break
        lcd.print('.')
        time.sleep(0.1)

if not wlan.isconnected():
    for _ in range(NTRIAL):
        wlan.connect(ssid, password)
        if wlan.isconnected():
            lcd.println('Connected.')
            lcd.println(wlan.ifconfig())
            break
        lcd.print('.')
        time.sleep(1.0)

ntptime_custom.settime(9*60*60) # +09:00:00 for JST
lt = utime.localtime()

circle4 = M5Circle(56, 61, 20, 0xff9900, 0x000000)
circle2 = M5Circle(108, 99, 20, 0xFFFFFF, 0xFFFFFF)
circle0 = M5Circle(137, 98, 32, 0xFFFFFF, 0xFFFFFF)
circle9 = M5Circle(115, 110, 20, 0xFFFFFF, 0xFFFFFF)
circle3 = M5Circle(88, 111, 20, 0xFFFFFF, 0xFFFFFF)
label_time = M5TextBox(0, 0, "{}/{}/{} {}:{}:{}".format(*lt), lcd.FONT_Default,0xFFFFFF, rotate=0)
label0 = M5TextBox(217, 104, "T :", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(217, 145, "P :", lcd.FONT_Default,0xFFFFFF, rotate=0)
label2 = M5TextBox(217, 185, "H :", lcd.FONT_Default,0xFFFFFF, rotate=0)
label3 = M5TextBox(257, 104, "Text", lcd.FONT_Default,0xffffff, rotate=0)
label4 = M5TextBox(254, 144, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
label5 = M5TextBox(254, 184, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
rect3 = M5Rect(91, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect4 = M5Rect(112, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect5 = M5Rect(135, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect6 = M5Rect(159, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
circle12 = M5Circle(164, 110, 20, 0xFFFFFF, 0xFFFFFF)

import random

random2 = None
i = None

while True:
  label3.setText(str(env0.temperature))
  label4.setText(str(env0.pressure))
  label5.setText(str(env0.humidity))
  lt = utime.localtime()
  label_time.setText("{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(*lt))
  r = am.send({'d1': env0.temperature, 'd2': env0.pressure, 'd3': env0.humidity})
  r.close()
  wait(1.0)
  if (env0.humidity) >= 50:
    circle4.setBgColor(0x000000)
    rgb.setColorAll(0x000099)
    rect3.setBorderColor(0x3333ff)
    rect4.setBorderColor(0x3333ff)
    rect5.setBorderColor(0x3333ff)
    rect6.setBorderColor(0x3333ff)
    random2 = random.randint(2, 50)
    rect3.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect4.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect5.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect6.setSize(height=random2)
  else:
    rect3.setBorderColor(0x000000)
    rect4.setBorderColor(0x000000)
    rect5.setBorderColor(0x000000)
    rect6.setBorderColor(0x000000)
    circle4.setBgColor(0xff6600)
    rgb.setColorAll(0xff6600)
    for i in range(20, 31):
      lcd.circle(56, 61, i, color=0xff9900)
      lcd.circle(56, 61, (i - 1), color=0x000000)
      wait(0.05)
    lcd.circle(56, 61, 30, color=0x000000)
  wait_ms(2)
