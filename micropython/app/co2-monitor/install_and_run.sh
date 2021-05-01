#!/bin/bash

# PORT 番号が以下である前提
# WSL
# export AMPY_PORT=/dev/ttyUSB0
# Mac
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
# 以下に ampy が入った python 環境がある前提
source ../../../venv/bin/activate

ampy put main.py
ampy put settings.json
ampy put ambient.py
ampy put ntptime_custom.py
ampy put wifi.py

if [ $? != 0 ]; then
    echo "Installation failed."
    exit
fi

echo "Installation finishied."
echo "Start main.py"

ampy run main.py
