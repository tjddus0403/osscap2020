import RPi.GPIO as GPIO
import time

list=[261.6256,293.6648,329.6276,349.2282,391.9954,440,493.8833,523.2511]
num=[0,1,2,3,4,5,6,7]
buzzer_pin=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)
try:
    pwm=GPIO.PWM(buzzer_pin,100);
    pwm.start(100)
    pwm.ChangeDutyCycle(90)
    for i in range(len(num)):
        pwm.ChangeFrequency(list[num[i]])
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
