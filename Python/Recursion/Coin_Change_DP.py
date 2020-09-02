# Coin change problem using Recursion + Memoization (DP) - O(m*n)
# Author: Pavan Kumar Paluri

# coin change problem 
# given a sum and list of coins: return minimum number of coin denominations 
import math
def min_coins(summ:int, list_coins: list, dp:list)->int:
  # stopping conditions
  if summ ==0:
    return 0
  final_res = math.inf
  for coin in list_coins:
    if summ-coin >=0:
      if dp[summ-coin] != -1:
        ans = dp[summ-coin]
      else:
        ans = min_coins(summ-coin, list_coins, dp)
        dp[summ-coin] = ans
      if ans+1 < final_res:
        final_res = ans+1
  print(dp) 
  dp[summ] = final_res
  return dp[summ] 

if __name__=="__main__":
  summ = 1
  dp = [-1 for _ in range(summ+1)]
  dp[0] =0
  list_coins = [3, 5, 1, 2]
  print(min_coins(summ, list_coins, dp))
