from numpy import *
#m1 = asmatrix('1,2,3; 4,5,6; 7,8,9')
#m2 = asmatrix('10,11,12; 13,14,15; 16,17,18')
## matrix multiplication using function
#m3 = m1 * m2
#print 'Matrix multiplication product: ',m3

## matrix multiplcation without using function
a1 = array([
               [1,2,3],
               [4,5,6],
               [7,8,9]
            ],int)
a2 = array([
               [10,11,12,19],
               [13,14,15,20],
               [16,17,18,21]
            ],int)
#arr3 = array([[],[]])
#arr3 = empty(shape=[0,2])
arr_result = zeros((3,4),int)
print (len(a1),len(a2[0]),len(a2))

for i in range(len(a1)):       # 3: no. of rows
    for j in range(len(a2[0])):   #4: no. of cols in first row
        for k in range(len(a2)):   # 3: no. of rows
           arr_result[i][j] += a1[i][k] * a2[k][j];

print(arr_result)