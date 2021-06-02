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

def checkPalindrome_2(string, k):
    revStr = string[::-1]                                                       #sets the palindrome
    l = len(string)                                                             #sets the length

    return (checker(string, revStr, l, l) <= k * 2)                             #passes it to the check function


#tests
string = "abcdcba"                                                              #our k = 1 test
k = 1

print("True" if checkPalindrome_1(string, k) else "False")

string2 = "abcdeba"                                                             #our k = 2 tests
k = 2
print("True" if checkPalindrome_2(string, k) else "False")
