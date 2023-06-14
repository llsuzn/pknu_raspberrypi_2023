# rgb led 컨트롤
# R : p17 , G : p27 , B : p22
 
import RPi.GPIO as GPIO
import time

red = 27
blue = 17
green = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
i = 0



try:
    while True:
        # red + green = yellow
        # red + blue = pink
        # green + blue = sky
        if i%3==0:    
            time.sleep(1)
            GPIO.output(red,True)
            GPIO.output(green,False)
            GPIO.output(blue,True)
        elif i%3==1:
            time.sleep(1)
            GPIO.output(red,True)
            GPIO.output(blue,False)
            GPIO.output(green,True)
        elif i%3==2:
            time.sleep(1)
            GPIO.output(green,True)
            GPIO.output(red,False)
            GPIO.output(blue,True)
        i = i+1

        

    
except KeyboardInterrupt:
    GPIO.cleanup()      # 에러발생시 지우기