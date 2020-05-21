#!/bin/bash

# PORT 番号が以下である前提
export AMPY_PORT=/dev/ttyUSB0
# 以下に ampy が入った python 環境がある前提
source ../../venv/bin/activate

ampy put main.py
ampy put settings.json
ampy put ambient.py
ampy put ntptime_custom.py

if [ $? != 0 ]; then
    exit
fi

echo "Installation finishied."
echo "Start main.py"

ampy run main.py
