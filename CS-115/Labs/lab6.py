'''
Created on: October 12, 2017
@author:    hrana2 - Himanshu Rana 
Pledge:     "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Lab 6
'''
'''The complete base-2 representation of the number 42 is 00101010'''
'''If a base-10 number is odd then the rightmost bit will be a 1. If the number 
    is even the the lest-significant bit will be a 0'''
'''By eliminating the least-significant bit we are basically dividing 
    the original number by 2'''
'''By already knowing the base-2 representation of Y, if N is odd then
   the base-2 number of N is Y plus a 1 at the end. If N is even then base-2 
   of N is Y plus a 0 at the end'''
'''The ternary representation of 59 is 2012 because when you do 59 % 3 you get 2 
   and then you keep doing that until you get the ternary number'''
 
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''  
    if n % 2 == 1: 
        return True 
    return False

print(isOdd(42))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.''' 
    if n == 0: 
        return ''
    if isOdd(n): 
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'
    
print(numToBinary(11))
    

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': 
        return 0 
    if s[-1] == '1':
        return  2 * binaryToNum(s[:-1]) + 1
    return  2 * binaryToNum(s[:-1])

 
print(binaryToNum('100'))

  

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111': 
        return '00000000'
    int_val = binaryToNum(s) + 1
    bin_val = numToBinary(int_val)
    lead_zero = 8 - len(bin_val)
    return (lead_zero * '0') + (bin_val)

print(increment('100'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0: 
        print(s)
    else: 
        print(s)
        return count(increment(s), n - 1)
        

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0: 
        return ''
    elif n % 3 == 0: 
        return numToTernary(n // 3) + '0'
    elif n % 3 == 1: 
        return numToTernary(n // 3) + '1'
    elif n % 3 == 2: 
        return numToTernary(n // 3) + '2'

print(numToTernary(10))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '': 
        return 0 
    return 3 * ternaryToNum(s[:-1]) + int(s[-1])
