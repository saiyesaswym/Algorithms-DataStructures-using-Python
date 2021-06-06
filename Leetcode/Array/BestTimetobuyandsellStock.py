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
