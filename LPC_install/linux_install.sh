#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
#python3 -m pip install --upgrade pip
sudo apt install python3-pip --upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9 -y
sudo apt install python3.9-venv -y
sudo apt install python3.9-distutils -y
sudo apt install python3.9-dev -y
sudo apt install python3.9-tk -y
#cd ..
python3.9 -m venv seven
source seven/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install pycocotools==2.0.4
pip install opencv-python==4.5.5.64
pip install wget
pip install ipython
pip install easyocr==1.5.0
ipython install.py
#cp -R files_to_be_copied/workspace/ Tensorflow/
