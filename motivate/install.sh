#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be with sudo" 1>&2
   exit 1
fi

INSTALLDIR="/opt/motivate"

# Create motivate folder
mkdir -p $INSTALLDIR

# Copy the datafolder and set permissions
cp -r $PWD/data $INSTALLDIR/
chmod -R 777 $INSTALLDIR/data

# Copy and link the executable
cp motivate.py $INSTALLDIR
ln -s $INSTALLDIR/motivate.py /usr/local/bin/motivate
