# -*- coding: utf-8 -*-

import gspeech2
import time
def exam():
    gsp = gspeech2.Gspeech()
    while True:
        # 음성 인식 될때까지 대기 한다.
        stt = gsp.getText()
        if stt is None:
            break
        print(stt)
        time.sleep(0.01)
        if ('끝' in stt):
            return 'a'
            break


a = exam()
print(a)

