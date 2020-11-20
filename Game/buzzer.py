import RPi.GPIO as GPIO
import time

list=[261,294,329,349,393,440,493,523]
num=[0,1,2,3,4,5,6,7]
buzzer_pin=17
GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)
try:
    pwm=GPIO.PWM(buzzer_pin,100);
    pwm.start(100)
    pwm.ChangeDutyCycle(90)
    for i in range(80):
        pwm.ChangeFrequency(list[num[i]])
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
