# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:35:44 2021

@author: rodin
"""
from datetime import datetime
from scitools import pprint2

class AccountP(object):
    
    tempvar=False
    def __init__(self, name, account_number, initial_amount): 
       
        AccountP.tempvar = True
        self._name = name 
        self._no = account_number 
        self._balance = initial_amount
        self._transactions = []
    
    def deposit(self, amount): 
        self._balance += amount 
        self._transactions.append({'Amount': '+%d' % amount, \
                                  'Date & Time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        
    def withdraw(self, amount): 
        self._balance -= amount 
        self._transactions.append({'Amount': '-%d' % amount, \
                                  'Date & Time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    
    def get_balance(self): 
        return sum(float(transct['Amount']) for transct in self._transactions)
    
    def print_transactions(self):
        pprint2.pprint(self._transactions)
    
    def dump(self): 
        s = '%s, %s, balance: %s, number of transacations: %d' % \
            (self._name, self._no, self._balance,len(self._transactions)) 
        print(s)