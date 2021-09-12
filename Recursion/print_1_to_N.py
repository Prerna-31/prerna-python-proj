"""
hypothesis: printSequence(n)   --> print 1, 2, 3..n
            printSequence(n-1) --> print 1,2,3 ..n-1
induction:  print(n)
base condition: if n==1 : return 1
"""
def printSequence(n):
    if(n == 1):
        print(n)
        return 1

    printSequence(n-1)
    print(n)

if(__name__ =="__main__"):
    n = int(input("Enter the upper limit to which you want to print sequence:"))
    printSequence(n)



