#!/usr/bin/env bash

rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y wine32 python-pip pyinstaller
wget httpswww.python.orgftppython2.7.14python-2.7.14.msi
wine msiexec i python-2.7.14.msi
sudo wine ~.winedrive_cPython27python.exe -m pip install requests==2.5.1
sudo pip install requests==2.5.1
