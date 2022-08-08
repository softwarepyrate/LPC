#!/bin/bash

sudo apt-get update
sudp apt-get upgrade -y
sudo apt install python3-virtualenv
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.9
sudo apt install python3.9-distutils
sudo apt-get install python3.9-dev
sudo apt-get install python3.9-tk
git clone https://github.com/vands2013/install_test LPC
cd LPC
python3 -m virtualenv seven -p python3.9
source seven/bin/activate
python3 -m pip install ipython
#sudo python3 -m pip install -r requirements.txt
ipython install.py
#cp -R files_to_be_copied/workspace/ Tensorflow/