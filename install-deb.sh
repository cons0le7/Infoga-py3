#!/bin/bash

echo "Updating Package List..."
sudo apt-get update 
echo "Installing Python3..."
sudo apt-get install -y python3 
echo "Installing pip..."
sudo apt-get install -y python3-pip 
echo "Installing dependencies..."
pip3 install requests  
echo "Installation complete."
