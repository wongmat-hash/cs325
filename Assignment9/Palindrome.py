def checker(str1, str2, m, n):
    #error validation
    if not m: return n                                                          #checks if we have an empty string being passed in error validation
    if not n: return m                                                          #error validation for 2nd reversed string

    if str1[m-1] == str2[n-1]:                                                  #checks if the last chars are the same
        return checker(str1, str2, m-1, n-1)                                    #recursively calls itself to check inside -1 char are the same

    res = 1 + min(checker(str1, str2, m-1, n),  # Remove from str1              #if they are not the same we remove last chars as possible k value and check again
                 (checker(str1, str2, m, n-1))) # Remove from str2

    return res                                                                  #return the value

def checkPalindrome_1(string, k):
    revStr = string[::-1]                                                       #sets the palindrome
    l = len(string)                                                             #sets the length

    return (checker(string, revStr, l, l) <= k * 2)                             #passes original + rev + lengths to checker

def checker_2(X, Y, m, n ):                                                     #checker function for method 2

    L = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):                                                        #loop to the lenght
        for j in range(n+1):                                                    #loop again to the length
            if not i or not j:
                L[i][j] = 0                                                     #check if the values of the string + reversed are the same
            elif X[i - 1] == Y[j - 1]:                                          #else check for the inner values of the outter values
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

def checkPalindrome_2(string, k):

    n = len(string)                                                             #set the n to the length of the string

    revStr = string[::-1]                                                       #reverse the string itself

    lps = checker_2(string, revStr, n, n)                                       #pass to the checker which checks for longest common subsequence

    return (n - lps <= k)                                                       #if the difference is less than K then we say its k palindrome



#tests
string = "abcdcba"                                                              #our k = 1 test
k = 1

print("True" if checkPalindrome_1(string, k) else "False")

string2 = "abcdeba"                                                             #our k = 2 tests
k = 2
print("True" if checkPalindrome_2(string, k) else "False")
