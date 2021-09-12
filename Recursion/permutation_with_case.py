"""
Program to print all the permutations of the given string in different cases.
"""
def permutation_with_case(input, output):
    if(len(input) == 0):
        print(output)
        return

    if(input[0].isdigit()):
        op1 = output + input[0]
        permutation_with_case(input[1:],op1)
    elif(input[0].isalpha()):
        op1 = output + input[0]
        ascii_val = ord(input[0])

        if(ascii_val >=65 and ascii_val <= 91 ):
            op2 = output +  input[0].lower()
        elif(ascii_val >=97 and ascii_val <=123):
            op2 = output + input[0].upper()

        permutation_with_case(input[1:], op1)
        permutation_with_case(input[1:], op2)

    return

input = "A1B2"
output = ""
permutation_with_case(input, output)