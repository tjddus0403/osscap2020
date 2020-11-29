from matrix import*  
from random import*
import time
import LED_display as LMD
import threading
from score import*

def LED_init():     #LED에 불 들어오게 하기 위한 함수(threading)
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):     #원하는대로 matrix를 그리기 위한 함수
      array=m.get_array()
      for y in range (m.get_dy()):
         for x in range(m.get_dx()):
            if array[y][x]==0:
               LMD.set_pixel(x,y,0)
            elif array[y][x]==1:   #white(테두리)
               LMD.set_pixel(x,y,7)
            elif array[y][x]==2:  #skyblue (컨트롤하는 블록의 색상)
               LMD.set_pixel(x,y,6)
            elif array[y][x]==3:  #yellow (설치되는 노란색 블록)
               LMD.set_pixel(x,y,3)
            elif array[y][x]==4: #red  (설치되는 빨간색 블록)
               LMD.set_pixel(x,y,1)
            elif array[y][x]==7:   #green  (설치되는 초록색 블록)
               LMD.set_pixel(x,y,2)
            elif array[y][x]==12:   #blue  (설치되는 파란색 블록)
               LMD.set_pixel(x,y,4)
            elif array[y][x]==20:   #pink  (설치되는 핑크색 블록)
               LMD.set_pixel(x,y,5)
            else:        #white(겹칠 때 즉, 컨트롤하는 블록이 이동한 위치에 이미 설치된 블록이 있으면 설치된 상태라는 것을 하얀색 블록을 통해 알려줌)
               LMD.set_pixel(x,y,7)
         print()
