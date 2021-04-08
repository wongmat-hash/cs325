def function(N):
    assert N >= 8                                                               #got to make sure its not hitting the < 8
    if N == 8:                                                                  #base case for 8
        return (1,1)
    if N == 9:                                                                  #base case for 9
        return (3,0)
    if N == 10:                                                                 #base case for 10
        return (0,2)
    (a, b) = function(N-3)                                                      #recursion portion
    return (a+1,b)

#sample tests check to see if our function works
print("testing 45...")
print(function(45))
print("testing 66...")
print(function(66))
print("testing 8...")
print(function(8))
