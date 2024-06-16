'''
Created on Sep 13, 2017

@author: himanshu_rana99 - Himanshu Rana 
hrana2 
"I pledge my honor that I have abided by the Stevens Honor System"
'''


"""This function takes the dot product of two vectors or lists. Dot product is the sum of the products of the elements in the same position"""
def dot(L, K):
    if L == [] or K == []: 
        return 0.0 
    return L[0] * K[0] + (dot(L[1:], K[1:]))
    
print(dot([5,3], [6,4]))

"""This function takes a string S as input and returns a list of the characters in that string"""
def explode(S):
     if S == '':
        return []
     return [S[0]] + explode(S[1:])
 
print(explode('spam'))

"""This function takes an element and a sequence and finds the first instance(index) of the element in the sequence"""
def ind(e, L):
    if L == "" or L == []:
        return 0
    elif e == L[0]: 
        return 0 
    return 1 + ind(e, L[1:])
        
print(ind(42, [55, 77, 42, 12, 42, 100]))

"""This function takes in an element and a sequence and removes all the elements in that sequence"""
def removeAll(e, L):
    if L == []: 
        return [] 
    if e == L[0]: 
        return removeAll(e, L[1:]) 
    return [L[0]] + removeAll(e, L[1:])
print(removeAll(42, [55, 77, 42, 11, 42, 88]))

"""The myFilter function acts just like the built-in filter. It keeps all the elements that are true and removes those that are false"""
def myFilter(f, L):
    if L == []: 
        return []
    elif  f(L[0]): 
        return [L[0]] + myFilter(f, L[1:])
    return myFilter(f, L[1:])
     
"""This function takes a list of elements and returns the reversal of the list"""
def deepReverse(lst):
    if lst == []: 
        return []
    elif isinstance(lst[0], list): 
        return deepReverse(lst[1:]) + [deepReverse(lst[0])]
    return deepReverse(lst[1:]) + [lst[0]] 

print(deepReverse([1,[2,3], 4]))
    