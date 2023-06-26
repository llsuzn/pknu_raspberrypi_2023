# switch누르면 led켜고 /끄기
import RPi.GPIO as GPIO
import time

red = 27
blue = 17
green = 22
button = 24
i = 0

GPIO.setmode(GPIO.BCM)      # GPIO mode
GPIO.setwarnings(False)     # 경고 없애기

def switchin(channel):
    global i 
    i = i + 1
    if i%2==0:
        GPIO.output(red,True)
        GPIO.output(green,True)
        GPIO.output(blue,True)
    else:
        GPIO.output(red,False)
        GPIO.output(green,False)
        GPIO.output(blue,False)
    

GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button,GPIO.RISING,callback=switchin)

while 1:
    time.sleep(1);