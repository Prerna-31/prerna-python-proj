from numpy import *
##arr = array([])
n = int(input('Enter the length of an array: '))
arr = empty(n,'int')
for i in range(n):
    x = int(input('Enter the element: '))
    arr[i] = x
print ('Original array :',arr)
## reversing an array without using in-built function.
arr_rev = empty(n,'int')
r_ind = 0
for i in range(n-1,-1,-1):
    arr_rev[r_ind] = arr[i]
    r_ind+=1
print ('Reversed array :',arr_rev)