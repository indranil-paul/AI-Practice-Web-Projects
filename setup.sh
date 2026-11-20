#!/bin/bash

set -e

PYTHON_VERSION="3.14.5"
VENV_NAME=".venv"

echo
echo "==========================================="
echo "        FastAPI Project Setup"
echo "==========================================="
echo

if command -v pyenv >/dev/null 2>&1; then
    echo "Installing Python ${PYTHON_VERSION} (if needed)..."
    pyenv install -s ${PYTHON_VERSION}
    pyenv local ${PYTHON_VERSION}
fi

echo
echo "Creating virtual environment..."
python -m venv ${VENV_NAME}

echo
echo "Activating virtual environment..."
source ${VENV_NAME}/bin/activate

echo
echo "Upgrading pip..."
python -m pip install --upgrade pip

echo
echo "Installing packages..."
pip install -r requirements.txt

echo
echo "==========================================="
echo "        Setup Completed Successfully"
echo "==========================================="
echo
echo "Activate the virtual environment using: source ${VENV_NAME}/bin/activate"
echo
