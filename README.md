# Dupa GitHub Tiles Art
This is a picture generator on GitHub activity tiles.

A Python script creates commits in the past with a specific date. These commits are composing a pattern on GitHub contribution activity tiles.
Here's the example:

[![igrek51 GitHub Tiles](https://github.com/igrek51/dupa-art/blob/master/wiki/dupa-github-igrek51.png)](https://github.com/igrek51?tab=overview&from=2015-12-01&to=2015-12-31)

## Let's make the Art
Set the pattern and a date in `dupaart.py` file:
```python
secretArt = [
	'               ',
	'DD  U U PP   A ',
	'D D U U P P A A',
	'D D U U PP  AAA',
	'D D U U P   A A',
	'DD  UUU P   A A',
	'               '
]

firstDay = '2015-01-04'
```

After that, just run:
```bash
python dupaart.py
```
You may need to install `future` module before:
```bash
apt install python-pip # for Debian
pip install future
```

## Testing
Running tests on both Python 2 and 3:
```bash
pip2 install future pytest coverage mock
pip3 install future pytest coverage mock
./pytest23.sh
```
