"""
Ex- str = Prerna
Hypothesis: reverse_string(str)  --->  reverse the string --> anrerP
            reverse_string(smaller string)   ---> rever the input string ---> nrerp
Induction : print 'a'(last character) before recursive call == str[len(str)-1]
Base Condition: if len(str) = 1 , print str
"""

def reverse_string(str):
    if(len(str) == 1):
        print(str)
        return

    print(str[len(str)-1] , end="")
    reverse_string(str[0:len(str)-1])

if(__name__ =="__main__"):
    str = input("Enter the string you want to reverse:")
    reverse_string(str)