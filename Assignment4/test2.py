#recurrence we need to start off with 1st number and add all permutations of non consecutive
def backtracking(arr, array, pos):
    print(*array)
    summation(array)
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
    print("Sum: ", sum)         #test prints the sum

arr = [1, 2, 3]   #test array
powerset(arr)
