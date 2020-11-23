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
      elif ('우' in stt):
        return 'd'
      elif ('하' in stt):
        return 's'
      elif ('끝' in stt):
        return ' '
      elif ('빨강' in stt):
        return 'r'
      elif ('노랑' in stt):
        return 'o'
      elif ('초록' in stt):
        return 'g'
      elif ('지워' in stt):
        return 'e'
      elif ('열기' in stt):
        return 'o'
      elif ('힌트' in stt):
        return 'h'

key=voice()
print(key)


