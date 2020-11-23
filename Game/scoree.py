from matrix import*
from original import*
from LED_display import*
from ScoreBlk import*

def Score(score):
    Scorescreen=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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


    Tenscore = score // 10
    Onescore = score % 10
    TenscoreBlk = Matrix(ScoreBlk(Tenscore))
    OnescoreBlk = Matrix(ScoreBlk(Onescore))
    
     # 숫자 출력 index 좌표값
    Tenscoretop = 4
    Onescoretop = 4
    Tenscoreleft = 8
    Onescoreleft = 14
    
    Scoreiscreen=Matrix(Scorescreen)
    Scoreoscreen=Matrix(Scoreiscreen)
    
    if Tenscore == 0:
       Onescoretop = 4
       Onescoreleft = 11
        
       tempBlk=Scoreiscreen.clip(Onescoretop,Onescoreleft,Onescoretop+OnescoreBlk.get_dy(),Onescoreleft+OnescoreBlk.get_dx())
       tempBlk=tempBlk+OnescoreBlk
       Scoreoscreen.paste(tempBlk,Onescoretop,Onescoreleft)
    
    
    else:
        tempBlk=Scoreiscreen.clip(Onescoretop,Onescoreleft,Onescoretop+OnescoreBlk.get_dy(),Onescoreleft+OnescoreBlk.get_dx())
        tempBlk=tempBlk+OnescoreBlk
        Scoreoscreen.paste(tempBlk,Onescoretop,Onescoreleft)
        tempBlk=Scoreiscreen.clip(Tenscoretop,Tenscoreleft,Tenscoretop+TenscoreBlk.get_dy(),Tenscoreleft+TenscoreBlk.get_dx())
        tempBlk=tempBlk+TenscoreBlk
        Scoreoscreen.paste(tempBlk,Tenscoretop,Tenscoreleft)

    LED_init() 
    draw_matrix(Scoreoscreen); print()
