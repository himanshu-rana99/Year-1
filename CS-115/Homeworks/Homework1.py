'''
Created on Sep 12, 2017

@author: himanshu_rana99 - Himanshu Rana 

hrana2 
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import reduce 

def add(a, b):
    return a + b

"""The function takes the factorial of n similar to the factorial function in the math module"""
def factoiral(n):
   if n == 0:
       return 1
   else: 
       return n * factoiral(n-1)
        
print(factoiral(5))

"""The function computes the average of the given list"""
def mean(L):
    return reduce(add, L)/len(L)
    
print(mean([1, 2, 3]))
    
def divides(n):
    def div(k):
        return n % k == 0 
    return div

"""The function determines whether the given number is prime and returns true or false if the number is composite""" 
def prime(n):
     def div(k):
         return n % k == 0 
     lst = map(div, range(2, n))
     if True in lst: 
         return False 
     else: 
         return True 
     

print(prime(21))
print(prime(17))
