class Solution:
    # THis function only conisders right subtrees of a binary tree
    
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # USe Depth First Search - DFS. 
        digits = [1,2,3,4,5,6,7,8,9]
        if N==1:
            return [0]+digits
        ans =[]
        def DFS(N, num):
            # base case:
            if N == 0:
                return ans.append(num)
            # Compute tail digit
            tail_digit = num%10
            # set:
            next_set_nums = set([tail_digit+K, tail_digit-K])
            
            for next_num in next_set_nums:
                if 0<= next_num < 10:
                    new_num = num*10 + next_num
                    DFS(N-1, new_num)
        
        for num in range(1, len(digits)+1):
            DFS(N-1, num)
        return ans
        
        '''
        digits =[0,1,2,3,4,5,6,7,8,9]
        # Apply 2-sum
        if N==1:
            return digits
        lo = 0
        hi = len(digits)-1
        output = []
        final_output = []
        hash_set = set()
        for i in range(0, len(digits)):
            if digits[i]+K in digits:
                if digits[i] != 0:
                    output.append((digits[i], digits[i]+K))
                if digits[i]+K != digits[i]:
                    output.append((digits[i]+K, digits[i]))
        print(output)
        # If here: Output should have desired tuples we are looking for
        
        for tup in output:
            string_new = ""
            iterator = 0
            for i in range(N):
                if i%2 ==0:
                    # reset iterator
                    iterator =0
                string_new += str(tup[iterator])
                iterator+=1
            final_output.append(int(string_new))
        return sorted(final_output)
          '''          
 
