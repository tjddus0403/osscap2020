from matrix import*
from random import*
import random
import time

def draw_matrix(m):
    array=m.get_array()
    for y in range (m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x]==0:
                print("□", end=' ')
               #none 비어있음
            elif array[y][x]==1:
               print("■", end=' ')
               #white
            elif array[y][x]==2:
               print("▣", end=' ')
               #skyblue
            elif array[y][x]==3:
               print("▨", end=' ')
               #yellow
            elif array[y][x]==4:
               print("▤", end=' ')
               #red
            elif array[y][x]==7:
               print("▩", end=' ')
               #green
            elif array[y][x]==12:
                print("▥", end=' ')
                #blue
            elif array[y][x]==20:
                print("▦", end=' ')
                #pink
            else:
               print("X", end=' ')
               #white 겹치는거
        print()

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

piano=[261,294,329,349,393,440,493,523]

star=[261,261,393,393,440,440,393]

plane=[329, 294, 261, 294, 329, 329, 329, 294,
       294, 294, 329, 393, 393 ]

butterfly=[393,329,329,349,294,294]

playlist = [star,plane,butterfly]
random.shuffle(playlist)
i=0
while True:
      if (i==1)or(i==2):
            break
      for song in playlist:
            for a in song:
                  top=2
                  left=2
                  QiScreen=Matrix(QarrayScreen)
                  if a==261:
                        left=2

                  elif a==294:
                        left+=4

                  elif a==329:
                        left+=8

                  elif a==349:
                        left+=12

                  elif a==393:
                        left+=16

                  elif a==440:
                        left+=20

                  elif a==493:
                        left+=24

                  tempBlk=QiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
                  tempBlk=tempBlk+currBlk
                  QoScreen = Matrix(QiScreen)
                  QoScreen.paste(tempBlk, top, left)
                  draw_matrix(QoScreen); print()
                  time.sleep(0.5)
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
                  elif left==6:
                        answer.append(294)
                  elif left==10:
                        answer.append(329)
                  elif left==14:
                        answer.append(349)
                  elif left==18:
                        answer.append(393)
                  elif left==22:
                        answer.append(440)
                  elif left==26:
                        anwer.append(493)
                                            
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
            continue
      elif song!=answer:
            print("실패하셨습니다.")
            again=input("게임을 다시 시작하시겠습니까? (Y/N): ")
            if again=='Y':
                  i=1
                  break
            elif again=='N':
                  i=2
                  break
 
