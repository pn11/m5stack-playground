'''lcd モジュールの挙動を理解したかった。
lcd.setColor() したあとは lcd.clear() しないと背景色は切り替わらない。
lcd.print() などしたあと次にどこに出力されるかは、 lcd.getCursor() で分かる。
これは lcd.clear() しても reset されるわけではないので、したい場合は lcd.setCuror() する。
lcd.LASTX とかは何に使うのか不明。
'''
import time
from m5stack import lcd
import sys
import random

print(lcd.LASTX, lcd.LASTY)

colors = [lcd.BLACK, lcd.NAVY, lcd.DARKGREEN, lcd.DARKCYAN, lcd.MAROON, lcd.PURPLE, lcd.OLIVE, lcd.LIGHTGREY, lcd.DARKGREY, lcd.BLUE, lcd.GREEN, lcd.CYAN, lcd.RED, lcd.MAGENTA, lcd.YELLOW, lcd.WHITE, lcd.ORANGE, lcd.GREENYELLOW, lcd.PINK]

screen_x, screen_y = lcd.screensize()

ys = []
for i in range(100):
    cur_x, cur_y = lcd.getCursor()
    print(cur_x, cur_y, screen_x, screen_y)
    if cur_x > screen_x-10 and cur_y > screen_y -10:
        lcd.setCursor(0, 0)
    lcd.setColor(random.choice(colors), random.choice(colors))
    lcd.clear()
    lcd.print('test', color=random.choice(colors))
    time.sleep(0.05)

print('test')
print(dir(lcd))
print(lcd.LASTX)
print(lcd.LASTY)
print(lcd.text_x)
print(lcd.text_y)
print(lcd.getCursor())
print(lcd.screensize())
#print(lcd.init())
print(ys)
