# Motivate

[![Join the chat at https://gitter.im/motivate-new/community](https://gitter.im/motivate-new/community.svg)](https://gitter.im/motivate-new/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Motivate](motivate.png)

<br/>

A simple script to print random motivational quotes. Highly influenced by linux command [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)).

## Motivate-new
As previous repo is not maintained now, but there are a lot of people who want to contribute, I've decided to fork and continue the project. This would be active and would be maintained by me. PRs are welcome :tada:.

- Feel free to open an issue for **bugs** or **feature request**.
- Add more quotes referencing this [issue](https://github.com/avats-dev/motivate/issues/1).
- Use the new [gitter community](https://gitter.im/motivate-new/community) to chat and communicate. 

Thanks :heart:

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
$ git clone https://github.com/avats-dev/motivate.git
$ cd motivate/motivate
$ sudo ./install.sh
$ source ~/.bashrc
```

zsh users should replace `.bashrc` with `.zshrc`.

If you have no root priviledge, install in this way:
```
$ git clone https://github.com/avats-dev/motivate.git
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
* Clone the repository `git clone https://github.com/avats-dev/motivate.git`.
* Add the path to your local clone to your system path.
* Run `py -3 motivate.py` from the command prompt.

## Update Database

```
$ git clone https://github.com/avats-dev/motivate.git
$ cd motivate
$ ./UPDATE
```

## Usage

```
$ motivate

"When something is important enough, you do it even if the odds are not in your favor."
		--Elon Musk
```

## Contribution
The most popular way to contribute is adding [new quotes](https://github.com/avats-dev/motivate/issues/1). You do it by adding next JSON file in `motivate/data/` directory. The rule is 10 quotes per file.

Before you submit your new JSON file, it is helpful to validate your file at this [website](https://jsonlint.com/) to make sure it is formatted correctly.

Bug reports and new feature ideas are welcome, open a new issue.

You're also welcome to discuss the idea on [Gitter Chat](https://gitter.im/motivate-new/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge).
