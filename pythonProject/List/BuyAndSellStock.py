import sys
def BuyAndSellStock(nums:list[int])->int:
    profit=0
    min_price=sys.maxsize

    for num in nums:
        min_price=min(min_price,num)
        profit=max(profit,num-min_price)
        
    return profit

