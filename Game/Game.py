from match import*
from original import*
from gallery import*
from LED_display import*
while True:
   print("MODE")
   print("1. Original \n 2. Matching \n 3. Gallery \n 4. Turn off")
   choice=int(input("Select the Mode : "))
   if choice==1:
      memory_key()
      continue
   elif choice==2:
      memory_to()
      continue
   elif choice==3:
      gallery_mode_exe()
      continue
   elif choice==4:
      break
   else:
      continue
