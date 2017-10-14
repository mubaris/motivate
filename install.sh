#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be with sudo" 1>&2
   exit 1
fi

HOMEDIR="/home/"$SUDO_USER

# Create motivate folder
mkdir -p $HOMEDIR/.motivate

# Symlink the json datafolder
ln -sf $PWD/data/ $HOMEDIR/.motivate/data

# Copy the executable
cp motivate.py /usr/local/bin/motivate
