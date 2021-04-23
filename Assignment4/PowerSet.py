max_length = 0                                                                  #max possible storage

store = []                                                                      #storage array

ans = []

def powerset(arr, index, sum, k):                                               #this takes in the array, index, sum, and temp variable
    global max_length
    sum = sum + arr[index]                                                      #set the sum to accumulate the array index
    store.append(arr[index])                                                    #append the array value via index
    if (sum == k):
        if (max_length < len(store)):
            max_length = len(store)                                             #set the max_length to what we have

            ans = store                                                         #store the sequence
    for i in range(index + 1, len(arr)):
        if(sum + arr[i] <= k):
            powerset(arr, i, sum, k)

            store.pop()
        else:                                                                   #if the sum > 0 continue with earlier values
            return

def maximum(arr, n, k):
    #print("now in max function")                                               #TEST
    arr.sort()                                                                  #sort our array
    #print("finished sorting array")                                            #TEST
    for i in range (n):
        #print("i val", i)                                                      #TEST
        #print("max: ", max_length)                                             #TEST
        if (max_length >= n - i):
            #print("breaking because array was empty")
            break

        store.clear()
        powerset(arr, i , 0, k)

    return max_length

if __name__ == "__main__":
    arr = [-3, 0, 1, 1, 2]
    #arr = [7, 2, 5, 8, 6]
    #arr = []
    n = len(arr)
    #print('lenght of array', n)
    k = 1
    print(maximum(arr, n, k))
