from matrix import*
from original import*
import copy
from random import*
import time
from score import*

def memory_to():
      player=input("플레이어의 이름을 입력하세요 : ")  #사용자 이름 입력받는 변수 player생성
      QarrayScreen=[                                                                      #문제화면을 나타내는 QarrayScreen생성 
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
      
      lighton=[] #불이 들어올 칸들의 리스트 생성
      for i in range(20):
         num=randint(1,21)
         while True:
            if num in lighton:
               num=randint(1,21)    #21개의 칸 중 20개의 칸만 랜덤으로 선택
            else:
               break
         lighton.append(num)  #선택된 20개의 칸을 위에서 생성한 리스트에 추가
      red=lighton[:4]   #리스트의 맨 처음부터 4번째까지의 칸으로 빨간색 리스트 생성
      yellow=lighton[4:8]     #리스트의 5번째부터 8번째까지의 칸으로 노란색 리스트 생성
      green=lighton[8:12]     #리스트의 9번째부터 12번째까지의 칸으로 초록색 리스트 생성
      blue=lighton[12:16]     #리스트의 13번째부터 16번째까지의 칸으로 파란색 리스트 생성 
      pink=lighton[16:]       #리스트의 17번째부터 마지막까지의 칸으로 핑크색 리스트 생성
    
      arrayBlk=[[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,2,2,2]] #사용자가 컨트롤할 블럭 배열
      currBlk=Matrix(arrayBlk)      #사용자가 컨트롤할 블럭배열을 행렬형태로 만든 currBlk생성
      
      for i in lighton:       #오리지널 모드와 마찬가지로 각 칸에 알맞은 색상 설정하기
         top=2                      #추가된 것은 파란색(번호12)과 핑크색(번호20) 두가지 뿐임
         left=2                                #문제 화면 띄우는 아래 과정들은 오리지널 모드와 동일
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
      LED_init()
      draw_matrix(QoScreen); print()
      time.sleep(7)     #문제화면 7초간 보여주기
      start_time=time.time()  #사용자의 기록을 시간으로 보여주기 위해서 시작시간 받아놓기
      
      top=2
      left=2
      AarrayScreen=[                                                               #사용자의 입력을 받을 정답화면 AarrayScreen 생성
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

      AiScreen=Matrix(AarrayScreen)       #AarrayScreen을 행렬형태로 만든 AiScreen 생성
      AoScreen=Matrix(AiScreen)           #AiScreen을 행렬형태로 받은 AoScreen 생성
      tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx()) #AiScreen에서 잘라 사용자가 컨트롤하는 블럭이 LED matrix에 움직이는 걸 보여주기 위한 위치블럭 tempBlk생성   
      tempBlk=tempBlk+currBlk       #위치블럭tempBlk에 모양블럭currBlk을 붙여 최종 사용자가 컨트롤하는 블럭tempBlk 재생성
      AoScreen.paste(tempBlk,top,left)    #AoScreen에 tempBlk붙이기
      draw_matrix(AoScreen); print()      #최종적으로 블럭이 위치한 화면(AoScreen)을 LED matrix에서 보여주기
      hint=0      #시작할 때는 힌트를 사용하지 않은 상태여야하기에 0으로 초기화
      t1=None     #짝맞추기 게임은 두개를 오픈해서 두개가 같은지 틀린지 판단해야하기에 처음에 오픈하는 블럭의 top를 나타내는 변수 t1생성
      t2=None     #두번째로 오픈하는 블럭의 top를 나타내는 변수 t2생성
      l1=None     #처음에 오픈하는 블럭의 left를 나타내는 변수 l1생성
      l2=None     #두번째로 오픈하는 블럭의 left를 나타내는 변수 l2생성
      count=0     #몇 번 뒤집었는지 알려주는 변수 count생성
      while True:
         print('Direction : q(quit),a(left),d(right),s(down)')
         print('Open the card : o(open)')
         print('Finish : \' \'')
         print('Hint : h(hint)')
         key=input('Enter a key : ') #사용자로부터 키 값 입력받는 변수 key생성
         if key=='q':   # q 입력 시, 반복문을 빠져나가면서 게임종료
            print('Game terminated')
            break
         elif key=='a':       # a 입력 시, 컨트롤하는 블럭의 left를 4칸 왼쪽으로 이동, left가 2인 경우 즉, 컨트롤하는 블럭이 왼쪽 벽에 닿은 경우 더이상 이동하지 X
            if left==2:
               continue
            left-=4
            
         elif key=='d':       # d 입력 시, 컨트롤하는 블럭의 left를 4칸 오른쪽으로 이동, left가 26인 경우 즉, 컨트롤하는 블럭이 오른쪽 벽에 닿은 경우 더이상 이동하지 X
            if left==26:
               continue
            left+=4

         elif key=='s':       # s 입력 시, 컨트롤하는 블럭의 top를 4칸 아래쪽으로 이동, top가 10인 경우 즉, 컨트롤하는 블럭이 아래쪽 벽에 닿은 경우 더이상 이동하지 X
            if top==10:
               continue
            top+=4

         elif key=='w':       # w 입력 시, 컨트롤하는 블럭의 top를 4칸 위쪽으로 이동, top가 2인 경우 즉, 컨트롤하는 블럭이 위쪽 벽에 닿은 경우 더이상 이동하지 X
            if top==2:
               continue
            top-=4

         elif key=='o':          # o 입력 시, 해당 칸 오픈
            if AarrayScreen[top][left]!=0:      #이미 오픈되어있는 칸을 다시 오픈할 수는 없기에 이미 열린 칸에 오픈을 누를 시, 다시 선택하게함(이것은 count에 포함 안됨)
               continue 
            count+=1    #한 번 누를때 count는 1 증가함
            for a in range(top,top+currBlk.get_dy()):       
               for b in range(left,left+currBlk.get_dx()):
                  if count%2==1:    #count가 홀수이면 뒤집어야할 두 개 중 첫번째 것에 해당하므로 해당 블럭의 top를 t1에 left를 l1에 저장해줌
                     t1=top
                     l1=left
                  elif count%2==0:  #count가 짝수이면 뒤집어야할 두 개 중 두번째 것에 해당하므로 해당 블럭의 top를 t2에 left를 l2에 저장해줌
                     t2=top
                     l2=left
                  if(AarrayScreen[a][b]==0):    #칸을 뒤집었을 때, 문제화면에서의 동일위치 칸을 AarrayScreen으로 카피해옴 (그칸이 무슨 색이었는지 사용자에게 보여줘야하는거니까) 
                     AarrayScreen[a][b]=copy.deepcopy(QarrayScreen[a][b])
              
            if count%2==0 and count!=0 :  #count가 짝수이지만 0은 아닐때, 뒤집힌 두개의 칸 색상을 비교하고 같으면 그대로 놔두고 다르면 다시 뒤집기
               AiScreen=Matrix(AarrayScreen) 
               tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
               tempBlk=tempBlk+currBlk
               AoScreen=Matrix(AiScreen)
               AoScreen.paste(tempBlk,top, left)
               draw_matrix(AoScreen); print()
               time.sleep(1)  #두 칸의 색상이 서로 같은지 확인 (1초동안 사용자에게 보여줌)
               if AarrayScreen[t1][l1]!=AarrayScreen[t2][l2]:           #두개의 색상이 같다면 위에서 바꾼(QarrayScreen을 deepcopy해온)AarrayScreen을 그대로 사용 
                  for a in range(t1,t1+currBlk.get_dy()):                    #다르다면 다시 두칸의 AarrayScreen을 0으로 바꿔줌
                     for b in range(l1,l1+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
                  for a in range(t2,t2+currBlk.get_dy()):
                     for b in range(l2,l2+currBlk.get_dx()):
                        AarrayScreen[a][b]=0
         elif key=='h':       # h 입력 시, 문제화면을 4초동안 보여줌
            if hint==0:       #힌트는 한번만 사용가능하기에 한번도 사용안했을 때만 사용할 수 있음
                  draw_matrix(QoScreen);print()
                  time.sleep(4)
                  hint+=1     #사용했다는 표시로 hint에 1을 더해줌
            
         elif key==' ':       #스페이스바 입력 시, 사용자의 정답화면 제출
            break
         else:          #잘못된 키 입력 시, 다시 입력받음
            print("Wrong key!")
            continue
         AiScreen=Matrix(AarrayScreen)    #위에서 말한 것과 마찬가지로 사용자에게 컨트롤 블럭의 움직임과 키에 따른 스크린의 변화를 보여주는 과정임
         tempBlk=AiScreen.clip(top,left,top+currBlk.get_dy(),left+currBlk.get_dx())
         tempBlk=tempBlk+currBlk
         AoScreen=Matrix(AiScreen)
         AoScreen.paste(tempBlk,top, left)
         draw_matrix(AoScreen); print()

      end_time=time.time() #제출 완료 시, 끝나는 시간을 받아놓는 end_time변수 생성
      draw_matrix(AiScreen); print()
      i = 0       #성공, 실패를 확인하기 위한 변수 i 생성
      for a in range(2,14):   #모든 칸을 돌면서 문제화면과 사용자의 정답제출화면이 같은지 판단
         for b in range(2, 30):
               if QarrayScreen[a][b] != AarrayScreen[a][b]: #다르다면 실패문구를 출력하고 i=1이됨
                     print("Game over")
                     i=1
                     break
         if i==1:
            break #i=1일 시, 즉시 게임 종료
      
      if i==0:    #i=0이면 성공했다는 의미이므로 사용자의 기록 계산
         runtime=(end_time-start_time)//1       #사용자의 기록=끝나는 시간-시작 시간(소수점 떼기)
         runtime=int(runtime)       #사용자 기록을 정수형태로 변환해줌(Score함수에 인자로 주기 위함)
         f = open("짝맞추기1등.txt", 'r')      #짝맞추기 모드 1등 기록이 저장된 파일을 열어 1등기록 읽어오기      
         file = f.read()
         f.close()
         list = file.splitlines()
        
         for line in list:
             print("1등의 기록 : ", line)     #1등기록 화면에 출력
             line=int(line)   # 1등기록을 문자열형태에서 정수형으로 변환
             draw_matrix(Score(line))     #정수로 변환된 1등기록을 score파일의 Score함수에 인자로 전달하여 점수가 적힌 스크린을 받아오고, 그 스크린을 draw_matrix를 통해 LED matrix에 출력
             time.sleep(2)    #2초동안 보여주기
             print(player,"의 기록: ",runtime)     #사용자의 기록 화면에 출력
             draw_matrix(Score(runtime))  #사용자의 기록을 score파일의 Score함수에 인자로 전달하여 점수가 적힌 스크린을 받아오고, 그 스크린을 draw_matrix를 통해 LED matrix에 출력
             time.sleep(2)    #2초동안 보여주기
             if line>runtime:       #1등기록보다 사용자의 기록이 더 작다면 파일을 열어 1등기록 갱신
                print("축하드립니다. 신기록을 세우셨군요!!")
                f= open("짝맞추기1등.txt", 'w')
                line = f.write(str(runtime))
                print("새로운 1등 기록 : ",runtime)
             if line==runtime:
                print("축하드립니다. 공동 1등 입니다!")
         f.close()


