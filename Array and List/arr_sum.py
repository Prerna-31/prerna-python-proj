#from array import *
#arr1 = array('i',[45,67,23,90,10])
#arr2 = array('i',[56,38,90,13,80])
#arr3 = array('i',[])

# Below logic to add array elements using array.
#for i in range(len(arr1)):
 #   arr3.append(arr1[i] + arr2[i])
#print arr3

# Below logic to add array elements using numpy-- matrix sum using function.
from numpy import *
arr1 = array([45,67,23,90,10],'int')
arr2 = array([56,38,90,13,80],'int')
arr3 = array(empty(5),'int')
m1 = asmatrix(arr1)
m2 = asmatrix(arr2)
#m3 = m1+ m2
# print m3
arr1 = add(arr1,arr2)
print(arr1)