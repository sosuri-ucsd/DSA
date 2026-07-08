def buy_and_sell(arr): # BRUTE 
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                profit = arr[j] - arr[i]
                max_profit = max(max_profit, profit)
    return max_profit

def boy_and_sell(arr):
    minima = float('inf')
    maxima = 0
    for i in range(len(arr)):
        min_price = min(minima, arr[i])
        maxima = max(maxima, arr[i] - minima)
    return maxima
        