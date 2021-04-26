#recurrence we need to start off with 1st number and add all permutations of non consecutive
def backtracking(arr, array, pos):
    print(*array)           #prints all elements seperated by space
    check(arr, array)       #check if they are consecutive
    #summation(array)
    for i in range(pos, len(arr)):
        array.append(arr[i])
        backtracking(arr, array, i+1)
        array.pop(-1)
    return

#function to find powersets
def powerset(arr):
    global res
    array = []  #empty storage list
    pos = 0
    backtracking(arr, array, pos)

#function to sum up the entire array
def summation(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    #print('')
    #print("Sum:", sum)         #test prints the sum
    return sum

#function to check if we are looking at non consecutive only
def check(arr, array):              #arr is original array and array is empty list containing permutations
    sum = 0                             #storage for sum
    for i in range(0, len(array)):  #loop to the new array
        for j in range(0, len(arr)):    #loop to old array
            if(array[i] == arr[j]):     #if the numbers match or we find a match
                if(i == 0 and j == 0):   #we are on the far left so compare
                    #case 1: the array ends up being 1 permutation so i cannot -1 or +1
                    if(len(array)==1):
                        #print("sum is just single")
                        sum = (summation(array))
                        print("if 1: sum", sum)
                        #print(summation(array))
                        return sum
                        #break;
                    if((len(array) > 1)and array[i+1] == arr[j+1]):
                        print("1: we found a conseq")
                        sum = 0
                        return sum
                        #break;
                    else:
                        sum = (summation(array))
                        print("else 1: sum", sum)
                        return sum
                        #print(summation(array))
                if(i == 0 and j == len(arr)):    #if the i spot compares to end of arr
                    if(array[i+1] == arr[j-1]):
                        print("2. we found a conseq")
                        sum = 0
                        return sum
                        #break;
                    else:
                        sum = (summation(array))
                        print("else 2: sum", sum)
                        #print(summation(array))
                if(i == len(array) and j == len(arr)):       #hit end on both sides
                    if(array[i-1] == arr[j-1]):
                        print("3. we found a conseq")
                        sum = 0
                        return sum
                        #break;
                if((i!= 0 and i!=len(array)) and j!= 0 and j!=len(arr)):       #all other conditions
                    if(array[i-1] or array[i+1 ]== arr[j-1] or arr[j+1]):
                        print("4. we found a conseq")
                        sum = 0
                        return sum
                        #break;
                if(len(array[i] > 1 and (len(arr[j] > 1))) and array[i+1] == arr[j+1]):
                    print("5. we found a conseq")
                    sum = 0
                    return sum
                else:
                    sum = (summation(array))
                    print("last else: sum", sum)
                    summation(array)
                    return sum
    #print("sum", sum)




arr = [1, 20, 3]   #test array
powerset(arr)
