from match import*    #각 모드의 게임파일들을 가져오기
from original import*
from gallery import*
from piano import*
from stt import*

while True:    
   print("MODE")        #사용자로부터 모드 입력받기
   print("1. Original \n2. Matching \n3. Gallery \n4. Piano \n5. Voice \n6. Turn off")
   choice=int(input("Select the Mode : "))
   if choice==1:     
      memory_key()   #original파일에 있는 오리지널 모드 게임 함수 실행
      break

   elif choice==2:
      memory_to()    #match파일에 있는 matching모드 게임 함수 실행
      break

   elif choice==3:
      gallery_mode_exe()   #gallery파일에 있는 갤러리모드 게임 함수 실행
      break

   elif choice==4:      
      memory_piano()    #piano파일에 있는 피아노모드 게임 함수 실행
      break
      
   elif choice==5:
      memory_voice()    #stt파일에 있는 voice 모드 게임 함수 실행
      break
      
   elif choice==6:
      break    #6입력 시, 게임기 종료 
      
   else:
      print("잘못된 번호를 입력하셨습니다.") #잘못된 번호 입력시 다시 입력받음 
      continue
