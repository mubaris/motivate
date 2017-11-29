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

echo "Do you want to get quotes during startup ? : "

select yn in "Yes" "No"; do
    case $yn in
        Yes ) cp Launch_screen_disp.py $INSTALLDIR/motivate/Launch_screen_disp.py; sed -i "s:python $INSTALLDIR/motivate/Launch_screen_disp.py::g  " ~/.xprofile ;echo "python $INSTALLDIR/motivate/Launch_screen_disp.py" >> ~/.xprofile;echo "Startup Quotes setup Successfully";break;;
        No ) exit;;
    esac
done
