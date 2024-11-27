# Find the maximum profit by choosing a day to buy and a later day to sell a stock.

def buy_and_sell(nums):
    max_profit = 0
    min_price = float('inf')
    
    for num in nums:
        min_price = min(min_price, num)
        profit = num - min_price
        max_profit = max(max_profit, profit)
    return max_profit

print(buy_and_sell([7, 1, 5, 3, 6, 4])) 