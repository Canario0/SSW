#! /bin/bash

# Load virtual environment
source menv/bin/activate

# Run Flask application
export FLASK_APP=main.py
flask run

deactivate
