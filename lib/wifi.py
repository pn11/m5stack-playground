from m5stack import *
from m5ui import *
from uiflow import *
import unit
import network
import json
import time

def connect(ssid, password, num_trial=100):
    wlan = network.WLAN()
    lcd.setCursor(0, 0)
    
    if not wlan.active():
        for _ in range(num_trial):
            wlan.active(True)
            if wlan.active():
                lcd.println('Wi-Fi module is active.')
                break
            lcd.print('.')
            time.sleep(0.1)

    if not wlan.isconnected():
        lcd.println("Connecting to {}".format(ssid))
        for _ in range(num_trial):
            wlan.connect(ssid, password)
            if wlan.isconnected():
                lcd.println('Connected.')
                lcd.println(wlan.ifconfig())
                break
            lcd.print('.')
            time.sleep(1.0)
    time.sleep(0.5)
    lcd.clear()
