def is_pallindrome(in_str):
    rev_str = ""
   # for i in range(len(in_str)-1, -1, -1):
    #    rev_str = rev_str + in_str[i]
    rev_str = in_str[::-1]        ## without for loop.
    print(rev_str)

    if(rev_str.upper() == in_str.upper()):
        return True
    return False

my_str = input("Enter the input string to determine if string is pallindrom :")
if (is_pallindrome(my_str)):
    print("The entered sring is pallindrome ")
else:
    print("The entered string is not a pallindrome ")