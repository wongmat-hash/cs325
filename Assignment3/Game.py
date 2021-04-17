import math
import os
import random
import re
import sys
#global variable
g = 0

#bottom up approach
def game_bottomup(n):
    #global g
    #g = g + 1
    #if (g % 2 == 1):
    #    print("its A's turn")
    #else:
    #    print("its B's turn")
    #base cases
    #print("bottom up start: n val = ", n)           #TEST
    if (n == 2):                                    #insta win for A
        return True

    if (n == 3):                                    #insta win for B no winnable cases for A
        return False

    #loop code to find factors
    for i in range(1, n):
        #print("i = ", i)                            #TEST
        if n % i == 0:                              #we find the factor
            lastfactor = i
            #print("i is factor", i)                 #TEST:should print the factor
            if (((n-i) % 2) == 1):                  #check if its odd to force odd to next person
                #print("if ODD state", i)            #TEST ODD state
                return(game_bottomup(n-i))
            #else:
                #print("else EVEN state", i)         #TEST EVEN state
    #print("exit i val ", i)                         #TEST exit val
    #print("Lastfact ", lastfactor)                  #TEST lastfactor val
    return(game_bottomup(n-lastfactor))


    #checks if A is facing odd
    #if (n % 2 == 1):
    #checks if A is facing even
    #if (n % 2 == 0):


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
print(game_bottomup(3))    #should return true
#print(game_bottomup(3))    #should return false
