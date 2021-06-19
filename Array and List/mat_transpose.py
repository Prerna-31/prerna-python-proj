"""
Get transpose Using Zip
"""
def getTransposeByZip(lst):
    transpose_matrix = zip(*lst)
    print("Transpose using Zip :")
    for i in transpose_matrix:
        print(i)

"""
Get transpose Using List comprehension:
"""
def gettransposeByListComp(lst):
    transpose_matrix = [[lst[i][j] for i in range(len(lst))] for j in range(len(lst[0]))]
    print("Transpose using List Comprehension :")
    for row in transpose_matrix:
        print(row)

"""
Get transpose Using numpy:
"""
from numpy import asmatrix
def getTransposeByNumpy(lst):
    transpose_mat = asmatrix(lst).transpose()
    print("Transpose using Numpy :")
    print(transpose_mat)


lst = [[1,2,3],
       [4,5,6]]
getTransposeByZip(lst)
gettransposeByListComp(lst)
getTransposeByNumpy(lst)