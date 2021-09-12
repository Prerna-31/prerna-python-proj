"""
Program to print unique substrings(non-repeating subsets) for the given string
"""
result = set()
def print_unique_subsets(input, output):
    global result
    if(len(input) == 0):
        result.add(output)
        return

    op1 = output
    op2 = output + input[0]
    print_unique_subsets(input[1:],op1)
    print_unique_subsets(input[1:],op2)

    return


input = "abb"
output = ""
print_unique_subsets(input, output)
for i in result:
    print(i)