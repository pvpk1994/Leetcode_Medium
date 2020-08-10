# Longest Common Subsequence using Dynamic Programming 
# Hackerrank Medium Problem 

# Complete the commonChild function below.
def commonChild(s1, s2):
    # Case of DP 
    max_num = 0
    dp = [[0 for _ in range(-1,len(s1))] for _ in range(-1,len(s2))]
    # dp=[][]
    for i in range(-1,len(s2)):
        for j in range(-1,len(s1)):
            dp[i][j] = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
                # dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if dp[i][j] > max_num:
                max_num = dp[i][j]
    return max_num
