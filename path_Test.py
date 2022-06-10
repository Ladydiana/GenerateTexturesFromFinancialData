# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:15:50 2022

@author: Ballerina
"""

import os
import sys

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(user_paths)
#print("sys.path: "+ sys.path)