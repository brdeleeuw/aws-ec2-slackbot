#!/bin/sh 

# This script automates the configuration of an already launched EC2 instance
# First, adjust the desired packages, directories, repos etc. to install below 
# Then copy this file to the remote instance (e.g. by using Filezilla) 
# Run it by typing `sh ec2-config.sh` in the command line


## Installing/Updating Python and necessary package managers ##
sudo apt-get update --yes
sudo apt install python-pip --yes
sudo apt install python3-pip --yes

## Generating/enabling correct locales ##
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo locale-gen --purge en_US.UTF-8
export LC_ALL=C

## Installing desired (Python) packages ##
pip3 install pandas
pip3 install numpy
pip3 install scipy
pip3 install sklearn
pip3 install tqdm

## Setting up your directories ##
mkdir src
cd src

## Use git clone to clone a project directly into the your instance, otherwise use Filezilla to transfer projects ##
git clone -b <branch> https://<git-username>@<repo link>.git

## Continue setting up your desired directory structure ##
mkdir dirname
cd ~/src/dirname/....

exit 0 