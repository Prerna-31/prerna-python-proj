lst = [x*x for x in range(1,5)]
print('Square of first five numbers:',lst)

lst = [x for x in range(10) if not x%2]   ## non-zero value for lst to have some values in it.
print('First 10 even numbers:',lst)

lst = [(b,a) for (a,b) in ((1,2),(3,4))]
print('Swap each element of tuple in the list:', lst)

lst = [ord(c) for c in 'My name is khan']
print('ASCII value of each character in string:',lst)

lst = [i for i,c in enumerate('My name is khan') if c==' ']
print('Index of each space:',lst)

lst = [p for p in range(50) if not [x for x in range(2,p) if not p%x]]
print('list of prime numbers < 50',lst)

v='aeiouAEIOU'
#lst = [{w:[w.upper(),len(w),w.isalpha(), 'vowel' if any(c in v for c in w) else 'non-vowel']}
      # for words in open("file_to_read.txt","r") for w in words.split(' ')]  # gives addtional information- length, upper case, if it is alpha
lst = [{w:['vowel' if any(c in v for c in w) else 'non-vowel']} for words in open("file_to_read.txt") for w in words.split(' ')]
print('Tells if word in the text file contains vowels:')
print(lst)