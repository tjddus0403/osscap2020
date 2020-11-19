from gpiozero import Buzzer
import RPi.GPIO as GPIO
import time
buzzer=Buzzer(17)
while True:
    for i in [261,294,329,349]:
        buzzer.on()
        time.sleep(1)
        buzzer.off()
        time.sleep(1)
while True:
    buzzer.beep()

