from matrix import*
from original import*
from LED_display import*
scoreBlk = [[0, 0, 0, 0, 0, 0, 0, 0, 0],                    #scoreBlk초기화
            [0, 0, 0, 0, 0, 0, 0, 0, 0],        
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def ScoreBlk(num):
    global scoreBlk     #전역변수 scoreBlk사용하겠다는 의미
    if num == 0:        #전달받은 숫자num이 0인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 1:                  #전달받은 숫자num이 1인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [                
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
   
    elif num == 2:      #전달받은 숫자num이 2인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 3:      #전달받은 숫자num이 3인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 4:       #전달받은 숫자num이 4인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 5:      #전달받은 숫자num이 5인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 6:      #전달받은 숫자num이 6인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 7:      #전달받은 숫자num이 7인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 8:      #전달받은 숫자num이 8인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    elif num == 9:      #전달받은 숫자num이 9인 경우, 아래의 scoreBlk을 return 값으로 줌
        scoreBlk = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return scoreBlk
def Score(score):
    Scorescreen=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],             #점수를 나타낼 스크린 Scorescreen생성
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
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


    if (score<0)or(score>=100):         #받은 점수가 0보다 작거나 100 이상일 경우 아무 점수도 없는 화면 리턴(빈화면)
            return Matrix(Scorescreen)
    Tenscore = score // 10        #받은 점수의 십의자리 숫자를 저장한 변수 Tenscore생성            
    Onescore = score % 10           #받은 점수의 일의자리 숫자를 저장한 변수 Onescore생성
    TenscoreBlk = Matrix(ScoreBlk(Tenscore))    #Tenscore를 ScoreBlk함수에 인자로 전달해 해당 숫자에 맞는 scoreBlk을 리턴값으로 받고 이것을 행렬형태로 변환해 저장한 TenscoreBlk 생성
    OnescoreBlk = Matrix(ScoreBlk(Onescore))    #Onescore를 ScoreBlk함수에 인자로 전달해 해당 숫자에 맞는 scoreBlk을 리턴값으로 받고 이것을 행렬형태로 변환해 저장한 OnescoreBlk 생성
 
    Tenscoretop = 4     #십의 자리 숫자 블럭이 위치할 top의 값을 저장한 변수 Tenscoretop생성
    Onescoretop = 4     #일의 자리 숫자 블럭이 위치할 top의 값을 저장한 변수 Onescoretop생성
    Tenscoreleft = 8    #십의 자리 숫자 블럭이 위치할 left의 값을 저장한 변수 Tenscoreleft생성
    Onescoreleft = 16   #일의 자리 숫자 블럭이 위치할 left의 값을 저장한 변수 Onescoreleft생성
            
    Scoreiscreen=Matrix(Scorescreen)          #Scorescreen을 행렬형태로 받는 Scoreiscreen생성
    Scoreoscreen=Matrix(Scoreiscreen)          #Scoreiscreen을 행렬형태롤 받는 Scoreoscreen생성
   
    if Tenscore == 0:        #십의자리 숫자가 0 즉, 존재하지 않으면 일의자리 숫자만 나타내기에 일의자리 숫자 위치값이 달라짐
       Onescoretop = 4         #일의 자리 숫자 블럭이 위치할 top의 값을 4로 저장
       Onescoreleft = 11            #일의 자리 숫자 블럭이 위치할 left의 값을 11로 저장
        
       tempBlk=Scoreiscreen.clip(Onescoretop,Onescoreleft,Onescoretop+OnescoreBlk.get_dy(),Onescoreleft+OnescoreBlk.get_dx()) #Scoreiscreen을 잘라 일의 자리 숫자를 표현할 블럭의 위치를 나타내는 블럭 tempBlk생성      
       tempBlk=tempBlk+OnescoreBlk  #tempBlk에 OnescoreBlk을 더해 tempBlk 재생성
       Scoreoscreen.paste(tempBlk,Onescoretop,Onescoreleft) #Scoreoscreen에 tempBlk붙이기
    
    else:
        tempBlk=Scoreiscreen.clip(Onescoretop,Onescoreleft,Onescoretop+OnescoreBlk.get_dy(),Onescoreleft+OnescoreBlk.get_dx())#Scoreiscreen을 잘라 일의 자리 숫자를 표현할 블럭의 위치를 나타내는 블럭 tempBlk생성
        tempBlk=tempBlk+OnescoreBlk   #tempBlk에 OnescoreBlk을 더해 tempBlk 재생성
        Scoreoscreen.paste(tempBlk,Onescoretop,Onescoreleft)    #Scoreoscreen에 tempBlk붙이기
        tempBlk=Scoreiscreen.clip(Tenscoretop,Tenscoreleft,Tenscoretop+TenscoreBlk.get_dy(),Tenscoreleft+TenscoreBlk.get_dx())#Scoreiscreen을 잘라 십의 자리 숫자를 표현할 블럭의 위치를 나타내는 블럭 tempBlk생성
        tempBlk=tempBlk+TenscoreBlk #tempBlk에 TenscoreBlk을 더해 tempBlk 재생성
        Scoreoscreen.paste(tempBlk,Tenscoretop,Tenscoreleft)   #Scoreoscreen에 tempBlk붙이기
       
    return Scoreoscreen #점수를 표현하도록 최종 생성된 Scoreoscreen을 리턴해주기
