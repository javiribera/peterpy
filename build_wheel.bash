#!/bin/bash

python setup.py bdist_wheel
mv dist/*.whl .
rm -R build dist print_time.egg-info
rm -R __pycache__

echo 'DONE'


