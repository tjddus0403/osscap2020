from matrix import*
from original import*
import copy
from random import*
import time
from score import*

def memory_to():
      player=input("플레이어의 이름을 입력하세요 : ")  #사용자 이름 입력받는 변수 player생성
      QarrayScreen=[                                                                      #문제화면을 나타내는 QarrayScreen생성 
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
      
      lighton=[] #불이 들어올 칸들의 리스트 생성
      for i in range(20):
         num=randint(1,21)
         while True:
            if num in lighton:
               num=randint(1,21)    #21개의 칸 중 20개의 칸만 랜덤으로 선택
            else:
               break
         lighton.append(num)  #선택된 20개의 칸을 위에서 생성한 리스트에 추가
      red=lighton[:4]   #리스트의 맨 처음부터 4번째까지의 칸으로 빨간색 리스트 생성
      yellow=lighton[4:8]     #리스트의 5번째부터 8번째까지의 칸으로 노란색 리스트 생성
      green=lighton[8:12]     #리스트의 9번째부터 12번째까지의 칸으로 초록색 리스트 생성
      blue=lighton[12:16]     #리스트의 13번째부터 16번째까지의 칸으로 파란색 리스트 생성 
      pink=lighton[16:]       #리스트의 17번째부터 마지막까지의 칸으로 핑크색 리스트 생성
    
      arrayBlk=[[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,2,2,2]] #사용자가 컨트롤할 블럭 배열
      currBlk=Matrix(arrayBlk)      #사용자가 컨트롤할 블럭배열을 행렬형태로 만든 currBlk생성
      
      for i in lighton:       #오리지널 모드와 마찬가지로 각 칸에 알맞은 색상 설정하기
         top=2                      #추가된 것은 파란색(번호12)과 핑크색(번호20) 두가지 뿐임
         left=2                                #문제 화면 띄우는 아래 과정들은 오리지널 모드와 동일
         if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):   
            left=left+(i-1)*4
            for a in range(top,top+currBlk.get_dy()):
               for b in range(left,left+currBlk.get_dx()):
                  if i in red:
                     QarrayScreen[a][b]=4
                  elif i in yellow:
                     QarrayScreen[a][b]=3
                  elif i in green:
                     QarrayScreen[a][b]=7
                  elif i in blue:
                     QarrayScreen[a][b]=12
                  elif i in pink:
                     QarrayScreen[a][b]=20
         elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):
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
                  elif i in blue:
                     QarrayScreen[a][b]=12
                  elif i in pink:
                     QarrayScreen[a][b]=20
         elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):
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
                  elif i in blue:
                     QarrayScreen[a][b]=12
                  elif i in pink:
                     QarrayScreen[a][b]=20

      QiScreen=Matrix(QarrayScreen)
      QoScreen=Matrix(QiScreen)
      LED_init()
      draw_matrix(QoScreen); print()
      time.sleep(7)     #문제화면 7초간 보여주기
      start_time=time.time()  #사용자의 기록을 시간으로 보여주기 위해서 시작시간 받아놓기
      
      top=2
      left=2
      AarrayScreen=[                                                               #사용자의 입력을 받을 정답화면 AarrayScreen 생성
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

      AiScreen=Matrix(AarrayScreen)       #AarrayScreen을 행렬형태로 만든 AiScreen 생성
      AoScreen=Matrix(AiScreen)           #AiScreen을 행렬형태로 받은 AoScreen 생성
      tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx()) #AiScreen에서 잘라 사용자가 컨트롤하는 블럭이 LED matrix에 움직이는 걸 보여주기 위한 위치블럭 tempBlk생성   
      tempBlk=tempBlk+currBlk       #위치블럭tempBlk에 모양블럭currBlk을 붙여 최종 사용자가 컨트롤하는 블럭tempBlk 재생성
      AoScreen.paste(tempBlk,top,left)    #AoScreen에 tempBlk붙이기
      draw_matrix(AoScreen); print()
      hint=0
      t1=None
      t2=None
      l1=None
      l2=None
      count=0
      while True:
         
         print('Direction : q(quit),a(left),d(right),s(down)')
         print('Open the card : o(open)')
         print('Finish : \' \'')
         print('Hint : h(hint)')
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

         elif key=='o':
         
            
            if AarrayScreen[top][left]!=0:
               continue
            count+=1
            for a in range(top,top+currBlk.get_dy()):
               for b in range(left,left+currBlk.get_dx()):
                  if count%2==1:
                     t1=top
                     l1=left
                  elif count%2==0:
                     t2=top
                     l2=left
                  if(AarrayScreen[a][b]==0):
                     AarrayScreen[a][b]=copy.deepcopy(QarrayScreen[a][b])
              
            if count%2==0 and count!=0 :
               AiScreen=Matrix(AarrayScreen) 
               tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk
               AoScreen=Matrix(AiScreen)
               AoScreen.paste(tempBlk,top, left)
               draw_matrix(AoScreen); print()
               time.sleep(1)  
               if AarrayScreen[t1][l1]!=AarrayScreen[t2][l2]:
                  for a in range(t1,t1+currBlk.get_dy()):
                     for b in range(l1,l1+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
                  for a in range(t2,t2+currBlk.get_dy()):
                     for b in range(l2,l2+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
         elif key=='h':
            if hint==0:
                  draw_matrix(QoScreen);print()
                  time.sleep(4)
                  hint+=1
            
         elif key==' ':
            break
         else:
            print("Wrong key!")
            continue
         AiScreen=Matrix(AarrayScreen) 
         tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
         tempBlk=tempBlk+currBlk
         AoScreen=Matrix(AiScreen)
         AoScreen.paste(tempBlk,top, left)
         draw_matrix(AoScreen); print()

      end_time=time.time()
      draw_matrix(AiScreen); print()
      i = 0
      for a in range(2,14):
         for b in range(2, 30):
               if QarrayScreen[a][b] != AarrayScreen[a][b]:
                     print("Game over")
                     i=1
                     break
         if i==1:
            break
      
      if i==0:
         runtime=(end_time-start_time)//1
         runtime=int(runtime)
         f = open("짝맞추기1등.txt", 'r')
         file = f.read()
         f.close()
         list = file.splitlines()
        
         for line in list:
             
             print("1등의 기록 : ", line)
             line=int(line)
             draw_matrix(Score(line))
             time.sleep(2)
             print(player,"의 기록: ",runtime)
             draw_matrix(Score(runtime))
             time.sleep(2)
             if line>runtime:
                print("축하드립니다. 신기록을 세우셨군요!!")
                f= open("짝맞추기1등.txt", 'w')
                line = f.write(str(runtime))
                print("새로운 1등 기록 : ",runtime)
         f.close()


