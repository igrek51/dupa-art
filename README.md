# Dupa GitHub Tiles Art
This is a picture generator on GitHub activity tiles.

A Python script creates commits in the past with a specific date. These commits are composing a pattern on GitHub contribution activity tiles.
Here's the example:

[![igrek51 GitHub Tiles](https://github.com/igrek51/dupa-art/blob/master/wiki/dupa-github-igrek51.png)](https://github.com/igrek51?tab=overview&from=2015-12-01&to=2015-12-31)

## Let's make the Art
Set your `secret_art` pattern and `first_day` date in `dupaart.py` file:
```python
"""
Tiles pattern made out of single days:
Sun 
Mon DD  U U PP   A 
Tue D D U U P P A A
Wed D D U U PP  AAA
Thu D D U U P   A A
Fri DD  UUU P   A A
Sat
Week123456789012345 - 15 weeks = 105 days < 4 months
"""
secret_art = [
	'               ',
	'DD  U U PP   A ',
	'D D U U P P A A',
	'D D U U PP  AAA',
	'D D U U P   A A',
	'DD  UUU P   A A',
	'               '
]

first_day = '2015-01-04'
```

Install dependencies:
```bash
pip3 install -r requirements.txt
```
and just run:
```bash
python3 dupaart.py
```

## Testing
Running tests on Python 3:
```bash
pip3 install future pytest coverage mock
./pytest.sh
```
