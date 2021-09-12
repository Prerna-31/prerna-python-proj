"""
Program to print all subsets /powersets for the given list
"""
def print_subsets(input, output):
    if len(input) == 0:
        print(output)
        return

    op1 = output[:]  ## current element is not included in the resultant list
    op2 = output + [input[0]]    ## current element is included in the resultant list

    print_subsets(input[1:],op1)
    print_subsets(input[1:],op2)

    return

lst = [4,2,1]
output = []
print_subsets(lst, output)