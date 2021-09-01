set1={1, 2, 3}
set2={1.0, "Hello", (1, 2, 3)}

#adding elements
set1.add(5)
print(set1)

set1.update([6,5,7,8],(9,12))
print(set1)

#Removing elements from a set
set1.discard(12)
print(set1)

set1.remove(2)
print(set1)

#set1.remove(2)     this gives error as 2 isn't present in set
#print(set1)

set1.pop()
print(set1)

set2.clear()
print(set2)

#Python Set Operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a|b,'(union)')                #or a.union(b)
print(a&b,'intersection')           #or a.intersection(b)
print(a-b,'difference')             #or a.difference(b)
print(a^b,'symmetric difference')   #or a.symmetric_difference(b)