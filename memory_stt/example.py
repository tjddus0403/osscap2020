# -*- coding: utf-8 -*-
import gspeech
import time
def main():
    gsp = gspeech.Gspeech()
    while True:
        # 음성 인식 될때까지 대기 한다.
        stt = gsp.getText()
        if stt is None:
            break
        print(stt)
        time.sleep(0.01)
        if ('끝내자' in stt):
            break


if __name__ == '__main__':
    main()

