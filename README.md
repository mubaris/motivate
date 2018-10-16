# Motivate

[![Join the chat at https://gitter.im/pymotivate/Lobby](https://badges.gitter.im/pymotivate/Lobby.svg)](https://gitter.im/pymotivate/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Motivate](motivate.png)

<br/>

A simple script to print random motivational quotes. Highly influenced by linux command [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)).

## Features
* Colored Output
* Supports `bash` and `zsh`

## Requirements

```
git
python 3x
```

## Installation

### Linux/MacOS

```
$ git clone https://github.com/mubaris/motivate.git
$ cd motivate/motivate
$ sudo ./install.sh
$ source ~/.bashrc
```

zsh users should replace `.bashrc` with `.zshrc`.

If you have no root priviledge, install in this way:
```
$ git clone https://github.com/mubaris/motivate.git
$ cd motivate
$ ln -s $PWD/motivate/motivate.py moti
$ ln -s $PWD/dummy.sh mmoti

$ export PATH=$PWD:$PATH
$ # echo 'export PATH=$PWD:$PATH' >> ~/.bashrc

```
Later you can run by calling `moti` (a single run) or `mmoti` (keep running until you break it).
After doing so, I found that python 2.x is enough to run this script.

### Windows

* Make sure you have Python3 on your path.
* Clone the repository `git clone https://github.com/mubaris/motivate.git`.
* Add the path to your local clone to your system path.
* Run `py -3 motivate.py` from the command prompt.

## Update Database

```
$ git clone https://github.com/mubaris/motivate.git
$ cd motivate
$ ./UPDATE
```

## Usage

```
$ motivate

"When something is important enough, you do it even if the odds are not in your favor."
		--Elon Musk
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).
