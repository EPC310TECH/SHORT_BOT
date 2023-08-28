#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages from requirements.txt
pip install numpy
pip install -r requirements.txt

echo "Installation complete. Activate the virtual environment using 'source venv/bin/activate'."

