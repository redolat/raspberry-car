#!/bin/sh
# install.sh

sudo apt update
sudo apt install git
git clone https://github.com/redolat/raspberry-car.git
sudo apt install python3-flask
sudo apt install python3-gpiozero
#pip install RPi.GPIO

mkdir -p logs
chmod 755 /home/pi/raspberry-car/launcher.sh

(sudo crontab -l; echo "@reboot sh /home/pi/raspberry-car/launcher.sh >/home/pi/logs/cronlog 2>&1") | sudo crontab -

sh /home/pi/raspberry-car/launcher.sh
