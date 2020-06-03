def print_names(lst):
    print('List of names having length more than 4: ')
    for elm in lst:
        if len(elm) > 4:
            print(elm)

#lst = ['user1','user21','usr','user301']
lst = []
n = int(input('Enter the length of list having names:'))
print("Enter names::::")
for i in range(n):
    ele = input()    ## for string as an input to the list
    lst.append(ele)
print_names(lst)