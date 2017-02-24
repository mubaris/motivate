#!/bin/bash

mkdir -p $HOME/.motivate/data

cp motivate.py $HOME/.motivate/motivate

cp -r $PWD/data/ $HOME/.motivate

chmod +x $HOME/.motivate/motivate

echo 'export PATH=$PATH:$HOME/.motivate' >> $HOME/.bashrc

if [ -e $HOME/.zshrc ]
	then
	echo 'export PATH=$PATH:$HOME/.motivate' >> $HOME/.zshrc
fi