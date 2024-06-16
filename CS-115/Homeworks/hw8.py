'''
Created on Oct 29, 2017

@author: hrana2 - Himanshu Rana 
"I pledge my honor that I have abided by the Stevens Honor System" 
'''
#helper functions 
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': 
        return 0 
    if s[-1] == '1':
        return  2 * binaryToNum(s[:-1]) + 1
    return  2 * binaryToNum(s[:-1])

def numToBaseB(N, B):
    '''This function takes in a non-negative number and a base between 
    2 and 10. It will convert the number into the given base. If the number 
    is zero then zero will be outputed'''
    if N == 0: 
        return "0"
    if B > 10 or B < 2: 
        return ''
    else: 
        if N // B == 0: 
            return str(N % B)
        return numToBaseB(N // B, B) + str(N % B)
 
    
def baseBToNum(S, B):
    '''This function takes in a string of numbers and a base between 
    2 and 10. Then it will convert the string into the number in the 
    given base. If an empty string is given, then zero will be outputed''' 
    if S == '': 
        return 0
    return B * baseBToNum(S[:-1], B) + int(S[-1])

def add(S, T):
    '''This function takes in two strings of binary numbers. 
    It will add the two numbers together and print out the answer in binary'''
    number1 = baseBToNum(S, 2)
    number2 = baseBToNum(T, 2)
    sum = number1 + number2
    return numToBaseB(sum, 2)



def TcToNum(S):
    '''This function takes in a string of 8 bits of binary. This string represents 
    the two's complement of a decimal number. The function will convert the two's 
    complement number into it's decimal number. '''
    if S[0] != '1': 
        return binaryToNum(S)
    def helper(S):
        if S == '': 
            return ''
        if S[0] == '1': 
            return '0' + helper(S[1:])
        return '1' + helper(S[1:])
    return -1 * binaryToNum(add(helper(S), '1'))
 
 #helper function   
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.''' 
    if n == 0: 
        return ''
    if n % 2 == 1: 
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'   
    
 
def NumToTc(N):
    '''This function takes in a decimal number and will find the two's complement 
    of that number up to 8 bits. Also making sure that, if necessary, there are 
    leading zeros to satisfy the 8 bit condition.'''
    if N > 127 or N < -128: 
        return 'Error' 
   
    def padded(S):
        return (8 - len(S)) * '0' + S
    if N >= 0: 
        return padded(numToBinary(N))
    pos_num = padded(numToBinary(-1 * N))
    
    def helper(S):
        if S == '': 
            return ''
        if S[0] == '1': 
            return '0' + helper(S[1:])
        return '1' + helper(S[1:])
        
    neg_num = padded(add(helper(pos_num), '1'))
    neg_num = '1' + neg_num[1:]
    return neg_num


    
  
  

