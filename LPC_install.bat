@echo on

git clone https://github.com/vands2013/install_test.git %CD%/LPC

cd LPC

pip install virtualenv

python -m virtualenv seven --python=python3.9.13

:: python -m venv seven

.\seven\Scripts\activate && pip install ipython && ipython install.py