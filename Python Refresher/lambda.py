#lambda with filter

def checkEven(num):
    if num%2==0:
        return True
    else:
        return False

lst=[1,2,3,4,5,6,7,8,9]
new_lst=list(filter(checkEven,lst))
print(*new_lst)

#lamda with map()

squared_lst=list(map(lambda x:x**2, new_lst))
print(*squared_lst)