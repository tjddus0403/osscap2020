import gspeech2
import time

import copy

def voice():
  gsp = gspeech2.Gspeech()
  while True:
      stt = gsp.getText()
      if stt is None:
         break
      print(stt)
      time.sleep(0.01)
      if ('왼쪽' in stt):
        return 'a'
        break


a = voice()
print(a)
