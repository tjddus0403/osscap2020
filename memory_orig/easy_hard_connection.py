from matrix import*
from random import*

arrayScreen=[
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

level = input("난이도를 선택하세요(easy or hard): ")

if level == "easy":
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
            else:
               print("X", end=' ')
         print()
         

   arrayBlk=[[3,3,3,3],[3,3,3,3],[3,3,3,3],[3,3,3,3]]
   lighton=sample(list(range(1,22)),7)
   print (lighton)

   currBlk=Matrix(arrayBlk)
   for i in lighton:
      top=2
      left=2
      if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):
         left=left+(i-1)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               arrayScreen[a][b]=3
      elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):
         top=6
         left=left+(i-8)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               arrayScreen[a][b]=3
      elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):
         top=10
         left=left+(i-15)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               arrayScreen[a][b]=3
   iScreen=Matrix(arrayScreen)
   oScreen=Matrix(iScreen)
   draw_matrix(oScreen); print()


if level == "hard":
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

   arrayBlk=[[3,3,3,3],[3,3,3,3],[3,3,3,3],[3,3,3,3]]
   lighton=sample(list(range(1,22)),8)
   red=lighton[:3]
   yellow=lighton[3:5]
   green=lighton[5:]
   print (lighton)
   print(red,yellow,green)
   currBlk=Matrix(arrayBlk)
   for i in lighton:
      top=2
      left=2
      if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):
         left=left+(i-1)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               if i in red:
                  arrayScreen[a][b]=4
               elif i in yellow:
                  arrayScreen[a][b]=3
               elif i in green:
                  arrayScreen[a][b]=5
      elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):
         top=6
         left=left+(i-8)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               if i in red:
                  arrayScreen[a][b]=4
               elif i in yellow:
                  arrayScreen[a][b]=3
               elif i in green:
                  arrayScreen[a][b]=5
      elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):
         top=10
         left=left+(i-15)*4
         for a in range(top,top+currBlk.get_dy()):
            for b in range(left,left+currBlk.get_dx()):
               if i in red:
                  arrayScreen[a][b]=4
               elif i in yellow:
                  arrayScreen[a][b]=3
               elif i in green:
                  arrayScreen[a][b]=5
   iScreen=Matrix(arrayScreen)
   oScreen=Matrix(iScreen)
   draw_matrix(oScreen); print()

