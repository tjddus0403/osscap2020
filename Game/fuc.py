import gspeech2
import time
import copy

def voice():
  #gspeech2 파일에서 음성입력 -> 텍스트 변환 하는 함수를 가져옴
  gsp = gspeech2.Gspeech()
  while True:
      stt = gsp.getText()
      # 입력값이 올 때까지 대기
      if stt is None:
         break
      # 인식한 텍스트를 보여줌
      print(stt)
      time.sleep(0.01)
      # 입력키 값에 대응하는 텍스트가 입력되면 해당 키 값을 반환하고 음성입력을 중단한다.
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


