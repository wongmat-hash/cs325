import math
import os
import random
import re
import sys
#global variable
g = 1

#bottom up approach
def game_bottomup(n):
    global g
    g = g + 1
    #if (g % 2 == 0):
        #print("its A's turn")
    #else:
        #print("its B's turn")
    #base cases
    #print("bottom up start: n val = ", n)           #TEST
    if (g % 2 == 0):
        if (n == 2):                                    #insta win for A
            return True
        if (n == 3):                                    #a instant lose
            return False
    if (g % 2 == 1):
        if (n == 2):                                    #b insta wins
            return False
        if (n == 3):                                    #b instant lose b
            return True

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

print(game_bottomup(11))    #should return true
#print(game_bottomup(3))    #should return false
