
# Python3 program to find
# the minimum cost required
# to reach the n-th floor

# function to find the minimum
# cost to reach N-th floor
def minimumCost(cost, n):

    # declare an array
    dp = [None]*n

    # base case
    if n == 1:
        return cost[0]

    # initially to climb
    # till 0-th or 1th stair
    dp[0] = cost[0]
    dp[1] = cost[1]

    # iterate for finding the cost
    for i in range(2, n):
        print("index: ", i)
        print("dp[i-1] = ", dp[i-1])
        print("dp[i-2] = ", dp[i-2])
        print("cost[i] = ", cost[i])
        print("dp[i-2] + cost[i] = ", dp[i-2] + cost[i])
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        print("value of dp[i] = ", dp[i])
    # return the minimum
    return min(dp[n - 2], dp[n - 1])

# Driver Code
if __name__ == "__main__":
    a = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    n = len(a)
    print(minimumCost(a, n))

# This code is contributed
# by ChitraNayal
