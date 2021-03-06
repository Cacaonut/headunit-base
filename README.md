# Headunit base system
## Features
* Media playback via USB and BT
* FM Radio
* OBD diagnostics from car
* Android Auto integration
## Requirements
### Hardware:
* Raspberry Pi 3 or better (Android Auto won't work fluently on RPI2, the rest might)
* Official RasPi touchscreen
* External Soundcard and BT adapter (for Android Auto)
* RTL-SDR dongle
* OBD2 Adapter
### Software:
* Raspbian OS based on Debian Wheezy
* Python3
## Installation
__Please note: These installation instructions are written mainly for my own purposes. However, with little customization of the code (e.g. changing the address of you obd2 adapter in main.py), you can get it running on your system as well. If you are in need of any assistance, feel free to open an issue.__

First build the following packages:  

aasdk: https://github.com/openDsh/aasdk  
OpenAuto: https://github.com/Cacaonut/openauto  
TCPBridge: https://github.com/Cacaonut/tcpbridge (using python3 setup.py install)  
bluetool: https://github.com/shoeffner/bluetool (using python3 setup.py install)

Then install it:
```
sudo apt-get -y install python3-pyqt5 python3-mutagen rtl-sdr libatlas-base-dev minicom python-serial
pip3 install pyrtlsdr numpy scipy matplotlib ipython jupyter pandas sympy nose rpi-backlight python-uinput

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
### Fixing bug that leads to sound cutting of on low volumes
Open the pulse audio config file:
```
sudo nano /etc/pulse/default.pa
```
Find the line starting with `load-module module-udev-detect` and append `ignore_dB=1`.
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
Open the lxsession autostart file:
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
Add the following line:
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
### Disable screen blanking
Open the start menu, then go to `Preferences`, then to `Raspberry Pi Configuration`. In there select `Display` from the top bar and disable `Screen Blanking`
### Disable mouse pointer
Open the LXDE configuration file:
```
sudo nano /etc/lightdm/lightdm.conf
```
Search for the line starting with `x-server-command`. Uncomment it and add `-nocursor` to the end of it.
### Change permission for uinput directory
Execute the following command:
```
sudo chmod 777 /dev/uinput
```
### Restart
__IMPORTANT: Don't forget to restart your Pi after making configuration changes!__
## Run
If you haven't configured autostart, you can run it manually.
```
python3 main.py
```
