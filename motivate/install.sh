#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be with sudo" 1>&2
   exit 1
fi

INSTALLDIR="/usr/local/share"

# Create motivate folder
mkdir -p $INSTALLDIR/motivate

# Symlink the json datafolder
ln -sf $PWD/data/ $INSTALLDIR/motivate/data

# Copy the executable
cp motivate.py /usr/local/bin/motivate
