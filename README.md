# Headunit base system
## Features
> coming soon
## Requirements
### Hardware:
* Raspberry Pi 3 or better (Android Auto won't work fluently on RPI2, the rest might)
* External Soundcard and BT adapter (for Android Auto)
### Software:
* Raspbian OS based on Debian Wheezy
* Python3
## Installation
First build the following packages:  

aasdk: https://github.com/openDsh/aasdk  
OpenAuto: https://github.com/Cacaonut/openauto  
TCPBridge: https://github.com/Cacaonut/tcpbridge (using python3 setup.py install)  
bluetool: https://github.com/shoeffner/bluetool (using python3 setup.py install)

Then install it:
```
sudo apt-get -y install python3-pyqt5 python3-mutagen

git clone https://github.com/Cacaonut/headunit-base
```
## Run
```
python3 main.py
```
