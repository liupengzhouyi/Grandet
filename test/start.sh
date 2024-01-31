#!/bin/bash

cp -r ./src/* ./test 
python -m unittest discover -s ./test  -p 'test_*.py' --verbose