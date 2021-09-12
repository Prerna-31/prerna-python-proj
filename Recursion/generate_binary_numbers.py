"""
Program to generate n-bit binary number such that no. of 1's >= no. of 0's in any of its prefix.
n = 3  --> valid binary numbers are:- 110, 111, 101
"""
def generate_binary_numbers(n, output, count1, count0):
    if(n == 0):
        print(output)
        return

    op1 = output + "1"
    generate_binary_numbers(n-1, op1, count1+1, count0)

    if(count0 < count1):
        op2 = output + "0"
        generate_binary_numbers(n-1, op2, count1, count0+1)

    return


if(__name__ == "__main__"):
    n = 3
    count1 = 0
    count0 = 0
    generate_binary_numbers(n,"", count1, count0)
