#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y
sudo apt install software-properties-common
sudo apt-get install python3-pip
python3 -m pip install --upgrade pip
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.9 -y
sudo pip3 install virtualenv
sudo apt install python3.9-distutils -y
sudo apt-get install python3.9-dev -y
sudo apt-get install python3.9-tk -y
git clone https://github.com/vands2013/install_test LPC && cd LPC
python3 -m virtualenv seven -p python3.9
source seven/bin/activate
pip install requests
pip install pycotools
pip install wget
pip install easyocr
python3 -m pip install ipython
ipython install.py
#cp -R files_to_be_copied/workspace/ Tensorflow/