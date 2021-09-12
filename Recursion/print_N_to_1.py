"""
Hypothesis: printSequence(n)   --->  n, n-1, n-2 .... 1
            printSequence(n-1) --->  n-1, n-2, n-3 ....1
Induction:  print(n) before calling printSequence(n-1)
Base Condition: if(n == 1) , return
"""

def printSequence(n):
    if(n == 1):
        print(1)
        return

    print(n)
    printSequence(n-1)

if(__name__ =="__main__"):
    n = int(input("Enter the upper limit to which you want to print sequence:"))
    printSequence(n)