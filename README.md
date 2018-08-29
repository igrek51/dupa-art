# Dupa GitHub Tiles Art
Magnum opus among the art of Dupa

A Python script creates commits in the past with a specific date. These commits are composing a pattern on GitHub contribution activity tiles.

![alt tag](https://github.com/igrek51/dupa-art/blob/master/wiki/dupa-github-igrek51.png)

## Let's make the Art
Set the pattern and a start date in `dupaart.py` file and simply run:
```bash
python dupaart.py
```
You may need to install `future` module before:
```bash
apt install python-pip # (for Debian)
pip install future
```

## Testing
Running tests on both Python 2 and 3:
```bash
pip2 install future pytest coverage mock
pip3 install future pytest coverage mock
./pytest23.sh
```
