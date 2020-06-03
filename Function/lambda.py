import operator
from functools import reduce

lst = [10,13,14,77,18]
even = list(filter(lambda a:a%2==0,lst))  ##returns list
print ('List of even numbers: ',even)
lst_of_prime = list(filter(lambda num:(num%2 != 0 and num != (0,1,2)),lst))
print("List of prime numbers: ", lst_of_prime)
doubles = list(map(lambda a:a*2,even))  ## returns list
print ('List of doubles of above list of even numbers: ',doubles)
print('Sum of doubles using lambda: ',reduce(lambda a,b:a+b,doubles))  ##returns sum
print('Sum of doubles using in-built method[add]:',reduce(operator.add,doubles))   ##returns sum
print('Product of doubles using in-built method[mul]:',reduce(operator.mul,doubles))   ##returns product
print('Concatenation of strings using in-built method[add]:',reduce(operator.add,['User1',' ','loves',' ','User2']))

lst2 = ['SAT','SUN']
print('Splitting list of strings into list of chars:',list(map(list,lst2)))  # returning list of list


