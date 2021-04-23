def swap(lista, idx1, idx2):
    temp = lista[idx1]
    lista[idx1] = lista[idx2]
    lista[idx2] = temp

def valid():
    return True

def total(arr, sum):                                                            #this function prints the value of our array
    for i in range(0, len(arr)):
        sum = sum + arr[i]

def permutare(lista, start):
    if start >= len(lista):
        if valid():
            #print("valid")
            return [list(lista)]

    sum = 0
    output = []
    for idx in xrange(start, len(lista)):
        #sum = sum + lista[idx]
        swap(lista, start, idx)
        output.extend(permutare(lista, start + 1))
        swap(lista, start, idx)  # backtrack
        #print("sum: ", total(output))
        #print(sum(output))
        #should only return if its non sequential

        #total(output)
        #sum up the array and return that instead
    #return sum
    return output

arr = [1, 2, 3, 4]
k = 0
print(permutare(arr, 0))
