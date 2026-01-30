f = open('sample.txt') 
#Read first line
data = f.readline()
print(data)
#Read second line
data = f.readline()
print(data)
#Read third line...or so on...
data = f.readline()
print(data)
f.close()