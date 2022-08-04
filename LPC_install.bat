@echo on
winget install --id Git.Git -e --source winget 

winget install "Python 3.9"

git clone https://github.com/vands2013/install_test.git %CD%/LPC

cd LPC

python -m venv seven

.\seven\Scripts\activate && pip install ipython && ipython install.py