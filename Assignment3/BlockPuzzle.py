#this function will solve the problem using bottom up approach with base cases
def blockpuzzle_dp(N):
    if (N == 0):
        return 1
    #use an array to the size of N + 1 for index
    dp = [0]*(N+1)

    #base cases
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(blockpuzzle_dp(2))
print(blockpuzzle_dp(3))
print(blockpuzzle_dp(4))
