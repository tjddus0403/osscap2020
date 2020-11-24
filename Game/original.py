from matrix import*
from random import*
import time
import LED_display as LMD
import threading
from score import*

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):
      array=m.get_array()
      for y in range (m.get_dy()):
         for x in range(m.get_dx()):
            if array[y][x]==0:
               LMD.set_pixel(x,y,0)
            elif array[y][x]==1:   #white(테두리)
               LMD.set_pixel(x,y,7)
            elif array[y][x]==2:  #skyblue
               LMD.set_pixel(x,y,6)
            elif array[y][x]==3:  #yellow
               LMD.set_pixel(x,y,3)
            elif array[y][x]==4: #red
               LMD.set_pixel(x,y,1)
            elif array[y][x]==7:   #green
               LMD.set_pixel(x,y,2)
            elif array[y][x]==12:   #blue
               LMD.set_pixel(x,y,4)
            elif array[y][x]==20:   #pink
               LMD.set_pixel(x,y,5)
            else:        #white(겹칠떄)
               LMD.set_pixel(x,y,7)
         print()
def memory_key():
      player=input("사용자 이름을 입력하세요 : ")
      arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
      currBlk=Matrix(arrayBlk)
      i=0
      success=0
      level = int(input("난이도 easy는 1, hard는 2를 입력하세요: "))
      while True:
         if i==1:
            success=0
            print("게임을 다시 시작합니다.")
         elif i==2:
            print("게임을 종료합니다.")
            break
         while True:
      #output
            i=0
            QarrayScreen=[
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

            if level == 1:
               lighton=sample(list(range(1,22)),7)

               currBlk=Matrix(arrayBlk)
               for i in lighton:
                  top=2
                  left=2
                  if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):
                     left=left+(i-1)*4
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
                  elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):
                     top=6
                     left=left+(i-8)*4
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
                  elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):
                     top=10
                     left=left+(i-15)*4
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
               
            if level == 2:
               lighton=sample(list(range(1,22)),8)
               red=lighton[:3]
               yellow=lighton[3:5]
               green=lighton[5:]

               for i in lighton:
                  top=2
                  left=2
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

            QiScreen=Matrix(QarrayScreen)
            QoScreen=Matrix(QiScreen)
            LED_init()
            draw_matrix(QoScreen); print()
            time.sleep(7)
            #input
            AiScreenDy=12
            AiScreenDx=28
            AiScreenDw=2
            top=2
            left=2
            AarrayScreen=[
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

            #prepare the initial screen output
            AiScreen=Matrix(AarrayScreen)
            AoScreen=Matrix(AiScreen)
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
                   time.sleep(1)
                   print(player,"의 기록: ",success)
                   draw_matrix(Score(success))
                   time.sleep(1)
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
      
