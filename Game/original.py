from matrix import*  
from random import*
import time
import LED_display as LMD
import threading
from score import*

def LED_init():     #LED에 불 들어오게 하기 위한 함수(threading)
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):     #원하는대로 matrix를 그리기 위한 함수
      array=m.get_array()
      for y in range (m.get_dy()):
         for x in range(m.get_dx()):
            if array[y][x]==0:
               LMD.set_pixel(x,y,0)
            elif array[y][x]==1:   #white(테두리)
               LMD.set_pixel(x,y,7)
            elif array[y][x]==2:  #skyblue (컨트롤하는 블록의 색상)
               LMD.set_pixel(x,y,6)
            elif array[y][x]==3:  #yellow (설치되는 노란색 블록)
               LMD.set_pixel(x,y,3)
            elif array[y][x]==4: #red  (설치되는 빨간색 블록)
               LMD.set_pixel(x,y,1)
            elif array[y][x]==7:   #green  (설치되는 초록색 블록)
               LMD.set_pixel(x,y,2)
            elif array[y][x]==12:   #blue  (설치되는 파란색 블록)
               LMD.set_pixel(x,y,4)
            elif array[y][x]==20:   #pink  (설치되는 핑크색 블록)
               LMD.set_pixel(x,y,5)
            else:        #white(겹칠 때 즉, 컨트롤하는 블록이 이동한 위치에 이미 설치된 블록이 있으면 설치된 상태라는 것을 하얀색 블록을 통해 알려줌)
               LMD.set_pixel(x,y,7)
         print()
