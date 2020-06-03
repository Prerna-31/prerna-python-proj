from array import *
arr = array('i',[])
n = int(input('Enter the length of an array: '))
for i in range(n):
    x = int(input('Enter element of array: '))
    arr.append(x)

max = arr[0]
for i in range(1,n):
    if (arr[i] > max):
        max = arr[i]

print('Maximum value in entered array: ', max)