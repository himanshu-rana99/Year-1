'''
Created on Oct 23, 2017

@author: hrana2 - Himanshu Rana 
"I pledge my honor that I have abided by the Stevens Honor System" 
'''

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
    
print(numToBaseB(4, 2))  
print(numToBaseB(0, 4))  
    
def baseBToNum(S, B):
    '''This function takes in a string of numbers and a base between 
    2 and 10. Then it will convert the string into the number in the 
    given base. If an empty string is given, then zero will be outputed''' 
    if S == '': 
        return 0
    return B * baseBToNum(S[:-1], B) + int(S[-1])

print(baseBToNum('11', 2))


def baseToBase(B1, B2, SinB1):
    '''This function takes in two bases between two and ten and a string 
    that is in the first base. The function will convert the string from 
    the first base into the corresponding number in the second base'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

print(baseToBase(2, 10, "11"))

def add(S, T):
    '''This function takes in two strings of binary numbers. 
    It will add the two numbers together and print out the answer in binary'''
    number1 = baseBToNum(S, 2)
    number2 = baseBToNum(T, 2)
    sum = number1 + number2
    return numToBaseB(sum, 2)

print(add("11", "01"))

def addB(S, T):
    '''This function is similar to the add function, however, this one 
    accounts for the length of the two inputed numbers. It does this by 
    checking the both rightmost digits and seeing if they are both zero 
    and adding zero to the string. If one of the rightmost digits is zero 
    then the other has to be one and adds one to the string'''
    if S == '': 
        return T 
    if T == '': 
        return S 
    elif S[-1] == '0' and T[-1] == '0': 
        return addB(S[:-1], T[:-1]) + '0'
    elif S[-1] == '0' or T[-1] == '0': 
        return addB(S[:-1], T[:-1]) + '1'
    return addB(addB(S[:-1], '1'), T[:-1]) + '0'
    
print(addB('011', '100'))
    
