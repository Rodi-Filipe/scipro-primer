# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:19:55 2021

@author: rodin
"""

def count_pairs(dna,pair):
    
    boolvec=[]
    dna_list=list(dna)
    r=len(pair)
    tempvar=[j for j in range(len(dna)) if dna[j]==pair[0]]
    for i in range(len(tempvar)):
        boolvec.append(pair==''.join(dna_list[tempvar[i]:tempvar[i]+r]))
    
    return sum(boolvec)
        

print(count_pairs('ACGTTACGGAACG','C'))

