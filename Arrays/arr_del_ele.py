from array import *
arr = array('i',[])
n = int(input('Enter the size of array: '))
print('Enter the array elements--> Only integer: ')
for i in range(n):
    x = int(input())
    arr.append(x)

x = int(input('Enter the index of which you want to delete element: '))

## First method to delete array element using in-built function:
#for i in range(n):
 #  if (i == x):
  #      arr.remove(arr[i])
#print(arr)

## second method to delete array element without using in-built function:
arr2 = array('i',(a for a in arr if a!=arr[x]))

## third method to delete array element without using in-built function:
#arr2 = array('i',(a for i,a in enumerate(arr) if a!=arr[x]))
print(arr2)