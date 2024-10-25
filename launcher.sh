#!/bin/sh
# launcher.sh

nohup python3 /home/pi/raspberry-car/app.py 2>&1 > "/home/pi/logs/raspberry-car.out" &
