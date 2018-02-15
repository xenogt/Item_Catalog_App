#! /usr/bin/python

import os
import sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, THIS_FOLDER)

from project import app as application