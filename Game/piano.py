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



'''buzzer_pin=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)'''

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
                  if a==261:
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=4
                  elif a==294:
                        left+=4
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=3
                  elif a==329:
                        left+=8
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=7
                  elif a==349:
                        left+=12
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=12
                  elif a==393:
                        left+=16
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=7
                  elif a==440:
                        left+=20
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=3
                  elif a==493:
                        left+=24
                        for a in range(top,top+currBlk.get_dy()):
                              for b in range(left,left+currBlk.get_dx()):
                                    QarrayScreen[a][b]=4
                                    
                        QiScreen=Matrix(QarrayScreen)
                        QoScreen=Matrix(QiScreen)
                        draw_matrix(QoScreen); print()
                        time.sleep(0.5)


                        '''
                        try:
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
                  currBlk=Matrix(arrayBlk)
                  tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
                  tempBlk=tempBlk+currBlk
                  AoScreen.paste(tempBlk,top,left)
                  draw_matrix(AoScreen); print()
                  hint=0

                  while True:

                        print('Direction : q(quit), a(left), d(right)')
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
                     continue
                                     
                  elif (i==1)or(i==2):
                     break
