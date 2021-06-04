def patternmatch(string, p):                                                    #function that takes in string and pattern
    s_len = len(string)                                                         #set the string length to s_len
    p_len = len(p)                                                              #store our length of p
    if p_len - p.count('*') > s_len:                                            #check if the length of p is less than s_len
        return False                                                            #already impossible for a pattern match
    array = [True] + [False]*s_len                                              #make an array to store our comparison
    for i in p:                                                                 #loop through to p
        if i != '*':                                                            #try to find '*'
            for n in reversed(range(s_len)):                                    #look through the reversed of s
                array[n+1] = array[n] and (i == string[n] or i == '?')          #check for ?
        else:
            for n in range(1, s_len+1):                                         #otherwise loop again to s len
                array[n] = array[n-1] or array[n]                               #set the array we use for storage
        array[0] = array[0] and i == '*'                                        #set the pattern '*'
    return array[-1]

#test cases
string = "abcde"
pattern = '*'
print(patternmatch(string, pattern))

string2 = 'abcde'
pattern2 = '*a?c*'
print(patternmatch(string2, pattern2))

string3 = 'abcde'
pattern3 = 'ad'
print(patternmatch(string3, pattern3))

string4 = 'abcde'
pattern4 = 'ad?'
print(patternmatch(string4, pattern4))
