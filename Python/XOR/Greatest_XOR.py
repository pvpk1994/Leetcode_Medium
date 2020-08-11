# Find the Count of XOR results greater than given number
# Author: Pavan Kumar Paluri
# Source: HackerRank

# Question: https://www.hackerrank.com/challenges/the-great-xor/problem?isFullScreen=true

# Solution

# Complete the theGreatXor function below.
def theGreatXor(x):
    '''
    # Naive Approach:

    counter  =0
    a = 1
    while a < x:
        if (a^x) > x:
            counter +=1
        a+=1
    return counter
    '''
    # A number XORed with less than all its numbers  goes upto max of binary representation of diigts of x
    bin_x = bin(x)
    bin_only = bin_x[2:]
    res = (1 << len(bin_only))-1
    return res-x
