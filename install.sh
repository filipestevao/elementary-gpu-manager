#!/bin/bash

# Copy files to the user's directory
mkdir /home/$USER/.ElementaryGPUManager
cp *.py /home/$USER/.ElementaryGPUManager/
cp intel-nvidia-icon.png /home/$USER/.ElementaryGPUManager/
cp elementary-gpu-manager.desktop /home/$USER/.local/share/applications/
chmod +x /home/$USER/.ElementaryGPUManager/*.py
chmod +x /home/$USER/.local/share/applications/elementary-gpu-manager.desktop

# Install mesa-utils to use 'glxinfo' and 'glxgears'
sudo apt install -y mesa-utils

# Enable PPA
sudo apt install -y software-properties-common

# Install System76 PPA
sudo apt-add-repository -ys ppa:system76-dev/stable

# Update
sudo apt update

# Install System76 driver
sudo apt install -y system76-driver-nvidia

