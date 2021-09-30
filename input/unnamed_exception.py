# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:16:12 2021

@author: rodin
"""

import sys
try:
    C = float(sys.argv[1])
except IndexError: 
    print('C must be provided as command-line argument')
    sys.exit(1)