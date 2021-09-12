"""
Program to generate balanced parenthesis for a given number n. so if n = 2, generate 2 balanced parenthesis.
possible output : (()), ()().
"""
def generate_balanced_parenthesis(n, output, left, right):
    if(left == n and right == n):
        print(output)
        return

    if(left < n):
        op1 = output + '('
        generate_balanced_parenthesis(n, op1, left + 1, right)
    if(left > right):
        op2 = output + ')'
        generate_balanced_parenthesis(n, op2, left, right + 1)

    return

if(__name__ == "__main__"):
    n = 3
    left = right = 0
    generate_balanced_parenthesis(n,   "" , left, right)