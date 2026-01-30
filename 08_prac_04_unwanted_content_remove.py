with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#") #we are replace according to need our 
 
with open("sample.txt", "w") as f:
    f.write(content)