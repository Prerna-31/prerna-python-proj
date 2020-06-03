## Pattern 1:##
###############
i=1
j=1
while i < 5:
    j=1
    while j < 5:
        print('#', end="")
        j+=1
    print('')
    i+=1

print('\n')

## Pattern 2:##
###############
i = 5
j = 0
while i >= 0:
    j = 0
    while j <= i:
        print('*',end="")
        j+=1
    print('')
    i-=1

print('\n')

## Pattern 3:##
###############
k = 5
for i in range(1,5):
    for j in range(i,k):
        print(j,end="")
    print('')

print('\n')

## Pattern 4:##
###############
## With hardcoded values in list
i = 0
lst = ['A','P','Q','R']
rep_lst = ['A','B','C','D']
for rc in rep_lst:
    for c in lst:
        lst[i] = rep_lst[i]
        print(c,end="")
    i+=1
    print('')

print('\n')
## Without hardcoded values in list
cnt = 0
for i in range(0,4):
    cnt = 0
    for j in range(79,83):
        if cnt <= i:
            print(chr(j-14) ,end="")
            cnt+=1
        else:
            print(chr(j) ,end="")
    i+=1
    print('')