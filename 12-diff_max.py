"""
[7, 1, 5, 3, 6, 4]

5
"""
import math

def max_profit(prices):
  prf = 0
  min_price = math.inf

  for p in prices:
    min_price = min(min_price, p)
    prf = max(prf, p-min_price)

  return prf

print(max_profit([7, 1, 5, 3, 6, 4]))