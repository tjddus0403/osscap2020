import gspeech2
import time

def voice():
  gsp = gspeech2.Gspeech()
  while Ture:
      stt = gsp.getText()
      if stt is None:
         break
      print(stt)
      time.sleep(0.01)
      if ('좌' in stt):
        return 'a'
        break
      if ('우' in stt):
        return 'd'
        break
      if ('하' in stt):
        return 's'
        break
      if ('끝' in stt):
        return ' '
        break
      if ('빨강' in stt):
        return 'r'
        break
      if ('노랑' in stt):
        return 'o'
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

key=voice()
print(key)


