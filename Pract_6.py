# 0/1 Knapsack using Dynamic Programming


# Top-Down Approach - Memoization
def knapsack_topdown(weights, values, n, capacity, memo):

    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_topdown(
            weights, values, n - 1, capacity, memo
        )
    else:
        # Include the item
        include = values[n - 1] + knapsack_topdown(
            weights, values, n - 1,
            capacity - weights[n - 1], memo
        )

        # Exclude the item
        exclude = knapsack_topdown(
            weights, values, n - 1, capacity, memo
        )

        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# Bottom-Up Approach - Tabulation
def knapsack_bottomup(weights, values, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                # Take the item
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                # Don't take the item
                not_take = dp[i - 1][w]

                dp[i][w] = max(take, not_take)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

n = len(weights)

# Memoization table
memo = [[-1] * (capacity + 1) for i in range(n + 1)]


# Output
print("Using Top-Down (Memoization):",
      knapsack_topdown(weights, values, n, capacity, memo))

print("Using Bottom-Up (Tabulation):",
      knapsack_bottomup(weights, values, capacity))