def memory_key(): #기억력 게임 original ver 게임 내용을 담은 함수
      player=input("사용자 이름을 입력하세요 : ")  #플레이어의 정보(이름) 받기
      arrayBlk=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]   #플레이어가 컨트롤하는 블록 설정
      currBlk=Matrix(arrayBlk)   # 위에서 정한 컨트롤할 블록을 매트릭스 형태로 변환
      i=0   # 성공해서 다음단계로 넘어가는 것인지(i=0), 실패해서 다시 시작하는 것인지(i=1), 실패해서 게임을 종료하는 것인지(i=2) 구분하기 위한 변수i 설정
      success=0  #스코어를 누적하는 변수 success 설정
      level = int(input("난이도 easy는 1, hard는 2를 입력하세요: "))  #사용자로부터 난이도를 level이라는 변수에 입력받기
      while True:
         if i==1:
            success=0
            print("게임을 다시 시작합니다.")
         elif i==2:
            print("게임을 종료합니다.")
            break
         while True:
      #문제 화면 출력하기
            i=0 #게임을 다시 시작하게 되더라도 여기서 i=0으로 바뀌기 때문에, 처음 상태로 초기화 되어 플레이 할 수 있음
            QarrayScreen=[                                                         #문제 화면을 출력할 2차원 배열 QarrayScreen 설정
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],       #총 블럭의 갯수는 7*3=21개
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

            if level == 1:               #level이 easy일 때의 문제 화면 출력 과정
               lighton=sample(list(range(1,22)),7)   #21개의 칸 중 불을 킬 7개의 칸 랜덤으로 정하기
            
               for i in lighton:
                  top=2     #첫번째 줄의 top위치
                  left=2
                  if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):      #첫 줄에 있는 7개의 칸들 중 불이 들어와야한다면, 
                     left=left+(i-1)*4       #첫번째 줄의 left위치                       #해당 블록의 숫자를 3으로 바꿔 LED에 노란색 불로 켜지게 하기                     
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3         
                  elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):       #두번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=6      #두번째 줄의 top위치
                     left=left+(i-8)*4  #두번째 줄의 left위치
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
                  elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):         #세번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
                     top=10     #세번째 줄의 top위치
                     left=left+(i-15)*4     #세번째 줄의 left위치
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           QarrayScreen[a][b]=3
               
            if level == 2:             #level이 hard일 때의 문제 화면 출력 과정
               lighton=sample(list(range(1,22)),8)  #21개의 칸 중 불을 킬 8개의 칸 랜덤으로 정하기
               red=lighton[:3]      #뽑은 리스트 중 맨 앞 세 개는 빨간색
               yellow=lighton[3:5]      #중간 두 개는 노란색
               green=lighton[5:]        #맨 마지막 세 개는 초록색이 됨

               for i in lighton:
                  top=2
                  left=2
                  if ((i==1)or(i==2)or(i==3)or(i==4)or(i==5)or(i==6)or(i==7)):  #easy모드와 비슷하지만, hard모드는 첫 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 
                     left=left+(i-1)*4                                                     # 해당 블록의 숫자를 4,3,7으로 바꿔 LED에 빨간색, 노란색, 초록색 불로 켜지게 하기
                     for a in range(top,top+currBlk.get_dy()):
                        for b in range(left,left+currBlk.get_dx()):
                           if i in red:
                              QarrayScreen[a][b]=4
                           elif i in yellow:
                              QarrayScreen[a][b]=3
                           elif i in green:
                              QarrayScreen[a][b]=7
                  elif ((i==8)or(i==9)or(i==10)or(i==11)or(i==12)or(i==13)or(i==14)):   #두번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
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
                  elif ((i==15)or(i==16)or(i==17)or(i==18)or(i==19)or(i==20)or(i==21)):     #세번째 줄에 있는 7개의 칸들 중 불이 들어와야 할 때, 위와 동일
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

            QiScreen=Matrix(QarrayScreen)   #문제화면(QarrayScreen)을 행렬형태로 바꾼 QiScreen설정
            QoScreen=Matrix(QiScreen)       #QiScreen을 또 행렬형태로 바꾼 QoScreen설정
            LED_init()      #LED판에 불이 들어오게 하기 (threading문제가 생길 수 있으므로 한 번만 해줄 것)
            draw_matrix(QoScreen); print()      #draw_matrix함수를 이용해 QoScreen을 LED matrix에 그리기
            time.sleep(7)       #그린 상태로 7초간 사용자에게 보여주기
            
            #input
            top=2
            left=2
            AarrayScreen=[                                                               #사용자의 답을 입력받을 AarrayScreen생성
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

            AiScreen=Matrix(AarrayScreen)       #AarrayScreen을 행렬형태로 바꾼 AiScreen 생성
            AoScreen=Matrix(AiScreen)       #마찬가지로 AiScreen을 행렬형태로 받은 AoScreen생성
          #  currBlk=Matrix(arrayBlk)    
            tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())  #원하는 위치로 블럭을 옮기기 위해 원하는 위치의 칸을 AiScreen에서 잘라서 tempBlk생성
            tempBlk=tempBlk+currBlk        #currBlk의 형태를 가진 tempBlk재생성
            AoScreen.paste(tempBlk,top,left)    #tempBlk을 AoScreen에 붙여주기
            draw_matrix(AoScreen); print()      #최종적으로 블럭이 옮겨진 화면(AoScreen)을 LED matrix에서 보여주기
            hint=0  #처음엔 힌트를 안사용했으므로 0으로 초기화
            
            while True:     #키를 계속 사용해 움직여야하기에 무한루프 생성

               print('Direction : q(quit), a(left), d(right), s(down)')     #키에 대한 설명
               print('Fix the color block : r(red), y(yellow), g(green)')
               print('Erase the block : e(erase)')
               print('Hint : h(hint)')
               print('Finish : \' \'')
               key=input('Enter a key : ')      #사용자로부터 키 값 받기
               if key=='q':
                  print('Game terminated')
                  break     #q 선택 시, while문을 탈출하며 게임 종료
               elif key=='a':       
                  if left==2:      # a 선택 시, 컨트롤하는 블럭의 left위치를 4만큼 왼쪽으로 이동/ 만약 left가 2 즉, 왼쪽 벽에 붙은 상태라면 더이상 이동하지 X
                     continue
                  left-=4
               elif key=='d':   
                  if left==26:      # d 선택 시, 컨트롤하는 블럭의 left위치를 4만큼 오른쪽으로 이동/ 만약 left가 26 즉, 오른쪽 벽에 붙은 상태라면 더이상 이동하지 X
                     continue
                  left+=4
               elif key=='s':       
                  if top==10:       # s 선택 시, 컨트롤하는 블럭의 top위치를 4만큼 아래로 이동/ 만약 top이 10 즉, 아래 벽에 붙은 상태라면 더이상 이동하지 X
                     continue
                  top+=4
               elif key=='w':
                  if top==2:        # w 선택 시, 컨트롤하는 블럭의 top위치를 4만큼 위로 이동/ 만약 top이 2 즉, 위쪽 벽에 붙은 상태라면 더이상 이동하지 X
                     continue
                  top-=4
               elif key=='y':           # y 선택 시, AarrayScreen에서 해당 칸들의 색상을 노란색으로 바꿈(각 칸의 숫자를 노란색을 가리키는 3으로 바꿔줌)
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==7):
                           AarrayScreen[a][b]=3
                           continue
                        elif AarrayScreen[a][b]==3:     #해당 칸이 이미 노란색인 상태에서 y를 한번 더 누를 경우 색상이 없어짐(취소)
                           AarrayScreen[a][b]=0
                           continue
                
               elif key=='r':        # r 선택 시, AarrayScreen에서 해당 칸들의 색상을 빨간색으로 바꿈(각 칸의 숫자를 노란색을 가리키는 4으로 바꿔줌)
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==3)or(AarrayScreen[a][b]==7):
                           AarrayScreen[a][b]=4
                           continue
                        elif AarrayScreen[a][b]==4:     #해당 칸이 이미 빨간색인 상태에서 r을 한번 더 누를 경우 색상이 없어짐(취소)
                           AarrayScreen[a][b]=0
                           continue
               
               elif key=='g':       # g 선택 시, AarrayScreen에서 해당 칸들의 색상을 초록색으로 바꿈(각 칸의 숫자를 초록색을 가리키는 7으로 바꿔줌)
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        if (AarrayScreen[a][b]==0)or(AarrayScreen[a][b]==4)or(AarrayScreen[a][b]==3):
                           AarrayScreen[a][b]=7
                           continue
                        elif AarrayScreen[a][b]==7:     #해당 칸이 이미 초록색인 상태에서 g를 한번 더 누를 경우 색상이 없어짐(취소)
                           AarrayScreen[a][b]=0
                           continue
                        
               elif key=='e':       # e 선택 시, 해당 칸의 색상을 없애줌(각 칸의 숫자를 빈 상태를 나타내는 0으로 바꿔줌)(지우기)
                  for a in range(top,top+currBlk.get_dy()):
                     for b in range(left,left+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
               
               elif key=='h':      # h 선택 시, 힌트 사용
                  if hint==0:   #힌트를 한번도 사용하지 않은 상태라면, 힌트 사용가능 (두번은 사용할 수 X)
                        success-=1      # 성공 점수에서 1점 깎임
                        draw_matrix(QoScreen);print()   # 문제화면을 LED matrix에 3초간 보여줌
                        time.sleep(3)
                        hint+=1     #힌트를 사용했다는 표시
                  
               elif key==' ':   #스페이스를 선택 시, 사용자의 정답 화면 제출
                  break
               else:       # 다른 키 입력 시, 잘못 선택했음을 알려주고 다시 선택하게 함
                  print('Wrong key!')
                  continue

               AiScreen=Matrix(AarrayScreen)    #아래의 과정은 위 키들을 한번씩 입력할 때마다 그것을 화면에 바로바로 보여주기 위한 코드임
                                                                              #위에서 설명한 LED matrix에 화면을 보여주는 코드와 내용 동일
               tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk

               AoScreen = Matrix(AiScreen)
               AoScreen.paste(tempBlk, top, left)
               draw_matrix(AoScreen); print()

            draw_matrix(AiScreen); print()  #최종으로 사용자가 제출한 답안 화면을 LED matrix에 보여줌

            #input_output_corfirm
            i = 0   #성공, 실패를 구분하기 위한 변수 i 생성
            for a in range(2,14):       #LED matrix의 모든 칸을 돌면서 QarrayScreen과 AarrayScreen이 동일한지 판단 
                  for b in range(2,30):
                        if QarrayScreen[a][b] != AarrayScreen[a][b]:
                            print("실패하셨습니다.")       #틀리다면 실패문구 출력
                            thehalgguenya = input("게임을 다시 시작하시겠습니까? (Y/N): ")  #게임을 다시 할 것인지 사용자로부터 입력받음
                            if thehalgguenya == "Y":        # 다시 한다면 i=1이 됨
                                i = 1
                                break
                            elif thehalgguenya == "N":      # 그만 한다면 i=2가 됨
                                i = 2
                                break
                  if (i==1)or(i==2):
                        break
         
            if i == 0:  #성공했다면 i에 변화가 없기에 그대로 0일 것임 
               print("success")
               success+=2   #성공 점수에 2점을 추가하고 다음 문제로 게임 계속 진행
               continue
                               
            elif (i==1)or(i==2):    #실패했다면 다시 시작하는 것의 유무와 상관없이 점수를 출력해줌 (1등의 점수, 사용자의 점수 순서대로 출력됨 (점수는 익명)->펀치기계같은 점수관리)
               if level==1:     #easy모드라면, easy모드 1등의 점수가 적힌 파일을 열어서 1등 점수 읽어오기
                   f = open("오리지널easy_1등.txt", 'r') 
                   file = f.read()
                   f.close()
                   ls = file.splitlines()
               elif level==2:      #hard모드라면, hard모드 1등 점수가 적힌 파일을 열어서 1등 점수 읽어오기
                   f=open("오리지널hard_1등.txt",'r')
                   file=f.read()
                   f.close()
                   ls=file.splitlines()
               for line in ls:      
                   print("1등의 기록 : ", line) #1등의 기록 출력
                   line=int(line)   #1등의 기록을 숫자형태로 바꾼후 
                   draw_matrix(Score(line)) #score 파일에 있는 Score함수에 인자로 넣어서 그 리턴값으로 1등 점수가 적힌 스크린 받아온 후, 그것을 draw_matrix함수를 통해 LED matrix에 표현 
                   time.sleep(2)    #2초동안 보여줌
                   print(player,"의 기록: ",success)   #마찬가지로 사용자의 기록 출력
                   draw_matrix(Score(success))  #위와 동일한 방식으로 사용자의 기록을 LED matrix에 2초간 출력
                   time.sleep(2)
                   if float(line)<success:  #만약 사용자 기록이 1등의 기록보다 높다면, 해당 모드의 파일 열어서 사용자의 기록으로 1등 기록 갱신
                       print("축하드립니다. 신기록을 세우셨군요!!")
                       if level==1:
                           f= open("오리지널easy_1등.txt", 'w')
                           line = f.write(str(success))
                           print("새로운 1등 기록 : ",success)
                           f.close()
                       elif level==2:
                           f= open("오리지널hard_1등.txt", 'w')
                           line = f.write(str(success))
                           print("새로운 1등 기록 : ",success)
                           f.close()
               break
      
