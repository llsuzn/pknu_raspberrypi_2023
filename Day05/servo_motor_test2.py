# 서보모터 테스트
import RPi.GPIO as GPIO
import time

pwm_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin,GPIO.OUT)
pwm = GPIO.PWM(pwm_pin,50)
pwm.start(3.0)

for i in range(0,3):
    for high in range(30,200):
        pwm.ChangeDutyCycle(high/10.0)
        print(f'각도 :{((high/10.0)-3)*10}')
        time.sleep(0.02)

    for low in range(200,30,-1):
        pwm.ChangeDutyCycle(low/10.0)
        print(f'각도 :{((low/10.0)-3)*10}')
        time.sleep(0.02)

pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()