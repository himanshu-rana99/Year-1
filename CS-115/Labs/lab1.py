'''
Created on Sep 7, 2017

@author: himanshu_rana99
Himanshu Rana 
I pledge my honor that I have abided by the rules of the Stevens Honor System 
'''

from cs115 import map, reduce, range
import math

#The function returns the summation of a and b 
def add(a, b):
    return a + b

#The function returns the reciprocal of n 
def inverse(n):
    return 1 / n

#The function tries to evaluate the math number e by using Taylor expansion 
def e(n):
    return reduce(add, (map(inverse, map(math.factorial, range(n + 1)))))
#The function returns the absolute value of the difference between the true value of e and e(n)
def error(n):
    return abs(math.e - e(n))






    