# About

A simplified fork of https://github.com/xpgeng/advanced_freeq

For a list of PDF files in the current directory, outputs word_occurrences.csv containing the word frequency occurrence of all words found in word_list.csv

## Download

Use Python 3.4+ to get the lastest version of advanced_freeq

```
$ git clone https://github.com/joemclo/advanced_freeq.git
```

Decorator packages are required for advanced_freeq.py.

```
$ pip install docopt pdfminer.six numpy pandas
```

### OS X

If you're on Mac OS X, The `sed` will return some error when use `sed -i`, you should use [`Homebrew`](http://brew.sh/) download `gnu-sed` to replace default `sed`.

```
$ brew install gnu-sed --with-default-names
```

Install Calibre

```
$ brew cask install calibre
```

### Debian

```
$ sudo apt-get install calibre
```

## Usage

```
$ ./advanced_freeq.py


## Thanks to

@[Enaunimes](https://github.com/Enaunimes/freeq); 12dicts word list: <http://wordlist.aspell.net/12dicts-readme/>

lemmas.txt is derrived from 2+2+3lem.txt in version 6 of 12dicts word
list.

```
