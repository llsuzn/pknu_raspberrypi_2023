# LED 깜빡이기
import RPi.GPIO as GPIO
import time

LED = 18

GPIO.setmode(GPIO.BCM)  # GPIO 18 , GROUND
#GPIO.setmode(GPIO.BOARD) # PINMODE
GPIO.setup(LED,GPIO.OUT)

while (True):
    GPIO.output(LED,True)
    time.sleep(2)
    GPIO.output(LED,False)
    time.sleep(2)
