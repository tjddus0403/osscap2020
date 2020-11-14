from matrix import*
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
         elif array[y][x]==7:
            print("▩", end=' ')
         else:
            print("X", end=' ')
      print()

arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]

iScreenDy=12
iScreenDx=28
iScreenDw=2
top=2
left=2
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

#prepare the initial screen output
iScreen=Matrix(arrayScreen)
oScreen=Matrix(iScreen)
currBlk=Matrix(arrayBlk)
tempBlk=iScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
tempBlk=tempBlk+currBlk
oScreen.paste(tempBlk,top,left)
draw_matrix(oScreen); print()

while True:
   #arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
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
            if (arrayScreen[a][b]==0)or(arrayScreen[a][b]==4)or(arrayScreen[a][b]==7):
               arrayScreen[a][b]=3
               continue
            elif arrayScreen[a][b]==3:
               arrayScreen[a][b]=0
               continue
      iScreen=Matrix(arrayScreen)
      oScreen=Matrix(iScreen)
   elif key=='r':
      for a in range(top,top+currBlk.get_dy()):
         for b in range(left,left+currBlk.get_dx()):
            if (arrayScreen[a][b]==0)or(arrayScreen[a][b]==3)or(arrayScreen[a][b]==7):
               arrayScreen[a][b]=4
               continue
            elif arrayScreen[a][b]==4:
               arrayScreen[a][b]=0
               continue
      iScreen=Matrix(arrayScreen)
      oScreen=Matrix(iScreen)
   elif key=='g':
      for a in range(top,top+currBlk.get_dy()):
         for b in range(left,left+currBlk.get_dx()):
            if (arrayScreen[a][b]==0)or(arrayScreen[a][b]==4)or(arrayScreen[a][b]==3):
               arrayScreen[a][b]=7
               continue
            elif arrayScreen[a][b]==7:
               arrayScreen[a][b]=0
               continue
      iScreen=Matrix(arrayScreen)
      oScreen=Matrix(iScreen)    
   elif key=='e':
      for a in range(top,top+currBlk.get_dy()):
         for b in range(left,left+currBlk.get_dx()):
            arrayScreen[a][b]=0
            
      iScreen=Matrix(arrayScreen)
      oScreen=Matrix(iScreen)
   elif key==' ':
      break
   else:
      print('Wrong key!')
      continue

   tempBlk=iScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
   tempBlk=tempBlk+currBlk

   oScreen = Matrix(iScreen)
   oScreen.paste(tempBlk, top, left)
   draw_matrix(oScreen); print()
draw_matrix(iScreen); print()
