from gpiozero import Buzzer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

buzzer = Buzzer(17)
scale=[261,294,329,349,392,440,493,523]
GPIO.setup(buzzer,scale)
p=GPIO.PWM(buzzer,600)
p.start(50)
try:
    for i in range(8):
        p.ChangeFrequency(scale[i])
        time.sleep(0.5)
finally:
    p.stop()
    GPIO.cleanup()
    
#while True:
    #buzzer.on()
    #sleep(1)
    #buzzer.off()
    #sleep(1)
#while True:
    #buzzer.beep()

