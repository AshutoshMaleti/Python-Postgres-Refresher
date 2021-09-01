# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)
print(odd)

odd.extend([9, 11, 13])
print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])
print(["re"] * 3)

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)
print(odd)

odd[2:2] = [5, 7]
print(odd)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

del my_list[2]
print(my_list)

#Demonstrating remove() and pop() methods
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

print(my_list)
print(my_list.pop(1))
print(my_list)
print(my_list.pop())

my_list.clear() #to delete all elements of list

# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]

print(my_list.index(8))     # Output: 1
print(my_list.count(8))     # Output: 2
my_list.sort()              #sorts the list
my_list.reverse()
print(my_list)              # Output: [8, 8, 6, 4, 3, 1, 0]

#List Comprehension
pow2 = [2 ** x for x in range(10)]
print(pow2)