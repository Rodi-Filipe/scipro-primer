# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:15:11 2021

@author: rodin
"""

class Account(object): 
    
    def __init__(self, name, account_number, initial_amount): 
        self.name = name 
        self.no = account_number 
        self.balance = initial_amount 
        self.transactions = 0
        
    def deposit(self, amount): 
        self.balance += amount 
        self.transactions += 1
        
    def withdraw(self, amount): 
        self.balance -= amount 
        self.transactions += 1
        
    def get_balance(self): 
        return self._balance
        
    def dump(self): 
        s = '%s, %s, balance: %s, number of transactions: %d' % \
            (self.name, self.no, self.balance, self.transactions)
        print(s) 

def test_Account():
    
    a1 = Account('John Olsson', '19371554951', 20000)
    a1.deposit(1000)
    a1.withdraw(250)
    
    expct1=20000+1000-250
    expct2=2
    
    assert a1.balance==expct1, '%d != to %d' %(a1.balance, expct1)
    assert a1.transactions==expct2, '%d != to %d' %(a1.transactions, expct2)
    
if __name__ == '__main__':
    test_Account()