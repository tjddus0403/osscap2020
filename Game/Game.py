from match import*
from original import*
from gallery import*
from piano import*
from stt import*

while True:
   print("MODE")
   print("1. Original \n2. Matching \n3. Gallery \n4. Piano \n5. Voice \n6. Turn off")
   choice=int(input("Select the Mode : "))
   if choice==1:
      memory_key()
      break

   elif choice==2:
      memory_to()
      break

   elif choice==3:
      gallery_mode_exe()
      break

   elif choice==4:
      memory_piano()
      break
      
   elif choice==5:
      memory_voice()
      break
      
   elif choice==6:
      break 
      
   else:
      print("잘못된 번호를 입력하셨습니다.")
      continue
