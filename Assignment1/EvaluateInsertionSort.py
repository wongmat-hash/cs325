import time                                                                     #used for random gen
import random                                                                   #used for random gen

def EvaluateInsertionSort(input):                                               #define our function eval insert sort which sorts an array in dec order
  for i in range(1, len(input)):                                                #loop to the range of index in array
    storageVar = input[i]                                                       #store our input from index
    j = i - 1                                                                   #store the index
    while j >= 0 and storageVar > input[j]:                                     #compare to see if its greater
        input[j+1] = input[j]                                                   #if so swap
        j = j - 1
    input[j + 1] = storageVar

#test it create some random array
input = [1, 3, 5, 7, 9]
print('Test...running our insertion sort function:...\n', input)
EvaluateInsertionSort(input)                                                    #pass in our array to the function
print("Sorted array in dec order...:\n", input)

#collection for time of the array to process
def testArr(inputArray):
    initiate = time.time()
    EvaluateInsertionSort(inputArray)
    end = time.time()

    return (end-initiate)*1000

#creates arrays of different sizes ranging from 0 - 10,000 with collected time
def timeSortingRandomNumbers(test = 10, lower_limit=10, upper_limit=10000):
    arrayone = []                                                              #create two empty arrays
    arraytwo = []
    for i in range(test):                                                       #now we need to seed init the arrays
        size = random.randint(lower_limit, upper_limit)
        array = [random.randint(1,size) for j in range(size)]                   #loop through and randomly fill
        t = testArr(array)
        arrayone.append(size)
        arraytwo.append(t)
    return arrayone, arraytwo

#creates arrays in different sizes randing from 0 - 10,000 with collected time
def timeSortingAscendingNumbers(test=10, lower_limit=10, upper_limit=10000):
    arrayone = []
    arraytwo = []
    for i in range(test):
        size = random.randint(lower_limit, upper_limit)                         #use our range for random number sizes
        array = list(range(size))                                               #instead of looping and initiating array we init the size
        t = testArr(array)
        arrayone.append(size)
        arraytwo.append(t)
    return arrayone, arraytwo

#creates ararys of different sizes ranging from 0 - 10,000 with numbers sorted in descending order with collected time
def timeSortinDescendingNumbers(test = 10, lower_limit=10, upper_limit=10000):
    arrayone = []
    arraytwo = []
    for i in range(test):
        size = random.randint(lower_limit, upper_limit)
        array = list(range(size))
        array.reverse()
        t = testArr(array)
        arrayone.append(size)
        arraytwo.append(t)
    return arrayone, arraytwo

#function to print the table for display
def print_table(len_one, len_two):
    for i in range(len(len_one)):
        print(len_one[i], '\t\t', len_two[i])

#run our functions above
print("Random order array:\nn\t\tTime")
arrayone, arraytwo = timeSortingRandomNumbers(10)
print_table(arrayone, arraytwo)

print("\nAscending Order array:\nn\t\tTime")
arrayone, arraytwo = timeSortingAscendingNumbers(10)
print_table(arrayone, arraytwo)

print("\nDescending order array:\nn\t\tTime")
arrayone, arraytwo = timeSortinDescendingNumbers(10)
print_table(arrayone, arraytwo)
