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
sudo apt-get -y install python3-pyqt5 python3-mutagen rtl-sdr libatlas-base-dev
pip3 install pyrtlsdr numpy scipy matplotlib ipython jupyter pandas sympy nose rpi-backlight

git clone https://github.com/Cacaonut/headunit-base
```
## Configuration
### Allowing screen brightness adjustments
```
echo 'SUBSYSTEM=="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"' | sudo tee -a /etc/udev/rules.d/backlight-permissions.rules
```
### Enabling Bluetooth audio streaming
Open the bluealsa configuration file:
```
sudo nano /lib/systemd/system/bluealsa.service
```
Edit the line starting with `ExecStart` and edit it to match below:
```
ExecStart=/usr/bin/bluealsa -p a2dp-sink
```
### Changing device name
Create a file called `machine-info`:
```
sudo nano /etc/machine-info
```
Fill it with the following content:
```
PRETTY_HOSTNAME=[device name]
```
### Configure autostart
__IMPORTANT: After these changes you won't be able to control the Pi from the desktop environment any more. Therefore enable SSH and change the admin password for security reasons.__ 
Open the lxsession autostart file:
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
Replace its content with the following line:
```
@/usr/bin/python3 /home/pi/headunit-base/main.py
```
### Disable bootup messages
Open the boot cmdline file:
```
sudo nano /boot/cmdline.txt
```
Change `console=tty1` to `console=tty3` and add `logo.nologo loglevel=3 vt.global_cursor_default=0`.
### Change splash screen
Open the boot config file:
```
sudo nano /boot/config.txt
```
Add the following line to disable the gpu test resolving in a rainbow screen:
```
disable_splash=1
```
Create a custom image matching your screen size and copy it the the following location:
```
sudo cp ~/my_splash.png /usr/share/plymouth/themes/pix/splash.png
```
### Restart
__IMPORTANT: Don't forget to restart your Pi after making configuration changes!__
## Run
```
python3 main.py
```
