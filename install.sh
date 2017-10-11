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

if [ -e $HOME/.config/fish/config.fish ]
	then
	echo 'set PATH $PATH $HOME/.motivate' >> $HOME/.config/fish/config.fish
fi

if [ -e $HOME/.xonshrc ]
	then
	echo "\$PATH.append('$HOME/.motivate')" >> $HOME/.xonshrc
fi
