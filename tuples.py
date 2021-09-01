# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

#no need to specify parentheses
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

#Creating a tuple with single element
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Concatenation
print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)          # Output: ('Repeat', 'Repeat', 'Repeat')

# Can't delete items, Can delete an entire tuple
del my_tuple

#Tuple methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3