#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be with sudo" 1>&2
   exit 1
fi

INSTALLDIR="/opt/motivate"

# Create motivate folder
mkdir -p $INSTALLDIR

# Copy the datafolder and set permissions
cp -r "$PWD"/data $INSTALLDIR/data
chmod -R 777 $INSTALLDIR/data

# Copy and link the executable for one time motivate
cp motivate.py $INSTALLDIR/motivate.py
ln -s $INSTALLDIR/motivate.py /usr/local/bin/motivate

# Copy and link the shell script for the perpetual motivate
cp pmotivate.sh $INSTALLDIR/pmotivate.sh
ln -s $INSTALLDIR/pmotivate.sh /usr/local/bin/pmotivate