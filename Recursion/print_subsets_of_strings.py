"""
Program to print substrings for the given string
"""
def print_subsets(input, output):
    if len(input) == 0:
        print(output)
        return

    op1 = output        ## current letter is not included in output string
    op2 = output + input[0]      ## current letter is included in string
    print_subsets(input[1:],op1)
    print_subsets(input[1:],op2)
    return

input = "abc"
output = ""
print_subsets(input, output)