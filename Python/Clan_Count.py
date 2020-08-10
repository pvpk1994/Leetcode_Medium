# Source: CodeSignal
# Author: Pavan Kumar Paluri
'''
Problem Description:
--------------------
Let's call two integers A and B friends if each integer from the array divisors is either a divisor of both A and B or neither A nor B. 
If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?

Example

For divisors = [2, 3] and k = 6, the output should be
numberOfClans(divisors, k) = 4.

The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a clan, and 3 and 6 do not have friends and each is a clan by itself. 
So the numbers 1 through 6 are broken into 4 clans.
'''


def numberOfClans(divisors, k):
    clans = [1]
    def is_frnd(divisors, a, b):
        for i in range(len(divisors)):
            if not(a%divisors[i]==0 and b%divisors[i]==0) and not(a % divisors[i] !=0 and b % divisors[i] != 0):
                return False
        return True
    for i in range(2, k+1):
        should_add = True
        for clan in clans:
            if is_frnd(divisors, clan, i):
                should_add = False
                break
        if should_add:
            clans.append(i)
    return len(clans)
