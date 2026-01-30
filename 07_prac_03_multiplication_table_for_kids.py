for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
       for j in range(1, 11):
           f.write(f"{i}X{j}={i*j}")
           if j!=10:
               f.write('\n')

# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# print(add_item(1))
# print(add_item(2))
# print(add_item(3, ['a']))
# print(add_item(4))

# text = "Hello, World!"
# print(text[7:12])

# person = {"name": "Alice", "age": 30}
# print(person.get("age"))

# nums = [1, 2, 3, 4]
# squares = [x**2 for x in nums]
# print(squares)
# lst = [[0]] * 3
# lst[0].append(1)
# print(lst)

# x = 5

# def func():
#     x = 10
#     print(x)

# func()
# print(x)

# nums = [1, 2, 3, 4, 5]
# result = [x for x in nums if x % 2 == 0]
# print(result)

# s = "hello"
# s[0] = "H"
# print(s)







    
