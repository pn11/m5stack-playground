'''無線LANに接続し、NTP で時刻同期する。
無線LANはつながらないことがあるので運ゲー。連続して try しても失敗するので、sleep(1)とかしてやると良い？
NTP は JST にするとなぜかずれるので CST にしてる。
'''
import network
import time
from m5stack import lcd
from m5ui import *
import sys

print('start')

NTRIAL = 100

ssid = 'YOUR (E)SSID'
password = 'YOUR PASSWORD'

#wlan = network.WLAN(network.STA_IF)
wlan = network.WLAN()

lcd.clear()
lcd.println('Started.')

lcd.print('Activating Wi-Fi')
if not wlan.active():
    for _ in range(NTRIAL):
        wlan.active(True)
        if wlan.active():
            break
        lcd.print('.')
        time.sleep(0.1)

if not wlan.active():
    sys.exit()

lcd.clear()

lcd.print('Connecting to:' +str(ssid))
if not wlan.isconnected():
    for _ in range(NTRIAL):
        wlan.connect(ssid, password)
        if wlan.isconnected():
            lcd.println('Connected.')
            lcd.println(wlan.ifconfig())
            break
        lcd.print('.')
        time.sleep(1.0)

lcd.clear()
lcd.setCursor(0, 0)
lcd.println(wlan.isconnected())

print('Connected = ', wlan.isconnected())

if not wlan.isconnected():
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print('Wi-Fi connection failed.')
    sys.exit()

import machine
import utime

rtc = machine.RTC()

lcd.print('Synchronizing with NTP server.')
for _ in range(NTRIAL):
    #rtc.ntp_sync(server="ntp.nict.jp", tz="tz='JST-9'")
    rtc.ntp_sync(server="ntp.nict.jp", tz="tz='CST-8'")
    if rtc.synced():
        break
    time.sleep(0.5)
    lcd.print('.')

if not rtc.synced():
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print('Sync failed.')
    sys.exit()


lcd.clear()
lcd.setCursor(0, 0)
lcd.println(utime.gmtime())
lcd.println(utime.localtime())

time.sleep(0.5)

lcd.clear()
lcd.setCursor(0, 0)

label_date = M5TextBox(100, 90, "Text", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label_time = M5TextBox(100, 120, "Text", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)


while True:
    year, month, day, hour, minute, sec, _, _ = utime.localtime()
    datestr='{:04d}/{:02d}/{:02d}'.format(year, month, day)
    timestr='{:02d}:{:02d}:{:02d}'.format(hour, minute, sec)
    label_date.setText(datestr)
    label_time.setText(timestr)
    time.sleep(0.1)
