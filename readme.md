## install and get into virtual enviroment first 
python3 -m venv venv 
source venv/bin/activate

## install python stuff since im on mac 
pip install pycryptodomex
pip install pycryptodome-test-vectors
python -m Cryptodome.SelfTest

## get into the virtual environment at any time 
source venv/bin/activate

## to run just do this 
python3 python.py

## and to leave it just 
deactivate

## heres the doucmentation I followed: 
https://www.pycryptodome.org/src/installation
https://www.pycryptodome.org/src/cipher/classic