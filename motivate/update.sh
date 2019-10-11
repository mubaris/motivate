#!/bin/bash

INSTALLDIR="/opt/motivate"

rm -rf $HOME/.motivate/data/*
cp -r $PWD/data $INSTALLDIR/

chmod -R 777 $INSTALLDIR/data
