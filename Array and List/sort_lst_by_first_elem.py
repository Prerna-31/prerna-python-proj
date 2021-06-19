"""
Sort list based on 0th element in each sublist/tuple without using sorted
"""
def sortFirstElement(lst):
    if( len(lst) == 0 ):
        return
    min_tup = min(lst)
    sort_lst.append(min_tup)
    lst.remove(min_tup)
    sortFirstElement(lst)

"""
Sort list based on 0th element in each sublist/tuple using sorted
"""
def sortListByFirstElement(lst):
    print(sorted(lst, key=lambda x:x[0]))



lst = [(10,6),(3,5),(8,1),(2,0)]
sort_lst = []
sortFirstElement(lst)
print("Sorting list without using sorted method: ")
print(sort_lst)

lst1 = [(10,6),(3,5),(8,1),(2,0)]
print("Sorting list using sorted method: ")
sortListByFirstElement(lst1)