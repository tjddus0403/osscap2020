
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 17
scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
#도 레 미 파 솔 라 시 도
GPIO.setup(buzzer, GPIO.OUT) # 출력 설정
# 입력 설정
p = GPIO.PWM(buzzer, 100)

list = [0,0,4,4,5,5,4,3,3,2,2,1,1,0] #작은별 노래
try:
    while 1: # 무한 
        p.start(100) # pwm 시작
        p.ChangeDutyCycle(90) # dutycycle 변경
        for i in range(len(list)): #len() => 길이 추출
            p.ChangeFrequency(scale[list[i]]) #주파수 변경
            if (i+1)%7 == 0: # 7번째 음 박자 변경
                time.sleep(1)
            else :
                time.sleep(0.5)
                p.stop() #pwm 종료
except KeyboardInterrupt: #ctrl+c->종료
    GPIO.cleanup()
