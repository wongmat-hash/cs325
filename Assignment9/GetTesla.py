import math as mt
R = 3
C = 3

def getTesla(M):
    dp = [[0 for x in range(C + 1)]
             for y in range(R + 1)]
    m, n = R, C

    if M[m - 1][n - 1] > 0:
        dp[m - 1][n - 1] = 1
    else:
        dp[m - 1][n - 1] = abs(M[m - 1][n - 1]) + 1
    '''
    Fill last row and last column as base
    to fill entire table
    '''
    for i in range (m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           M[i][n - 1], 1)
    for i in range (2, -1, -1):
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           M[m - 1][i], 1)
    '''
    fill the table in bottom-up fashion
    '''
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_M_on_exit = min(dp[i + 1][j],
                                     dp[i][j + 1])
            dp[i][j] = max(min_M_on_exit -
                               M[i][j], 1)

    return dp[0][0]

#test input 
M = [[-1,-2,3], [10,-8,1], [-5,-2,-3]]
print(getTesla(M))
