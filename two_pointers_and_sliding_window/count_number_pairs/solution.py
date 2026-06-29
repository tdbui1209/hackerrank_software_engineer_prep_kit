def countAffordablePairs(prices, budget):
    left = 0
    right = len(prices) - 1
    count = 0
    while left < right:
        if prices[left] + prices[right] <= budget:
            count += right - left
            left += 1
        else:
            right -= 1
    return count
