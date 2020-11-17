from matrix import*
from random import*
import random

def draw_matrix(m):
    array=m.get_array()
    for y in range (m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x]==0:
                print("□", end=' ')
               #none 비어있음
            elif array[y][x]==1:
               print("■", end=' ')
               #blue
            elif array[y][x]==2:
               print("▣", end=' ')
               #purple
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
                #brown
            elif array[y][x]==20:
                print("▦", end=' ')
                #orange
            else:
               print("X", end=' ')
               #white 겹치는거
        print()

arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
currBlk=Matrix(arrayBlk)
i=0

while True:
    if i==1:
        print("게임을 다시 시작합니다.")
    elif i==2:
        print("게임을 종료합니다.")
        break
    while True:
        #일단 그림의 종류 수박,아스크림 2가지라고 가정
        # a,b,c,d같은 요소는 수박 4등분한 각각의 그림파일을 의미
        # e,f,g,h는 아이스크림 4등분한 각각의 그림파일 의미
        gallery = [['a','b','c','d'],['e','f','g','h']]
        random.shuffle(gallery)
        print(gallery)

        for picture in gallery:
            random.shuffle(picture)
            print(picture)
            for order in picture:
                print(i)
                
                if order == 'a':
                    from a import QarrayScreen
                if order == 'b':
                    from b import QarrayScreen
                if order == 'c':
                    from c import QarrayScreen
                if order == 'd':
                    from d import QarrayScreen
                if order == 'e':
                    from e import QarrayScreen
                if order == 'f':
                    from f import QarrayScreen
                if order == 'g':
                    from g import QarrayScreen
                if order == 'h':
                    from h import QarrayScreen
                QiScreen=Matrix(QarrayScreen)
                QoScreen=Matrix(QiScreen)
                draw_matrix(QoScreen); print()

                # input코드 여기부터 복붙
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
                    print('Fix the color block : r(red), y(yellow), g(green), b(brown), o(orange)')
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

                    elif key=='o':
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
                    # for i in picture 루프로 돌아가 다음 그림 출력
                                     
                elif (i==1)or(i==2):
                    break

            if (i==1)or(i==2):
                break
            if i == 0:
                if order == 'a' or order == 'b' or order == 'c' or order == 'd':
                    from watermelon import QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                    QoScreen=Matrix(QiScreen)
                    draw_matrix(QoScreen); print()
                if order == 'e' or order == 'f' or order == 'g' or order == 'h':
                    from icecream import QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                    QoScreen=Matrix(QiScreen)
                    draw_matrix(QoScreen); print()
                
        if (i==1)or(i==2):
            break
