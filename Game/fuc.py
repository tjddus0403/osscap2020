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
      if ('오른쪽' in stt):
        return 'd'
        break
      if ('아래' in stt):
        return 's'
        break
      if ('위로' in stt):
        return 'w'
        break
      if ('끝' in stt):
        return ' '
        break
      if ('빨강' in stt):
        return 'r'
        break
      if ('노랑' in stt):
        return 'y'
        break
      if ('초록' in stt):
        return 'g'
        break
      if ('지워' in stt):
        return 'e'
        break
      if ('열기' in stt):
        return 'o'
        break
      if ('힌트' in stt):
        return 'h'
        break
      if ('예' in stt):
        return 'Y'
        break
      if ('아니요' in stt):
        return 'N'
        break


