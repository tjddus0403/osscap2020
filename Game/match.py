from matrix import*
from original import draw_matrix
import copy
from random import*
import time
def memory_to():
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
      
      lighton=[]
      for i in range(20):
         num=randint(1,21)
         while True:
            if num in lighton:
               num=randint(1,21)
            else:
               break
         lighton.append(num)
      red=lighton[:4]
      yellow=lighton[4:8]
      green=lighton[8:12]
      brown=lighton[12:16]
      orange=lighton[16:]
      print(red, yellow, green, brown, orange)
      arrayBlk=[[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,2,2,2]]
      currBlk=Matrix(arrayBlk)
      
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
                  elif i in brown:
                     QarrayScreen[a][b]=12
                  elif i in orange:
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
                  elif i in brown:
                     QarrayScreen[a][b]=12
                  elif i in orange:
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
                  elif i in brown:
                     QarrayScreen[a][b]=12
                  elif i in orange:
                     QarrayScreen[a][b]=20

      QiScreen=Matrix(QarrayScreen)
      QoScreen=Matrix(QiScreen)
      draw_matrix(QoScreen); print()
      time.sleep(15)
      start_time=time.time()
      
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
               time.sleep(2)  
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
            continue
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
         runtime=round(end_time-start_time,3)

         f = open("짝맞추기1등.txt", 'r')
         file = f.read()
         f.close()
         list = file.splitlines()
         print(list[0])
         print(runtime)
         for line in list:
             print(line)
             if float(line)>runtime:
                f= open("짝맞추기1등.txt", 'w')
                line = f.write(str(runtime))
         f.close()


