#empty array to store user input
lst = []

#user input for number of inputs
n = int(input("Enter number of elements : "))

#iterate through the array and store user inputs
for i in range(0, n):
    ele = int(input())

    lst.append(ele)     #adding the element into the array

print("Input: ")
print(lst)
