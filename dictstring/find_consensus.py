# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:31:04 2021

@author: rodin
"""

import numpy as np
import pprint

def find_consensus_v5(frequency_matrix):
    
    if isinstance(frequency_matrix,(list,tuple,np.ndarray)):
        if isinstance(frequency_matrix[0],(list,tuple,np.ndarray)):
            outputArg1 = find_consensus_v1(frequency_matrix)
        else:
            raise TypeError('Unsupported data structure type')
        
    elif isinstance(frequency_matrix,(list)) and isinstance(frequency_matrix[0],list):
         outputArg1 = find_consensus_v2(frequency_matrix)
    elif isinstance(frequency_matrix,dict) and isinstance(frequency_matrix[0],dict):
         outputArg1 = find_consensus_v3(frequency_matrix)
    else:
         raise TypeError('Unsupported data structure type')
   
    return outputArg1

def find_consensus_v1(frequency_matrix):
    
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    consensus = ''
    dna_length = len(frequency_matrix[0])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ATGC':
            if frequency_matrix[base2index[base]][i] > max_freq:
                max_freq = frequency_matrix[base2index[base]][i]
                max_freq_base = base
            elif frequency_matrix[base2index[base]][i] \
                     == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus


def find_consensus_v2(frequency_matrix):
    
    if isinstance(frequency_matrix, list) and \
       isinstance(frequency_matrix[0], list):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be list of lists')

    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    consensus = ''
    dna_length = len(frequency_matrix[0])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base2index[base]][i] > max_freq:
                max_freq = frequency_matrix[base2index[base]][i]
                max_freq_base = base
            elif frequency_matrix[base2index[base]][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus


def find_consensus_v3(frequency_matrix):
    
    if isinstance(frequency_matrix, dict) and \
       isinstance(frequency_matrix['A'], dict):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be dict of dicts')

    consensus = ''
    dna_length = len(frequency_matrix['A'])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base][i] > max_freq:
                max_freq = frequency_matrix[base][i]
                max_freq_base = base
            elif frequency_matrix[base][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus


inputArg1=[[2, 0, 2], [1, 2, 0], [0, 1, 0], [0, 0, 1]]

pprint.pprint(inputArg1)
pprint.pprint(find_consensus_v5(inputArg1))
