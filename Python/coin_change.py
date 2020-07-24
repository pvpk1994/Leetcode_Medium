# Coin change problem

def number_of_coins(coins: list, total: int)->int:
  # construct an array holding number of coins required for each sum value working up to the given sum
  coins = sorted(coins)
  print("Coins " + str(coins))
  num_coins = [total+1]*(total+1)
  # base case : If total is 0, 0 coins need to be picked
  if total ==0:
    return 0
  num_coins[0] =0
  # If num_coins dont add up to given total, simply return -1
  for i in range(total+1):
    # iterate through the list of coins
    for coin in coins:
      # if the coin to be picked is less than the sum itself, consider it.
      if(coin <= i):
        num_coins[i] = min(num_coins[i], 1 + num_coins[i-coin])
      else:
        break
  print(num_coins)
  if num_coins[total] > total:
    return -1
  else:
    return num_coins[total]
if __name__ == "__main__":
  coin_arr = [474, 83, 404, 3]
  money_sum = 264
  print(number_of_coins(coin_arr, money_sum))
