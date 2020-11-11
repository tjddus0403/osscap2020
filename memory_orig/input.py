from matrix import*
def draw_matrix(n):
   array=m.get_array()
   for y in range (m.get_dy()):
      for x in range(m.get_dx()):
         if array[y][x]==0:
            print("□", end=' ')
         elif array[y][x]==1:
            print("■", end=' ')
         else:
            print("XX", end=' ')
         print()

arrayBlk=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
iScreenDy=14
iScreenDx=30
iScreenDw=4
top=0
left=iScreenDw+iScreenDx//2-2
arrayScreen=[
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

#prepare the initial screen output
iScreen=Matrix(arrayScreen)
oScreen=Matrix(iScreen)
currBlk=Matrix(arrayBlk)
tempBlk=iScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
tempBlk=tempBlk+currBlk
oScreen.paste(tempBlk,top,left)
draw_matrix(oScreen)
print()

while True:
   key=input('Enter a key from [q(quit), a(left), d(right), s(down), w(up), f(fix)] : ')
   if key=='q':
      print('Game terminated')
      break
   elif key=='a':
      left-=1
   elif key=='d':
      left+=1
   elif key=='s':
      top+=1
   elif key=='w':
      top-=1
   elif key=='f':
      
   else:
      print('Wrong key!')
      continue

   tempBlk=iScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
   tempBlk=tempBlk+currBlk
   if tempBlk.get_dy()==0:
      if key=='w':
         top+=1
   elif tempBlk.get_dx()==0:
      if key=='a':
         left+=1
   elif tempBlk.get_dy()==13:
      if key=='s':
         top-=1
   elif tempBlk.get_dy()==29:
      if key=='d':
         left-=1

   
      
      

   
