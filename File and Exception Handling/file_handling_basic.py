f = open("file_to_read.txt","r")
print(f.readline(5))  ## read only the first line. If pass arguments ex- 5, it reads the first 5 characters of the first line
print(f.readline())
print(f.readline())
#print(f.readlines())  ## reads all lines but will print in a line separated by new line characters
#print(f.read())  ## This reads full file at a time.

fw = open("file_to_write.txt","w")
fw.write("Hi, this is my the first program to write into file.")

fw = open("file_to_write.txt","a")
for i in f.read():
    fw.write(i)

fw.writelines("Today's date is 28th Feb 2020 \nTime is 09:32AM")