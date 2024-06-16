'''
Created on Sep 28, 2017

@author: hrana2 - Himanshu Rana 
"I pledge my honor that I have abided by the Stevens Honor System" 
'''

def knapsack(capacity, itemList):
    """This function takes an integer value, capacity and a list of list 
    that contains a weight value and monetary value. The function will return 
    the best items to take without going over the capacity and has the best 
    monetary value"""
        
    
    if capacity == 0:  
        return [0, []]
    if itemList == []: 
        return [0, []]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:]) 
     
    use_it  = knapsack(capacity - itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    
    use_it_value  = [itemList[0][1] + use_it[0], [itemList[0]] + use_it[1]]
    
    if use_it_value[0] > lose_it[0]: 
        return use_it_value
    return lose_it

print(knapsack(6, [[1, 4], [5, 150], [4, 180]])) 