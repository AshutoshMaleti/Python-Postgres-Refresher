# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

#Accessing Elements from Dictionary
my_dict = {'name': 'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

#Removing elements from Dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# remove all items
squares.clear()

# delete the dictionary itself
del squares

# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)