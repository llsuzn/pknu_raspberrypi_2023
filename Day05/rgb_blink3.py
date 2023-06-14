# rgb led 컨트롤 / push Button 예제
# R : p17 , G : p27 , B : p22
 
import RPi.GPIO as GPIO
import time

red = 27
blue = 17
green = 22
button = 24
i = 0

def clickHandler(channel):
    global i
    i = i + 1
    print(i)
    if i%3==0:    
        GPIO.output(red,True)
        GPIO.output(green,False)
        GPIO.output(blue,True)
    elif i%3==1:
        GPIO.output(red,True)
        GPIO.output(blue,False)
        GPIO.output(green,True)
    elif i%3==2:
        GPIO.output(green,True)
        GPIO.output(red,False)
        GPIO.output(blue,True)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button,GPIO.RISING,callback=clickHandler)

while 1:
    time.sleep(1)