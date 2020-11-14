from matrix import*
from random import*

def draw_matrix(m):
      array=m.get_array()
      for y in range (m.get_dy()):
         for x in range(m.get_dx()):
            if array[y][x]==0:
               print("□", end=' ')
            elif array[y][x]==1:
               print("■", end=' ')
            elif array[y][x]==2:
               print("▣", end=' ')
            elif array[y][x]==3:
               print("▨", end=' ')
            elif array[y][x]==4:
               print("▤", end=' ')
            elif array[y][x]==5:
               print("▩", end=' ')
            else:
               print("X", end=' ')
         print()
arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
currBlk=Matrix(arrayBlk)

#output
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


level = int(input("난이도 easy는 1, hard는 2를 입력하세요: "))

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
                  QarrayScreen[a][b]=5
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
                  QarrayScreen[a][b]=5
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
                  QarrayScreen[a][b]=5

QiScreen=Matrix(QarrayScreen)
QoScreen=Matrix(QiScreen)
draw_matrix(QoScreen); print()

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

while True:

   print('Direction : q(quit), a(left), d(right), s(down)')
   print('Fix the color block : r(red), y(yellow), g(green)')
   print('Erase the block : e(erase)')
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