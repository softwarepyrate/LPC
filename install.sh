#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common
python3 -m pip install --upgrade pip
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9 -y
sudo apt install python3.9-venv
#sudo pip3 install virtualenv
sudo apt install python3.9-distutils -y
sudo apt-get install python3.9-dev -y
sudo apt-get install python3.9-tk -y
git clone https://github.com/vands2013/install_test LPC && cd LPC
#python3 -m virtualenv seven -p python3.9
python3.9 -m venv seven
source seven/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
#pip install requests
#python3 -m pip install --upgrade pip
pip install pycocotools==2.0.4
pip install opencv-python==4.5.5.64
pip install wget
#pip install -r requirements.txt
pip install ipython
pip install easyocr==1.5.0
ipython install.py
cp -R files_to_be_copied/workspace/ Tensorflow/
