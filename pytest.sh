#!/bin/bash
MODULE_NAME=dupaart

echo 'pytest + coverage: Python 3...'
python3 -m coverage run --source ${MODULE_NAME} -m pytest -v || exit 1
# show code coverage info
python3 -m coverage report -m
