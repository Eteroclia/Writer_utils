#!/bin/bash
if ! test -d venv; then
    echo "Creating virtual environment"
    python3 -m venv venv
    echo "Done"
fi
source venv/bin/activate
python3 ./splitter.py
