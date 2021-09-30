# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:17:01 2021

@author: rodin
"""

from collections import defaultdict

def get_base_counts2(dna):
    
    counts = defaultdict(int)
    
    for base in dna:
        counts[base] +=1
    return counts

def test_get_base_counts2():
    
    dna = 'ADLSTTLLD'
    
    expct={'A': 1, 'D': 2, 'L': 3, 'S': 1, 'T': 2}
    result=get_base_counts2(dna)
    
    assert expct==result, '%s != to %s' %(expct,result)

test_get_base_counts2()

