"""Two Sum Using Brute Force---> O(n^2)"""
def twoSum(nums, target):
    for num1 in range(0,len(nums)):
        for num2 in range(num1+1,len(nums)):
            target = 0
            target = nums[num1]+nums[num2]
            if(target == 9):
                print("[{},{}]".format(num1,num2))

nums = [2,7,11,13]
target = 9
print("Two sum using Brute Force O(n^2): ")
twoSum(nums, target)

"""Two Sum Using Hashing ---> O(n)"""
def towSumUsingHash(nums, target):
    myHash = {}
    for num1 in range(len(nums)):
        comp = target - nums[num1]
        if comp in myHash:
            return(myHash[comp], num1)

        myHash[nums[num1]] = num1
    return []

nums = [2,7,11,13]
target = 9
lst = towSumUsingHash(nums, target)
print("Two sum using dictionary - O(n): ")
print(lst)

"""Two Sum Using Hashing Another way ---> O(n)"""
def towSumUsingHash1(nums, target):
    myHash = {}
    for i,elem in enumerate(nums):
        comp = target - elem
        if comp in myHash:
            return(myHash[comp], i)

        myHash[elem] = i
    return []

nums = [2,7,11,13]
target = 9
lst = towSumUsingHash1(nums, target)
print("Two sum using Dictionary - O(n): ")
print(lst)

"""Two Sum Using Set ---> O(n)"""
def towSumUsingSet(nums, target):
    mySet = ()
    for elem in nums:
        comp = target - elem
        if comp in mySet:
            return(mySet)

        mySet.add(comp,elem)
    return []

nums = [2,7,11,13]
target = 9
lst = towSumUsingHash1(nums, target)
print("Two sum using Set - O(n): ")
print(lst)