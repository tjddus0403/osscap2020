from matrix import*
from random import*
from original import*
import random
import time
import RPi.GPIO as GPIO
import copy

def memory_piano():
   arrayBlk=[[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,2,2,2]] #사용자가 컨트롤 할 블럭 배열 arrayBlk생성
   currBlk=Matrix(arrayBlk)   #arrayBlk를 행렬형태로 만든 currBlk생성
   QarrayScreen=[                                                                         #문제화면을 보여줄 배열 QarrayScreen 생성
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

   piano=[261,294,329,349,393,440,493]    #도,레,미,파,솔,라,시 의 주파수를 담은 피아노 리스트 생성

   star=[261,261,393,393,440,440,393]     #작은별 노래의 주파수를 담은 리스트 생성
   
   plane=[329, 294, 261, 294, 329, 329, 329, 294,     #비행기 노래의 주파수를 담은 리스트 생성
          294, 294, 329, 393, 393 ]

   butterfly=[393,329,329,349,294,294]    #나비야 노래의 주파수를 담은 리스트 생성

   schoolbell=[393,393,440,440,393,393,329]  #학교종 노래의 주파수를 담은 리스트 생성
   
   playlist = [star,plane,butterfly,schoolbell]    #각 노래를 담은 플레이리스트 리스트 생성
   i=0   #성공, 실패를 판단하기 위한 변수 i 
   count=0  #맞춘 갯수(점수)를 판단하기 위한 변수 count 생성
   pl=copy.deepcopy(playlist)    #playlist를 카피한 리스트 pl 생성
   player=input("사용자 이름을 입력하세요 : ")    #사용자의 이름 입력받기
   buzzer_pin=26     #피에조 부저를 연결한 GPIO 핀 번호 (26), 아래는 피에조부저 소리를 출력하기 위한 과정임
   GPIO.setwarnings(False) 
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(buzzer_pin,GPIO.OUT)
   pwm=GPIO.PWM(buzzer_pin,600)
   while True:
         if i==1:    #i=1이라면 게임을 다시 시작하는 상태이기 때문에 위에서 정한 초기값을 다시 받아야함 아래는 그 과정임
               i=0
               player=input("사용자 이름을 입력하세요 : ")
               pl=copy.deepcopy(playlist)
         random.shuffle(pl)   #pl내용을 랜덤으로 섞기
         song=pl[0]  #p1에 있는 첫번째 곡을 저장한 리스트 변수 song 생성
         pl.pop(0)   #pl에 있는 첫번째 곡 빼기
         for a in song: #song에 있는 숫자에 따라 나타내는 소리가 다르기에 하나씩 뽑아서 맞는 칸에 currBlk이 뜨게 하고 해당 칸에 맞는 음이 나도록 해야함
               top=2
               left=2
               QiScreen=Matrix(QarrayScreen)    #QarrayScreen을 행렬형태로 받는 QiScreen생성
               if a==261:  #a가 261일 경우, 도를 나타내며 currBlk의 left위치는 2
                     left=2
                                         
               elif a==294:   #a가 294일 경우, 레를 나타내며 currBlk의 left위치는 2+4
                     left+=4

               elif a==329:    #a가 329일 경우, 미를 나타내며 currBlk의 left위치는 2+8
                     left+=8
      
               elif a==349:    #a가 349일 경우, 파를 나타내며 currBlk의 left위치는 2+12
                     left+=12

               elif a==393:    #a가 393일 경우, 솔을 나타내며 currBlk의 left위치는 2+16
                     left+=16

               elif a==440:    #a가 440일 경우, 라를 나타내며 currBlk의 left위치는 2+20
                     left+=20

               elif a==493:    #a가 493일 경우, 시를 나타내며 currBlk의 left위치는 2+24
                     left+=24

               tempBlk=QiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx()) #컨트롤하는 블럭의 위치를 나타내는 tempBlk을 QiScreen으로부터 잘라와 생성
               tempBlk=tempBlk+currBlk #위치 나타내는 tempBlk과 모양을 나타내는 currBlk을 합쳐 최종 컨트롤블럭 tempBlk 재생성
               QoScreen = Matrix(QiScreen)   #QiScreen을 행렬형태로 받는 QoScreen생성
               QoScreen.paste(tempBlk, top, left)  #QoScreen에 tempBlk붙여넣기
               LED_init()  #LED matrix에 불켜기
               draw_matrix(QoScreen); print()  #QoScreen을 LED matrix에 출력 
            
               pwm.start(50)              #아래는 피에조부저에서 song에 있는 음들이 나오게 하는 코드임
               pwm.ChangeDutyCycle(90)
               pwm.ChangeFrequency(a)
               time.sleep(0.7)
               draw_matrix(QiScreen); print()

         top=2
         left=2
         answer=[] #문제에서 들려준 순서대로 사용자가 입력했는지 답안을 저장할 리스트 answer 생성
         AarrayScreen=[                                                                #사용자가 입력할 화면 AarrayScreen생성
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
                    
         AiScreen=Matrix(AarrayScreen) #AarrayScreen을 행렬형태로 만든 AiScreen생성
         AoScreen=Matrix(AiScreen) #AiScreen을 행렬형태로 받은 AoScreen생성
         tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx()) # 위의 내용(Qarray에서 설명)과 동일
         tempBlk=tempBlk+currBlk
         AoScreen.paste(tempBlk,top,left)
         draw_matrix(AoScreen); print()
         hint=0   #힌트 사용 여부를 알기 위한 변수 hint 생성

         while True:
               print('Direction : q(quit), a(left), d(right)')
               print('Push the piano : p(push)')
               print('Finish : \' \'')
               key=input('Enter a key : ')   #사용자로부터 키 값 입력받기
               if key=='q':   # q 입력 시, 반복문을 탈출하면서 게임종료
                     print('Game terminated')
                     break
               elif key=='a':    # a 입력 시, 컨트롤 블럭의 위치 left를 4칸 왼쪽으로 이동, 블럭이 왼쪽 벽이 닿아있을 시 더이상 이동하지X
                     if left==2:
                           continue
                     left-=4
               elif key=='d':    # d 입력 시, 컨트롤 블럭의 위치 left를 4칸 오른쪽으로 이동, 블럭이 오른쪽 벽이 닿아있을 시 더이상 이동하지X
                     if left==26:
                           continue
                     left+=4
               elif key=='p':    # p 입력 시, 블럭의 위치에 따라 피에조 부저에서 울리는 음이 다름
                     if left==2:       #블럭의 위치 left가 2일때, 주파수 261인 도 음이 울리고, 261이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(261)
                           pwm.ChangeFrequency(261)
                     elif left==6:     #블럭의 위치 left가 6일때, 주파수 294인 레 음이 울리고, 294이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(294)
                           pwm.ChangeFrequency(294)
                     elif left==10:    #블럭의 위치 left가 10일때, 주파수 329인 미 음이 울리고, 329이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(329)
                           pwm.ChangeFrequency(329)
                     elif left==14:    #블럭의 위치 left가 14일때, 주파수 349인 파 음이 울리고, 349이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(349)
                           pwm.ChangeFrequency(349)
                     elif left==18:    #블럭의 위치 left가 18일때, 주파수 393인 솔 음이 울리고, 393이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(393)
                           pwm.ChangeFrequency(393)
                     elif left==22:    #블럭의 위치 left가 22일때, 주파수 440인 라 음이 울리고, 440이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(440)
                           pwm.ChangeFrequency(440)
                     elif left==26:    #블럭의 위치 left가 26일때, 주파수 493인 시 음이 울리고, 493이라는 숫자가 사용자의 정답리스트에 추가됨
                           answer.append(493)
                           pwm.ChangeFrequency(493)
                                               
               elif key==' ':    #스페이스바 입력 시, 사용자의 정답 화면과 answer리스트 제출
                     break
                                     
               else:    #잘못된 키 값 입력시, 다시 입력 받음
                     print('Wrong key!')  
                     continue

               AiScreen=Matrix(AarrayScreen)    # 아래는 오리지널, 짝맞추기 게임과 같은 루틴/ 위에 문제화면 출력할때와 같은 방식임
                                      
               tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk

               AoScreen = Matrix(AiScreen)
               AoScreen.paste(tempBlk, top, left)
               draw_matrix(AoScreen); print()

         draw_matrix(AiScreen); print()
               
         #input_output_corfirm            
         if song==answer:     #문제 노래의 리스트와 사용자가 입력하여 생성된 리스트가 같다면 성공
               print("성공하셨습니다.")
               count+=1 #성공 시, 점수 1점 받음
               if count==4:      #모든 노래(4곡)를 성공했을 때, 
                  f=open("피아노 1등.txt",'r')      #피아노 모드 1등 기록이 적힌 파일을 열어 1등기록 읽어오기
                  file=f.read()  
                  f.close()
                  ls=file.splitlines()
                  for line in ls:
                       print("1등의 기록 : ",line)     #1등 기록 화면에 출력
                       line=int(line)        #1등기록을 정수형으로 바꾸기
                       draw_matrix(Score(line))    #1등기록을 score파일에 있는 Score함수의 인자로 넘겨주어 점수가 적힌 스크린 받아온 후, draw_matrix를 통해 그것을 LED화면에 출력
                       time.sleep(2)   #2초동안 보여줌
                       print(player,"의 기록 : ",count)  #사용자 기록 화면에 출력
                       draw_matrix(Score(count))   #사용자 기록을 score파일에 있는 Score함수의 인자로 넘겨주어 점수가 적힌 스크린 받아온 후, draw_matrix를 통해 그것을 LED화면에 출력
                       time.sleep(2)   #2초동안 보여줌
                       if int(line)<count:   #사용자 기록이 1등기록보다 높은 경우, 1등기록이 적힌 파일 열어 1등기록 갱신 
                           print("축하드립니다. 신기록을 세우셨군요!!")
                           f=open("피아노 1등.txt",'w')
                           line=f.write(str(count))
                           print("새로운 1등 기록 : ",count)
                       elif int(line)==count:   
                           print("축하드립니다! 공동 1등 입니다!")
                  i=2    #자동적으로 게임이 끝남(다시 시작 안하고 게임 끝난다는 의미의 i=2)
                  break
               continue
         elif song!=answer:   #실패했을 경우
               print("실패하셨습니다.")
               again=input("게임을 다시 시작하시겠습니까? (Y/N): ")   #다시 할 것인지 사용자에게 입력받은 변수 again생성
               f=open("피아노 1등.txt",'r')         # 아래는 점수 출력과정으로 바로 위(성공했을 때)경우와 동일함
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
               if again=='Y':       #again이 Y일 경우, i=1(다시 시작하겠다는 의미)
                   i=1
                   continue
               elif again=='N':     #again이 N일 경우, i=2(다시 시작 안하고 게임 끝낸다는 의미)
                   i=2
                   break
