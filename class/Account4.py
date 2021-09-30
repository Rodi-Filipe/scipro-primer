# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:08:34 2021

@author: rodin
"""

class Account(object): 
    
    def __init__(self, name, account_number, initial_amount): 
        
        self.name = name 
        self.no = account_number 
        self.balance = initial_amount 
        
    def __iadd__(self, amount): 
        
        self.balance += amount 
        
        return self
        
    def __isub__(self, amount): 
        
        self.balance -= amount
        
        return self
    
    def __str__(self):
        
        return 'Name: %s, Acc No: %s, Balance: %s' %(self.name, self.no, self.balance)
    
    def __repr__(self):
        
        return 'Account( %s )' % self
    
    def dump(self): 
        
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance) 
        print(s)

def test_Account():
    
    name='rodi'
    account_number='029493847'
    initial_amount=800000
    deposit=20000
    withdraw=40000
    
    
    a1=Account(name,account_number,initial_amount)
    a1+=deposit
    a1-=withdraw
    expct=initial_amount+deposit-withdraw
    s='Name: %s, Acc No: %s, Balance: %s' %(name,account_number,expct)
    
    assert abs(expct-a1.balance) <1E-5, 'Test failed!, %s != to %s' %(expct, a1.balance)
    assert s==str(a1), 'Test failed!, %s !=to  %s' %(s,str(a1))

if __name__ == '__main__':
    
    test_Account()