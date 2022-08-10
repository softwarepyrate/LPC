##########################################################
# Version 1.0 - Matt
#
# Version 2.1 - Chen - removed "%CD%/.." line
#
##########################################################

@echo on

cd LPC

pip install virtualenv

python -m virtualenv seven --python=python3.9.13

:: python -m venv seven

.\seven\Scripts\activate && pip install ipython && ipython install.py