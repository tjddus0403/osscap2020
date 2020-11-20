from matrix import*
from random import*
import random
import time
'''import RPi.GPIO as GPIO'''

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

arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
currBlk=Matrix(arrayBlk)
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




plane=[330, 294, 261, 294, 330, 330, 330, 294,
       294, 294, 330, 392, 392, 330, 294, 261,
       294, 330, 330, 330, 294, 294, 330, 294,
       261, 523]
haul=[293, 391, 493, 587, 587, 523, 493, 440,
      493, 391, 493, 587, 783, 783, 783, 880,
      693, 659, 698, 440, 554, 698, 880, 783,
      698, 659, 698, 783, 698, 659, 587, 523,
      493, 523, 587, 523, 391, 440]


'''buzzer_pin=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)'''

#일단 노래가 두가지라고 가정. a가 비행기, b가 하울이라고 가정.
playlist = ['a','b']
random.shuffle(playlist)

for song in playlist:
      if song=='a':
            num=0
            
            lighton=[]
            for j in range(26):
                  n = random.randrange(1, 22)
                  lighton.append(n)
            print(lighton)

            red=lighton[:5]
            yellow=lighton[5:10]
            green=lighton[10:15]
            blue=lighton[15:20]
            pink=lighton[20:26]
            #문제 출력할때 차례대로 하나씩 보여주는거 구현은 했는데 이 위에 5줄 코드로 하면
            #처음부터 레드만 5개,옐로우 5개 그린 5개...순서대로 나와서
            #색깔을 옐로,그린,핑크,그린,레드,블루 이케 랜덤으로 나와야하는데
            #어케 해야할지 아무리 대가리 굴려도 모르겠음


            for i in lighton:
                  num+=1
                  if num>1:
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=0
                              
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
                  draw_matrix(QoScreen); print()
                  time.sleep(0.5)

            
                  '''try:
                        pwm=GPIO.PWM(buzzer_pin,100);
                        pwm.start(100)
                        pwm.ChangeDutyCycle(90)
                        for i in plane:
                              pwm.ChangeFrequency(i)
                              time.sleep(0.5)
                        #for i in range(len(num)):
                              #    pwm.ChangeFrequency(list[num[i]])
                              #   time.sleep(1)

                  
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()'''

            # input
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
                  print('Fix the color block : r(red), y(yellow), g(green), B(blue), P(Pink)')
                  print('Erase the block : e(erase)')
                  print('Use a hint : h(hint)')
                  print('Finish : \' \'')
                  key=input('Enter a key : ')
                  if key=='q':
                        Q=1
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
                                    if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==7)or(AarrayScreen[a][b]==12)or(AarrayScreen[a][b]==20):
                                          AarrayScreen[a][b]=3
                                          continue
                                    elif AarrayScreen[a][b]==3:
                                          AarrayScreen[a][b]=0
                                          continue
                            
                  elif key=='r':
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==7)or(AarrayScreen[a][b]==12)or(AarrayScreen[a][b]==20):
                                          AarrayScreen[a][b]=4
                                          continue
                                    elif AarrayScreen[a][b]==4:
                                          AarrayScreen[a][b]=0
                                          continue
                             
                  elif key=='g':
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==12)or(AarrayScreen[a][b]==20):
                                          AarrayScreen[a][b]=7
                                          continue
                                    elif AarrayScreen[a][b]==7:
                                          AarrayScreen[a][b]=0
                                          continue

                  elif key=='b':
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==7)or(AarrayScreen[a][b]==20):
                                          AarrayScreen[a][b]=12
                                          continue
                                    elif AarrayScreen[a][b]==12:
                                          AarrayScreen[a][b]=0
                                          continue

                  elif key=='p':
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==7)or(AarrayScreen[a][b]==12):
                                          AarrayScreen[a][b]=20
                                          continue
                                    elif AarrayScreen[a][b]==20:
                                          AarrayScreen[a][b]=0
                                          continue
                                      
                  elif key=='e':
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    AarrayScreen[a][b]=0

                  elif key=='h':
                        if hint==0:
                              score=-1
                              draw_matrix(QoScreen);print()
                              time.sleep(5)
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
      


