"""
Hypothesis: sort(4,3,6,2,1)  --> gives sorted array --> 1,2,3,4,6
            sort(4,3,6,2)    --> gives sorted array --> 2,3,4,6
Induction: Insert the last element(arr[n]) at correct position.  --> this also can be performed directly or using recursion
Base Condition: if n == 1 , return arr[n]  where n is size of an array.

last ele = 1
Hypothesis for insertion:  insert([2,3,4,6], ele_to_insert)  --> insert 1 at correct position.
                           insert([2,3,4) , ele_to_insert)  --> insert 1 at correct position.
Induction:
Base condition for sort: if ele_to_insert >= arr[n-1] , insert at the end.
"""
def sort(lst):
    if(len(lst) == 1 or len(lst) == 0):
        return lst
    last_ele = lst.pop(len(lst)-1)
    sort(lst)
    insert(lst,last_ele)

def insert(lst, ele_to_insert):
    if(len(lst) == 0 or ele_to_insert >= lst[len(lst)- 1]):
        lst.append(ele_to_insert)
        return

    val = lst.pop(len(lst)-1)
    insert(lst,ele_to_insert)
    lst.append(val)

lst = [4,3,6,2,1]
if(__name__ == "__main__"):
    sort(lst)
    print(lst)