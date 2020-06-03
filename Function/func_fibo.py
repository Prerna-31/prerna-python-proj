def print_fibo(lmt):
    n1 = 0
    n2 = 1
    print(n1, n2, end = " ")
    for i in range(lmt):
        n3 = n1 + n2
        n1,n2 = n2,n3
        if n3 > lmt:
            break;

        print(n3,end=" ")

lmt = int(input('Enter the the upper limit of fibbonacci series you want to print: '))
print_fibo(lmt)