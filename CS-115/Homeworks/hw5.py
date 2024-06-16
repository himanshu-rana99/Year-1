'''
Created on: October 6, 2017
@author:    hrana2 - Himanshu Rana 
Pledge:     "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    '''This function creates a fractal, image that it repeated when
     zoomed into, of a tree using turtle graphics'''
    if levels == 0:
        return 
        turtle.done()
    else: 
        turtle.color("brown")
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree(trunk_length / 2, levels -1 )
        turtle.color("green")
        turtle.right(90)
        sv_tree(trunk_length / 2, levels - 1)
        turtle.left(45)
        turtle.backward(trunk_length)
 
   
           
   
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_lucas_helper(n, memo):
        if n in memo: 
            return memo[n]
        if n == 0: 
            result = 2
        elif n == 1: 
            result = n 
        else: 
            result = fast_lucas_helper(n - 1, memo) + fast_lucas_helper(n - 2 , memo)
            
        memo[n] = result 
        return result
    
    return fast_lucas_helper(n, {})

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo: 
            return memo[(amount, coins)]
        
        if amount == 0: 
            result = 0
            memo[(amount, coins)] = result 
            return result
        if coins == (): 
            result = float('inf')
            memo[(amount, coins)] = result 
            return result 
        if coins[0] > amount: 
            result = fast_change_helper(amount, tuple(coins[1:]), memo)
            memo[(amount, coins)] = result 
            return result
        
        use_it = fast_change_helper(amount - coins[0], tuple(coins), memo)
        lose_it = fast_change_helper(amount, tuple(coins[1:]), memo)
        
        if use_it + 1 < lose_it: 
            result = use_it + 1
        else: 
            result = lose_it
            
        memo[(amount, coins)] = result 
        return result
       
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
