"""
For every element, calculating the difference between that element and the minimum of all the values
before that element and updating the maximum profit if the difference thus found is greater than the current maximum profit.
Time complexity: O(n)
Space complexity: O(1)
"""
def maxProfit(prices: List[int]) -> int:
    min_price=999999
    max_profit=0

    for i in prices:
        if i<min_price:
            min_price=i
        if i-min_price>max_profit:
            max_profit = i-min_price

    return max_profit


"""
Two pointer Approach
Increment left pointer to minimum values, updating the profit wherever possible
Time complexity: O(n)
Space complexity: O(1)
"""
def maxProfit(self, prices: List[int]) -> int:
    i=0
    j=1
    profit=0
    while j<len(prices):
        if prices[i]>prices[j]:
            i=j
            j+=1
        else:
            profit = max(profit, prices[j]-prices[i])
            j+=1
    return profit
