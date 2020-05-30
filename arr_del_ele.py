from array import *
arr = array('i',[])
n = input('Enter the size of array: ')
for i in range(n):
    x = input('Enter the array elements: ')
    arr.append(x)

x = input('Enter the index of which you want to delete element: ')
#for i in range(n):
 #  if (i == x):
  #      arr.remove(arr[i])
#print arr

## second method to delete array element without using in-built function:
arr2 = array('i',(a for a in arr if a!=arr[x]))

## third method to delete array element without using in-built function:
#arr2 = array('i',(a for i,a in enumerate(arr) if a!=arr[x]))
print arr2