from matrix import*
from random import*
import random
import time
from original import*

def gallery_mode_exe():
    arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
    currBlk=Matrix(arrayBlk)
    count=0
    hint=0
    Q=0
    i=0
    score=0
    
    while True:
        if Q==1:
            print("게임을 중도포기하셨습니다. 게임을 종료합니다.")
            break
        
        if count==5:
            print("갤러리 모드를 성공하셨습니다. 게임을 종료합니다.")
            break
        if i==1:
            print("게임을 다시 시작합니다.")
        elif i==2:
            print("게임을 종료합니다.")
            break
        if score>0:
         f = open("갤러리1등.txt", 'r')
         file = f.read()
         f.close()
         list = file.splitlines()
         for line in list:
             print(line)
             if int(line)<score:
                f= open("갤러리1등.txt", 'w')
                line = f.write(str(score))
         f.close() 
    
        print("환영합니다. 게임을 시작합니다.")        
       
        #갤러리 속 그림의 종류 수박,아스크림,당근,하트,강아지 총 5가지
        # a,b,c,d같은 요소는 수박 4등분한 각각의 그림파일을 의미
        gallery = [['a','b','c','d'],['e','f','g','h'],['i','j'],['k','l'],['m','n','o','p','q','r']]
        random.shuffle(gallery)
        #print(gallery)

        for picture in gallery:
            count = count+1
            random.shuffle(picture)
            #print(picture)
            for order in picture:
                #print(order)
                if order == 'a':
                    from watermelon import QarrayScreen1 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'b':
                    from watermelon import QarrayScreen2 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'c':
                    from watermelon import QarrayScreen3 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'd':
                    from watermelon import QarrayScreen4 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'e':
                    from icecream import QarrayScreen5 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'f':
                    from icecream import QarrayScreen6 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'g':
                    from icecream import QarrayScreen7 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'h':
                    from icecream import QarrayScreen8 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'i':
                    from carrot import QarrayScreen9 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'j':
                    from carrot import QarrayScreen10 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'k':
                    from heart import QarrayScreen11 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'l':
                    from heart import QarrayScreen12 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'm':
                    from dog import QarrayScreen13 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'n':
                    from dog import QarrayScreen14 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'o':
                    from dog import QarrayScreen15 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'p':
                    from dog import QarrayScreen16 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'q':
                    from dog import QarrayScreen17 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'r':
                    from dog import QarrayScreen18 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)

                QoScreen=Matrix(QiScreen)
                draw_matrix(QoScreen); print()
                time.sleep(15)

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

                while True:

                    print('Direction : q(quit), a(left), d(right), s(down)')
                    print('Fix the color block : r(red), y(yellow), g(green), b(brown), o(orange)')
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

                    elif key=='h':
                        if hint==0:
                            score-=1
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
       

                if Q==1:
                    i=-1
                    break
                
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
                            else:
                                print("잘못된 입력입니다.")
                                continue
                    if (i==1)or(i==2):
                        break
                if i == 0:
                    score+=2
                    print("success")
                    continue
                    # for i in picture 루프로 돌아가 다음 그림 출력                                
                if (i==1)or(i==2):
                    break
            if i == 0:
                print("그림하나를 완성하셨습니다.")
                if order == 'a' or order == 'b' or order == 'c' or order == 'd':
                    from watermelon import QarrayScreen
                elif order == 'e' or order == 'f' or order == 'g' or order == 'h':
                    from icecream import QarrayScreen 
                elif order == 'i' or order == 'j':
                    from carrot import QarrayScreen
                elif order == 'k' or order == 'l':
                    from heart import QarrayScreen
                elif order == 'm' or order == 'n' or order == 'o' or order == 'p'or order == 'q' or order == 'r':
                    from dog import QarrayScreen
                QiScreen=Matrix(QarrayScreen)
                QoScreen=Matrix(QiScreen)
                draw_matrix(QoScreen); print()
                
            if (i==1)or(i==2):
                break
            
            if Q==1:
                break

#gallery_mode_exe()
