class Solution {
    private:
    vector<int>final_result;
public:
    void dfs(int N, int digit, int K)
    {
        // If limiting condition reached : ie N==0
        if(N==0){
            // cout << "digit is: " << digit << endl;
            this->final_result.push_back(digit);
            return;
        }
        // cout << "digit: " << digit << endl; 
        int tail_digit = digit%10;
        set<int> s;
        s.insert(tail_digit+K);
        s.insert(tail_digit-K);
        // Now iterate through the set
        for(auto iters: s)
        {
            if(iters>=0 && iters<10){
                // if it falls in the range 
                int new_num = digit*10+iters;
                dfs(N-1, new_num, K);
            }
        }
        
    }
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int>digits {1,2,3,4,5,6,7,8,9};
        // if N==1 and K be anything
        if(N==1)
        {
            digits.insert(digits.begin(), 0);
            return digits;
        }
        for(auto&iter: digits)
        {
            dfs(N-1, iter, K);
        }
        
        return this->final_result;
    }
};
