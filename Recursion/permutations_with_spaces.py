"""
Program to print all the possible strings with spaces for the given string
"""
def permutation_with_spaces(input, output):
    if(len(input) == 0):
        print(output)
        return

    op1 = output + input[0]   ## Added input without space
    op2 = output + "_" + input[0]    ##Added input with space
    permutation_with_spaces(input[1:], op1)
    permutation_with_spaces(input[1:], op2)

input = "ABCD"
output = input[0]
permutation_with_spaces(input[1:], output)