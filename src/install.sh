
#! /bin/bash

# Create virtual environment if does not exists
if [ ! -d menv ] 
then
    virtualenv -p python3 menv
fi

# Source virtual environment
source venv/bin/activate

# Install python requirements from requirements 
pip install -r requirements.txt

# Deactivate virtual environment
deactivate