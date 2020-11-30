Memory_Game
==============================================================================
    LED Matrix 텍스트 출력: https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/samples

    LED Matrix와 파이썬 코드 연결:  https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/experimental-python-code

    라즈베리파이와 피에조 부저 연결: https://projects.raspberrypi.org/en/projects/physical-computing/8

    피에조 부저 소리 : http://naver.me/G196bN7C

    Google stt : https://cloud.google.com/speech-to-text/docs/endless-streaming-tutorial?hl=ko
==============================================================================

1. USB 마이크를 라즈베리 파이에 연결
-------------------------------------------------------------------------------
1. arecord -l 명령어로 마이크의 카드와 디바이스 번호를 확인합니다.

    .. code-block:: bash

        $ arecord -l

.. image:: https://user-images.githubusercontent.com/70687128/100592909-172f6080-333b-11eb-8428-7aaa5acc0a20.PNG

2. 위와 같이 표시되었다면, .asoundrc 파일을 아래와 같이 편집한다. 

    .. code-block:: bash

        $ pcm.!default {
            type asym
            capture.pcm "mic"
            playback.pcm "speaker"
          }
          pcm.mic {
            type plug
            slave {
              pcm "hw:<card number>,<device number>"
            }
          }
          pcm.speaker {
            type plug
            slave {
              pcm "hw:1,0"
            }
          }

위 예시의 경우 card 2, device 0 이므로 pcm.mic 안에 pcm "hw:2, 0"으로 적는다.

3. 설정을 저장하고 라즈베리파이를 재부팅한다.

    .. code-block:: bash

        $ sudo reboot
        
4. 다음 명령어를 통해 소리를 조절할 수 있다.

    .. code-block:: bash

        $ alsamixer
-------------------------------------------------------------------------------
　
　

2. Pyaudio 설치
-------------------------------------------------------------------------------

1. Pyaudio를 설치한다.

    .. code-block:: bash
   
        $ sudo apt-get install python3-dev
        $ sudo apt install portaudio19-dev
        $ sudo pip3 install pyaudio
        
2. 정상적으로 설치가 되지 않을 경우 아래 링크에 접속하여 자신의 machine 버전에 맞는 whl 파일을 다운한다.

 https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

3. 다운받은 파일을 설치한다.

    .. code-block:: bash
   
        $ pip install "파일이름"

전반적인 과정을 참고할 수 있을 것 같다 : https://blog.naver.com/rose1216_/221319294390
        
　
 　
3. 빠른 시작: 클라이언트 라이브러리 사용
-------------------------------------------------------------------------------

1. Cloud Console 프로젝트를 설정합니다.
https://console.cloud.google.com/에서 프로젝트를 만들거나 선택합니다.
프로젝트에 Cloud Speech-to-Text API를 사용 설정합니다.
서비스 계정을 만듭니다.
비공개 키를 JSON으로 다운로드합니다.

2. GOOGLE_APPLICATION_CREDENTIALS 환경 변수를 서비스 계정 키가 포함된 JSON 파일의 경로로 설정합니다. 이 변수는 현재 셸 세션에만 적용되므로, 새 세션을 열 경우, 변수를 다시 설정합니다.

[PATH]를 서비스 계정 키가 포함된 JSON 파일의 경로로 바꿉니다.

    .. code-block:: bash
   
        $ export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
        
        
3. Google SDK 설치 및 초기화 <- 4. Google Cloud SDK 설치 참고

4. 클라이언트 라이브러리 설치

    .. code-block:: bash
   
        $ pip install --upgrade google-cloud-speech
        

더 많은 안내는 https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-install-python를 참고합니다.

　

4. Google Cloud SDK 설치
-------------------------------------------------------------------------------

1. Cloud SDK에는 Python이 필요합니다. 지원되는 버전은 3.5~3.8 및 2.7.9 이상입니다.
   
    .. code-block:: bash
   
        $ python --version

2. 다음 중 하나를 다운로드합니다.

    Linux 64비트(x86_64) : google-cloud-sdk-318.0.0-linux-x86_64.tar.gz  /  
    Linux 32비트(x86) : google-cloud-sdk-318.0.0-linux-x86.tar.gz
    
    
3. 또는 명령줄에서 Linux 64비트 보관 파일을 다운로드하려면 다음을 실행합니다.

    .. code-block:: bash
   
        $ curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-318.0.0-linux-x86_64.tar.gz
        
   32비트 보관 파일의 경우 다음을 실행합니다.
   
    .. code-block:: bash
   
        $ curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-318.0.0-linux-x86.tar.gz
     
4. 원하는 파일 시스템 위치에 파일 콘텐츠 압축을 풉니다. 기존 설치를 대체하려면 기존 google-cloud-sdk 디렉터리를 삭제하고 동일한 위치에 보관 파일 압축을 풉니다.

5. 선택사항입니다. 설치 스크립트를 사용하여 경로에 Cloud SDK 도구를 추가합니다. 또한 셸 및 사용 통계 수집을 위한 명령어 완료 옵션을 선택할 수 있습니다. 이 명령어를 사용하여 스크립트를 실행합니다.

    .. code-block:: bash
   
        $ ./google-cloud-sdk/install.sh
      
6. gcloud init을 실행하여 SDK를 초기화합니다.

    .. code-block:: bash
   
        $ ./google-cloud-sdk/bin/gcloud init
        
        
더 많은 안내는 https://cloud.google.com/sdk/docs/install#linux를 참고합니다.

　
 　
5. Google Cloud Speech API Python Samples
-------------------------------------------------------------------------------

.. image:: https://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=speech/microphone/README.rst


This directory contains samples for Google Cloud Speech API. The `Google Cloud Speech API`_ enables easy integration of Google speech recognition technologies into developer applications. Send audio and receive a text transcription from the Cloud Speech API service.

- See the `migration guide`_ for information about migrating to Python client library v0.27.

.. _migration guide: https://cloud.google.com/speech/docs/python-client-migration




.. _Google Cloud Speech API: https://cloud.google.com/speech/docs/

Setup
-------------------------------------------------------------------------------


Authentication
++++++++++++++

This sample requires you to have authentication setup. Refer to the
`Authentication Getting Started Guide`_ for instructions on setting up
credentials for applications.

.. _Authentication Getting Started Guide:
    https://cloud.google.com/docs/authentication/getting-started

Install Dependencies
++++++++++++++++++++

#. Clone python-docs-samples and change directory to the sample directory you want to use.

    .. code-block:: bash

        $ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

#. Install `pip`_ and `virtualenv`_ if you do not already have them. You may want to refer to the `Python Development Environment Setup Guide`_ for Google Cloud Platform for instructions.

   .. _Python Development Environment Setup Guide:
       https://cloud.google.com/python/setup

#. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

    .. code-block:: bash

        $ virtualenv env
        $ source env/bin/activate

#. Install the dependencies needed to run the samples.

    .. code-block:: bash

        $ pip install -r requirements.txt

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/



The client library
-------------------------------------------------------------------------------

This sample uses the `Google Cloud Client Library for Python`_.
You can read the documentation for more details on API usage and use GitHub
to `browse the source`_ and  `report issues`_.

.. _Google Cloud Client Library for Python:
    https://googlecloudplatform.github.io/google-cloud-python/
.. _browse the source:
    https://github.com/GoogleCloudPlatform/google-cloud-python
.. _report issues:
    https://github.com/GoogleCloudPlatform/google-cloud-python/issues


.. _Google Cloud SDK: https://cloud.google.com/sdk/
-------------------------------------------------------------------------------






