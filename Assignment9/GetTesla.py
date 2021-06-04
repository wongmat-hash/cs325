def getTesla(M):                                                                #get Tesla function takes M in
    rows = 3                                                                    #preset the row and column data
    col = 3
    dp = [[0 for x in range(col + 1)]                                           #create an empty array and use loops to row and column size
             for y in range(rows + 1)]
    x = rows
    y = col

    if (M[x - 1][y - 1] > 0):                                                   #check if the m[3-1][3-1]= m[2][2] is > 0
        dp[x - 1][y - 1] = 1                                                    #fill our empty array same spot = 1
    else:
        dp[x - 1][y - 1]=abs(M[x - 1][y - 1])+1                                 #otherwise our empty array spot [2][2] in first case = abs value of [2][2] value + 1

    for i in range (x - 2, -1, -1):                                             #we fill last row last column as base case x = rows in this case
        dp[i][y - 1] = max(dp[i + 1][y - 1]-M[i][y - 1], 1)                     #empty array column spot -1 = max value of the empty array previous col spot
    for i in range (2, -1, -1):                                                 #loop through in range again without column base case
        dp[x - 1][i] = max(dp[x - 1][i + 1] - M[x - 1][i], 1)                   #set our empty array row values

    for i in range(x - 2, -1, -1):                                              #use bottom up and fill up the array for rows
        for j in range(y - 2, -1, -1):                                          #use bottom up and fill up the array for columns
            min_M_val = min(dp[i + 1][j],dp[i][j + 1])                          #our min m value we can have is now the min of the storage array for loop values
            dp[i][j] = max(min_M_val - M[i][j], 1)                              #our j values are set
    return dp[0][0]                                                             #return the first spot of our array 

#test input
M = [[-1,-2,3], [10,-8,1], [-5,-2,-3]]                                          #m definition by grid
print(getTesla(M))                                                              #prints the return of getTesla
