#! /bin/bash

# Create virtual environment if it not exist
if [ ! -d menv ]
then
    virtualenv -p python3 menv
fi

# Source virtual environment
source menv/bin/activate

# Install python requirements from requirements
pip install -r requirements.txt

# Deactivate virtual environment
deactivate
