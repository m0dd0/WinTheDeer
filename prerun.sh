#!/bin/bash

cd /home/pi/JaegerSkript_Pi
echo "MAKIN SKRIPT EXECUTABLE"
sudo chmod +x jaegermesiter.py
echo "INSTALLING SELENIUM"
pip3 install selenium
echo "INSTALLING VIRTUALDISPLAY"
pip3 install pyvirtualdisplay
echo "INSTALLING CHROMEDRIVER"
sudo apt-get install chromium-chromedriver
# echo "INSTALLING CHROMIUM"
#sudo apt-get install chromium
echo "INSTALLING XVFB"
sudo apt-get install xvfb
echo "INSTALLINg TMUX"
sudo apt-get install tmux
echo "STARTING TMUX SESSION AND RUNNING SKRIPT"
tmux new-session "python3 jaegermesiter.py"
