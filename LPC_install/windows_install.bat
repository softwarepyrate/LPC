::=================================================================================
::Version 1.0 - Matt
::
::Version 2.1 - Chen - removed "%CD%/.." line
::
::Version 2.2 - Chen - Updated version control format, add wget package in line 18 
::
::=================================================================================

@echo on

cd LPC

pip install virtualenv

python -m virtualenv seven --python=python3.9.13

.\seven\Scripts\activate && pip install ipython wget && ipython install.py