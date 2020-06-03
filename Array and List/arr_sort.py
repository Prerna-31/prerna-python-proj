from array import *
org_arr = array('i',[])
n = int(input('Enter number of elements you want to sort: '))
for i in range(n):
    val = int(input('Enter element for array: '))
    org_arr.append(val)

for i in range(n):
    for j in range(i+1,n):
        if org_arr[i] > org_arr[j]:
            temp = org_arr[i]
            org_arr[i] = org_arr[j]
            org_arr[j] = temp

print('The array after sorting :' ,  org_arr)