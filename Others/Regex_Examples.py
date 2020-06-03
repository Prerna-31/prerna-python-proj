import random
import re

##Find a pair in the passed string:
pattern=r'.*(.).*\1'
string1='abade cbc dde abcd'
rc = re.compile(pattern)
mth=rc.search(string1)
if mth:
    print("The passed string has pair and the repeated character is ",mth.groups())
else:
    print("The passed string does not have any pair")


## Making a phonebook:

## Text munging: The first and last character of each words would be the same but it would have mixed in between.
Pattern =  r'(\w)(\w+)(\w)'
string1='Mccdonald,Matrimony,Neighbourhood,Whatelse'
def repl(mtc):
    words = list(mtc.group(2))
    random.shuffle(words)
    return (mtc.group(1)+"".join(words)+mtc.group(3))
print("The original string:",string1)
print("The text munging string:",re.sub(Pattern,repl,string1))


## Finding all adverbs and its positions:
Pattern = '\w+ly'
string1 = 'He was carefully disguised but captured quickly'
print("The adverbs are as follows:",re.findall(Pattern,string1))
print("The adverbs and their positions:")
for am in re.finditer(Pattern,string1):
    print("%s --->  %2d-%2d"%(am.group(0),am.start(),am.end()))

