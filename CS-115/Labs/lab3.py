'''
Created on Sep 21, 2017

@author: Himanshu Rana - hrana2 
"I pledge my honor that I have abided by the Stevens Honor System" 
'''


def change(amount, coins):
    """This function takes in a non-negative amount. A list, coins, will be provided. 
        The function will return the least number of coins needed to make the amount"""
    def min_val(x, y):
        """This function finds the least amount of coins that are needed to get the amount"""
        if y == 0: 
            return 0 
        elif x == -1 or y < 0: 
            return float("inf")
        else: 
            use_it = min_val(x - 1 , y)
            lose_it = 1 + min_val(x, y - coins[x])
        return min(use_it, lose_it)
    
    return min_val(len(coins) - 1, amount)
                                                                                    
    


    
    
print(change(48, [1, 5, 10, 25, 50]))