def memory_key(): #기억력 게임 original ver 게임 내용을 담은 함수
      player=input("사용자 이름을 입력하세요 : ")  #플레이어의 정보(이름) 받기
      arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]   #플레이어가 컨트롤하는 블록 설정
      currBlk=Matrix(arrayBlk)   # 위에서 정한 컨트롤할 블록을 매트릭스 형태로 변환
      i=0   # 성공해서 다음단계로 넘어가는 것인지(i=0), 실패해서 다시 시작하는 것인지(i=1), 실패해서 게임을 종료하는 것인지(i=2) 구분하기 위한 변수i 설정
      success=0  #스코어를 누적하는 변수 success 설정
      level = int(input("난이도 easy는 1, hard는 2를 입력하세요: "))  #사용자로부터 난이도를 level이라는 변수에 입력받기
      while True:
         if i==1:
            success=0
            print("게임을 다시 시작합니다.")
         elif i==2:
            print("게임을 종료합니다.")
            break
         while True:
      #문제 화면 출력하기
            i=0 #게임을 다시 시작하게 되더라도 여기서 i=0으로 바뀌기 때문에, 처음 상태로 초기화 되어 플레이 할 수 있음
            QarrayScreen=[                                                         #문제 화면을 출력할 2차원 배열 QarrayScreen 설정
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],       #총 블럭의 갯수는 7*3=21개
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

            if level == 1:               #level이 easy일 때의 문제 화면 출력 과정
               lighton=sample(list(range(1,22)),7)   #21개의 칸 중 불을 킬 7개의 칸 랜덤으로 정하기
            
               for i in lighton:
                  top=2     #첫번째 줄의 top위치
                  left=2
                  if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):      #첫 줄에 있는 7개의 칸들 중 불이 들어와야한다면, 
                        left=left+(i-1)*4       #첫번째 줄의 left위치                       #해당 블록의 숫자를 3으로 바꿔 LED에 노란색 불로 켜지게 하기                     
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3         
                  elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):       #두번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=6      #두번째 줄의 top위치
                     left=left+(i-8)*4  #두번째 줄의 left위치
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
                  elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):         #세번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=10     #세번째 줄의 top위치
                     left=left+(i-15)*4     #세번째 줄의 left위치
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
               
            if level == 2:             #level이 hard일 때의 문제 화면 출력 과정
               lighton=sample(list(range(1,22)),8)  #21개의 칸 중 불을 킬 8개의 칸 랜덤으로 정하기
               red=lighton[:3]      #뽑은 리스트 중 맨 앞 세 개는 빨간색
               yellow=lighton[3:5]      #중간 두 개는 노란색
               green=lighton[5:]        #맨 마지막 세 개는 초록색이 됨

               for i in lighton:
                  top=2
                  left=2
                  if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):  #easy모드와 비슷하지만, hard모드는 첫 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 
                     left=left+(i-1)*4                                                     # 해당 블록의 숫자를 4,3,7으로 바꿔 LED에 빨간색, 노란색, 초록색 불로 켜지게 하기
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           if i in red:
                              QarrayScreen[a][b]=4
                           elif i in yellow:
                              QarrayScreen[a][b]=3
                           elif i in green:
                              QarrayScreen[a][b]=7
                  elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):   #두번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=6
                     left=left+(i-8)*4
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           if i in red:
                              QarrayScreen[a][b]=4
                           elif i in yellow:
                              QarrayScreen[a][b]=3
                           elif i in green:
                              QarrayScreen[a][b]=7
                  elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):     #세번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=10        
                     left=left+(i-15)*4
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           if i in red:
                              QarrayScreen[a][b]=4
                           elif i in yellow:
                              QarrayScreen[a][b]=3
                           elif i in green:
                              QarrayScreen[a][b]=7

            QiScreen=Matrix(QarrayScreen)   #문제화면(QarrayScreen)을 행렬형태로 바꾼 QiScreen설정
            QoScreen=Matrix(QiScreen)       #QiScreen을 또 행렬형태로 바꾼 QoScreen설정
            LED_init()      #LED판에 불이 들어오게 하기 (threading문제가 생길 수 있으므로 한 번만 해줄 것)
            draw_matrix(QoScreen); print()      #draw_matrix함수를 이용해 QoScreen을 LED matrix에 그리기
            time.sleep(7)       #그린 상태로 7초간 사용자에게 보여주기
            
            #input
            top=2
            left=2
            AarrayScreen=[                                                               #사용자의 답을 입력받을 AarrayScreen생성
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

            currBlk=Matrix(arrayBlk)
            tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
            tempBlk=tempBlk+currBlk
            AoScreen.paste(tempBlk,top,left)
            draw_matrix(AoScreen); print()
            hint=0
            
            while True:

               print('Direction : q(quit), a(left), d(right), s(down)')
               print('Fix the color block : r(red), y(yellow), g(green)')
               print('Erase the block : e(erase)')
               print('Hint : h(hint)')
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
               elif key=='s':
                  if top==10:
                     continue
                  top+=4
               elif key=='w':
                  if top==2:
                     continue
                  top-=4
               elif key=='y':
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==7):
                           AarrayScreen[a][b]=3
                           continue
                        elif AarrayScreen[a][b]==3:
                           AarrayScreen[a][b]=0
                           continue
                
               elif key=='r':
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==7):
                           AarrayScreen[a][b]=4
                           continue
                        elif AarrayScreen[a][b]==4:
                           AarrayScreen[a][b]=0
                           continue
               
               elif key=='g':
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==3):
                           AarrayScreen[a][b]=7
                           continue
                        elif AarrayScreen[a][b]==7:
                           AarrayScreen[a][b]=0
                           continue
                        
               elif key=='e':
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
               elif key=='h':
                  if hint==0:
                        success-=1
                        draw_matrix(QoScreen);print()
                        time.sleep(3)
                        hint+=1
                  
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
            for a in range(2,14):
                  for b in range(2, 30):
                        if QarrayScreen[a][b] != AarrayScreen[a][b]:
                            print("실패하셨습니다.")
                            thehalgguenya = input("게임을 다시 시작하시겠습니까? (Y/N): ")
                            if thehalgguenya == "Y":
                                i = 1
                                break
                            elif thehalgguenya == "N":
                                i = 2
                                break
                  if (i==1)or(i==2):
                        break
         
            if i == 0:
               print("success")
               success+=2
               continue
                               
            elif (i==1)or(i==2):
               if level==1:
                   f = open("오리지널easy_1등.txt", 'r')
                   file = f.read()
                   f.close()
                   ls = file.splitlines()
               elif level==2:
                   f=open("오리지널hard_1등.txt",'r')
                   file=f.read()
                   f.close()
                   ls=file.splitlines()
               for line in ls:
                   success=int(success)
                   print("1등의 기록 : ", line)
                   line=int(line)
                   draw_matrix(Score(line))
                   time.sleep(2)
                   print(player,"의 기록: ",success)
                   draw_matrix(Score(success))
                   time.sleep(2)
                   if float(line)<success:
                       print("축하드립니다. 신기록을 세우셨군요!!")
                       if level==1:
                           f= open("오리지널easy_1등.txt", 'w')
                           line = f.write(str(success))
                           print("새로운 1등 기록 : ",success)
                           f.close()
                       elif level==2:
                           f= open("오리지널hard_1등.txt", 'w')
                           line = f.write(str(success))
                           print("새로운 1등 기록 : ",success)
                           f.close()
               break
      
