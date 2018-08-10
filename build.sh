#!/bin/bash

python3 setup.py sdist bdist_wheel
cp -f dist/django-storage-swift-epfl-0.1.tar.gz install/
