# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


#string methods
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)         #list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]

#character count
print('len(str) = ', len(str))                          #len(str) =  4

#common string methods
print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))