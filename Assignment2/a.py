def MajorityBirthdays(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_fre = List.count(i)
        if(curr_fre > counter):
            counter = curr_fre
            num = i
    return num

def foo(arr, start, end):
  if(start < end):
    middle = (start+end)//2
    foo(arr, start, middle)
    foo(arr, middle+1, end)
  else:
    arr[start] = 2 * arr[start]

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

  foo(arr, 0, len(lst))

  for i in range(0, len(lst)):
    print(arr[i])
