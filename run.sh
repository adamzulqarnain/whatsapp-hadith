#!/bin/sh

cd /home/pi/repo/whatsapp-hadith
git pull
python3 send.py > log.txt
