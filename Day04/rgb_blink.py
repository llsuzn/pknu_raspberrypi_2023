# rgb led 컨트롤
# R : p17 , G : p27 , B : p22
 
import RPi.GPIO as GPIO
import time

red = 27
green = 4
blue = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

try:
    while True:

        # GPIO.output(red,True)
        # GPIO.output(green,False)
        # GPIO.output(blue,False)
        # time.sleep(1)
        # GPIO.output(red,False)
        # GPIO.output(blue,False)
        # GPIO.output(green,True)
        # time.sleep(1)
        # GPIO.output(green,False)
        # GPIO.output(red,False)
         GPIO.output(blue,True)
        # time.sleep(1)
        
    
except KeyboardInterrupt:
    GPIO.cleanup()      # 에러발생시 지우기