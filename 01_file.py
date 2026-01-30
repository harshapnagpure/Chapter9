# use open() function to read the content of a file .
# f = open('sample.txt','r')
f = open('sample.txt') # by default the mode is r(read).
data = f.read()
#data = f.read(5) # reads only first 5 character from content of files
print(data)
f.close()