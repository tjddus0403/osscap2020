from matrix import*
import random
import time
from original import draw_matrix
import LED_display as LMD
import threading
from score import ScoreBlk
from score import Score

def LED_init():                                        ## LED에 불빛이 들어오게 하는 함수
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def gallery_mode_exe():                                ## 갤러리 모드 게임을 실행하는 함수
    arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]        ## 사용자가 조종하는 블록
    currBlk=Matrix(arrayBlk)      ## matrix로 변환        
    count=0      ## 그림 5개를 모두 맞췄는지 카운팅하기 위한 변수
    Q=0        ## 게임을 중도포기 했을 때 바로 게임을 종료시키기 위해 사용되는 변수
    i=0        ## 게임을 성공하거나 실패했을 때 게임을 계속 이어가거나 종료시키기 위해 사용되는 변수
    score=0     ## 사용자의 게임 스코어를 매기기 위해 사용되는 변수
    
    while True:               ##게임을 종료할 때까지 무한 루프
        if Q==1:
            print("게임을 중도포기하셨습니다. 게임을 종료합니다.")
            break                                                ## 사용자가 q를 입력하여 Q값이 1이 되면 무한루프 탈출 및 게임 종료
        if count==5:
            print("갤러리 모드를 성공하셨습니다. 게임을 종료합니다.")
            break                              ## 그림 5종류를 모두 성공하여 count값이 5가 되면 무한루프 탈출 및 게임 종료
        
        if (i==1)or(i==2):                     ## 게임을 성공하거나 실패한 경우(중도포기 제외) 점수 출력
            score=int(score)
            f = open("갤러리1등.txt", 'r')
            file = f.read()
            f.close()
            list = file.splitlines()     ## 갤러리1등 텍스트 파일에 저장되어있는 기존 1등의 점수를 읽어들여 list에 저장
            for line in list:
                print("1등의 기록 : ", line)
                line=int(line)                ## 점수를 정수 형태로 받아들임
                draw_matrix(Score(line))                 ## Score 함수를 호출해 해당 점수가 적힌 스크린을 리턴받고 draw_matrix 함수를 호출하여
                time.sleep(2)                         ## 기존 1등 점수 led matrix에 2초동안 출력
                print(player,"의 기록: ",score)
                draw_matrix(Score(score))
                time.sleep(2)                 ## 동일한 방식으로 현재 사용자 점수 2초동안 출력
                if line<score:
                    print("축하드립니다. 신기록을 세우셨군요!!")
                    f= open("갤러리1등.txt", 'w')
                    line = f.write(str(score))        ## 현 사용자가 신기록을 달성할경우 현 사용자의 점수를 갤러리1등 텍스트 파일에 1등의 점수로 새로 갱신
                    print("새로운 1등 기록 : ",score)           ## 현재 사용자가 달성한 신기록 출력
            f.close()
            if i==1:                                      ## 실패했지만 사용자가 게임을 다시 시작하겠다고 한 경우
                print("게임을 다시 시작합니다.")
            elif i==2:                             ## 실패했지만 사용자가 게임을 종료하겠다고 한 경우
                print("게임을 종료합니다.")
                break                            ## 무한루프 탈출 및 게임 종료
                
        ## output
        print("환영합니다. 게임을 시작합니다.")              ## 게임 시작
        player = input("플레이어의 이름을 입력하세요: ")            ## 사용자 이름 입력받음
        
        ## 갤러리 속 그림의 종류 수박,아이스크림,딸기,하트,강아지 총 5가지
        ## 각 그림은 조각 조각 나뉘어져 조각 하나씩 문제로 출제됨
        ## a,b,c,d같은 요소는 수박 그림을 4등분한 각각의 그림 조각 파일을 의미
        gallery = [['a','b','c','d'],['e','f','g','h'],['i','j'],['k','l'],['m','n','o','p','q','r']]
        random.shuffle(gallery)       ## 갤러리 리스트 속 요소들의 순서 무작위로 변경

        for picture in gallery:                ## 무작위로 변경된 순서대로, 즉 랜덤으로 그림 하나씩 뽑기
            count = count+1                    ## 뽑힌 그림 하나당 count 값이 1씩증가, count가 5가 되면 모든 그림이 출제된 것임
            random.shuffle(picture)            ## 뽑힌 그림 리스트 속 그림 조각들의 순서 무작위로 변경
            for order in picture:              ## 무작위로 변경된 순서대로, 즉 랜덤으로 그림 조각 하나씩 뽑혀 문제로 출제
                if order == 'a':               ## 문제로 출제될 그림 조각이 a일 경우, 수박의 첫번째 그림 조각이므로
                    from watermelon import QarrayScreen1 as QarrayScreen     ## watermelon 파일에서 문제로 출제할 QarrayScreen1 이라는 수박 그림 조각을 불러옴
                    QiScreen=Matrix(QarrayScreen)                            ## matrix 함수를 통해 행렬 형태로 바꾸어 QiScreen에 저장
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
                    from strawberry import QarrayScreen9 as QarrayScreen
                    QiScreen=Matrix(QarrayScreen)
                if order == 'j':
                    from strawberry import QarrayScreen10 as QarrayScreen
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

                QoScreen=Matrix(QiScreen)    ## matrix 함수를 통해 QiScreen을 행렬 형태로 바꾸어 QoScreen에 저장
                LED_init()                       ## LED에 불 들어오게 하는 함수 호출
                draw_matrix(QoScreen); print()               ## draw_matrix 함수를 호출하여 QoScreen을 출력, led matrix에 불이 들어오며 문제 화면이 출력됨
                time.sleep(10)                      ## 10초동안 문제화면 출력

                ## input
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
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]              #사용자의 답을 입력받을 AarrayScreen

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
                            score=score-1
                            LED_init()
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
                    score=score+2
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
                    from strawberry import QarrayScreen
                elif order == 'k' or order == 'l':
                    from heart import QarrayScreen
                elif order == 'm' or order == 'n' or order == 'o' or order == 'p'or order == 'q' or order == 'r':
                    from dog import QarrayScreen
                QiScreen=Matrix(QarrayScreen)
                QoScreen=Matrix(QiScreen)
                LED_init()
                draw_matrix(QoScreen); print()
                time.sleep(5)
                
            if (i==1)or(i==2):
                break
            
            if Q==1:
                break

#gallery_mode_exe()
