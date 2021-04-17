

#bottom up approach
def game_bottomup(n):

    if (n % 2 == 0):
        return True

    if (n % 2 == 1):
        return False



        #recursive statement



    #make this array work
    #dp = [0] * (N+1)

    #base cases
    #dp[0] = False
    #dp[1] = False

    #for i in range(2, N+1):
    #    dp[i] = dp[i-1] + dp[i-2]
    #return dp[N]

#top down approach
#def game_topdown(N):
print(game_bottomup(2))    #should return true
print(game_bottomup(3))    #should return false
