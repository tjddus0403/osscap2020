from matrix import*
from random import*
from original import*
import random
import time
import RPi.GPIO as GPIO
import copy

def memory_piano():
   arrayBlk=[[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,2,2,2]]
   currBlk=Matrix(arrayBlk)
   QarrayScreen=[
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],  
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

   piano=[261,294,329,349,393,440,493]

   star=[261,261,393,393,440,440,393]

   plane=[329, 294, 261, 294, 329, 329, 329, 294,
          294, 294, 329, 393, 393 ]

   butterfly=[393,329,329,349,294,294]

   schoolbell=[393,393,440,440,393,393,329]
   
   playlist = [star,plane,butterfly,schoolbell]
   i=0
   count=0
   pl=copy.deepcopy(playlist)
   player=input("사용자 이름을 입력하세요 : ")
   buzzer_pin=26
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(buzzer_pin,GPIO.OUT)
   pwm=GPIO.PWM(buzzer_pin,600)
   while True:
         if i==1:
               i=0
               player=input("사용자 이름을 입력하세요 : ")
               pl=copy.deepcopy(playlist)
        
         random.shuffle(pl)
         song=pl[0]
         pl.pop(0)
         for a in song:
               top=2
               left=2
               QiScreen=Matrix(QarrayScreen)
               if a==261:
                     left=2
                                         
               elif a==294:
                     left+=4
                    # pwm.ChangeFrequency(294)
               elif a==329:
                     left+=8
                    # pwm.ChangeFrequency(329)

               elif a==349:
                     left+=12
                    # pwm.ChangeFrequency(349)

               elif a==393:
                     left+=16
                    # pwm.ChangeFrequency(393)

               elif a==440:
                     left+=20
                     #pwm.ChangeFrequency(440)

               elif a==493:
                     left+=24
                    # pwm.ChangeFrequency(493)

               tempBlk=QiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk
               QoScreen = Matrix(QiScreen)
               QoScreen.paste(tempBlk, top, left)
               LED_init()
               draw_matrix(QoScreen); print()
            
               pwm.start(50)
               pwm.ChangeDutyCycle(90)
               pwm.ChangeFrequency(a)
               time.sleep(0.7)
               draw_matrix(QiScreen); print()
                           

                
                     # input
         top=2
         left=2
         answer=[]
         AarrayScreen=[
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],  
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,4,4,4,4,3,3,3,3,7,7,7,7,12,12,12,12,7,7,7,7,3,3,3,3,4,4,4,4,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]
                     #prepare the initial screen output
         AiScreen=Matrix(AarrayScreen)
         AoScreen=Matrix(AiScreen)
         tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
         tempBlk=tempBlk+currBlk
         AoScreen.paste(tempBlk,top,left)
         draw_matrix(AoScreen); print()
         hint=0

         while True:

               print('Direction : q(quit), a(left), d(right)')
               print('Push the piano : p(push)')
               print('Finish : \' \'')
               key=input('Enter a key : ')
               if key=='q':
                     print('Game terminated')
                     break
               elif key=='a':
                     if left==2:
                           continue
                     left-=4
               elif key=='d':
                     if left==26:
                           continue
                     left+=4
               elif key=='p':
                     if left==2:
                           answer.append(261)
                           pwm.ChangeFrequency(261)
                     elif left==6:
                           answer.append(294)
                           pwm.ChangeFrequency(294)
                     elif left==10:
                           answer.append(329)
                           pwm.ChangeFrequency(329)
                     elif left==14:
                           answer.append(349)
                           pwm.ChangeFrequency(349)
                     elif left==18:
                           answer.append(393)
                           pwm.ChangeFrequency(393)
                     elif left==22:
                           answer.append(440)
                           pwm.ChangeFrequency(440)
                     elif left==26:
                           answer.append(493)
                           pwm.ChangeFrequency(493)
                                               
               elif key==' ':
                     break
                                     
               else:
                     print('Wrong key!')
                     continue

               AiScreen=Matrix(AarrayScreen)
                                      
               tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk

               AoScreen = Matrix(AiScreen)
               AoScreen.paste(tempBlk, top, left)
               draw_matrix(AoScreen); print()

         draw_matrix(AiScreen); print()
               
         #input_output_corfirm            
         i = 0
         if song==answer:
               print("성공하셨습니다.")
               count+=1
               if count==3:
                  f=open("피아노 1등.txt",'r')
                  file=f.read()
                  f.close()
                  ls=file.splitlines()
                  for line in ls:
                       print("1등의 기록 : ",line)
                       print(player,"의 기록 : ",count)
                       if int(line)<count:
                           print("축하드립니다. 신기록을 세우셨군요!!")
                           f=open("피아노 1등.txt",'w')
                           line=f.write(str(count))
                           print("새로운 1등 기록 : ",count)
                       elif int(line)==count:
                           print("축하드립니다! 공동 1등 입니다!")
                  i=2    
                  break
               continue
         elif song!=answer:
               print("실패하셨습니다.")
               again=input("게임을 다시 시작하시겠습니까? (Y/N): ")
               f=open("피아노 1등.txt",'r')
               file=f.read()
               f.close()
               ls=file.splitlines()
               for line in ls: 
                   print("1등의 기록 : ",line)
                   line=int(line)
                   draw_matrix(Score(line))
                   time.sleep(2)
                   print(player,"의 기록 : ",count)
                   draw_matrix(Score(count))
                   time.sleep(2)
                   if int(line)<count:
                       print("축하드립니다. 신기록을 세우셨군요!!")
                       f=open("피아노 1등.txt",'w')
                       line=f.write(str(count))
                       print("새로운 1등 기록 : ",line)
                   elif int(line)==count:
                       print("축하드립니다! 공동 1등 입니다!")
               if again=='Y':
                   i=1
                   continue
               elif again=='N':
                   i=2
                   break
