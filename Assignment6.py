def knapsack_top_down(values, weights, W, n, dp):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if weights[n - 1] <= W:
        include = values[n - 1] + knapsack_top_down(
            values, weights, W - weights[n - 1], n - 1, dp
        )
        exclude = knapsack_top_down(values, weights, W, n - 1, dp)
        dp[n][W] = max(include, exclude)
    else:
        dp[n][W] = knapsack_top_down(values, weights, W, n - 1, dp)

    return dp[n][W]


def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

print("Top-Down:", knapsack_top_down(values, weights, W, n, dp))
print("Bottom-Up:", knapsack_bottom_up(values, weights, W))
