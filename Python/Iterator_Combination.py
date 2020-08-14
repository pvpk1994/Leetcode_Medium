# Author: Pavan Kumar Paluri
# Iterator for Combination - LeetCode Medium - Backtracking 

'''
Problem Description:
-------------------
Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    A function next() that returns the next combination of length combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.

 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

 

Constraints:

    1 <= combinationLength <= characters.length <= 15
    There will be at most 10^4 function calls per test.
    It's guaranteed that all calls of the function next are valid.

'''
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combo_arr= []
        n,k = len(characters), combinationLength
        
        def backtracking(first=0, current = []):
            if len(current)==k:
                self.combo_arr.append(''.join(current[:]))
            # iterate through the array 
            for i in range(first, n):
                current.append(characters[i])
                backtracking(i+1, current)
                current.pop()
        backtracking()
        # Rerverse the array to pop elements one after other
        self.combo_arr=self.combo_arr[::-1]
        
    def next(self) -> str:
        return self.combo_arr.pop()
        
    def hasNext(self) -> bool:
        if self.combo_arr:
            return True
        return False 


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
