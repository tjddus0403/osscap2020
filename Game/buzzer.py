import RPi.GPIO as GPIO
import time
       #0       #1            #2      #3       #4       #5      #6       #7        #8       #9         #10      #11     #12   #13     
#list=[261.6256|,293.6648|,329.6276|,349.2282|,391.9954|,440|,493.8833|,523.2511|,587.3295|,659.2551|,698.4565|,783.9909|,880|,987.7666]
#num=[2,4,5,8,8,7,6,5,6,4,6,8,11,11,11,12,10,9,10,5,]

plane=[330, 294, 261, 294, 330, 330, 330, 294, 294, 294,
330, 392, 392]
buzzer_pin=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)
try:
    pwm=GPIO.PWM(buzzer_pin,100);
    pwm.start(100)
    pwm.ChangeDutyCycle(90)
    for i in plane:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
   #for i in range(len(num)):
    #    pwm.ChangeFrequency(list[num[i]])
     #   time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
