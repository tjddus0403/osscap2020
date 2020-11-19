import RPi.GPIO as GPIO
import time

list =[261,294,329,349,393,440,493,523]
num =[2,2,2,2,2,2,2,4,0,1,2,3,3,3,3,3,2,2,2,2,1,1,0,1,4,2,2,2,2,2,2,2,4,0,1,2,3,3,3,3,3,2,2,2,4,4,3,2,0]
buzzer_pin= 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)



try: 
    pwm= GPIO.PWM(buzzer_pin,100);
    pwm.start(100)
    pwm.ChangeDutyCycle(90)
                    
    for i in range(80):
        pwm.ChangeFrequency(list[num[i]])
        time.sleep(0.3)
                                                
except KeyboardInterrupt: 
        PWM.stop()
        GPIO.cleanup()

            
