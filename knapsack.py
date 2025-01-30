def knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

# Test the function
values = [50, 100, 140]
weights = [2, 3, 5]
capacity = 5
n = len(values)
print("Maximum value:", knapsack(capacity, weights, values, n))
