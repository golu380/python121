# #function

# # int a(){

# # }

# def square(x):
#     return x *x

# res = square(5)

# def add1(a,b):
#     return  (a+ b)

# def isEven1 (x):
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(isEven1(34))

# print(add1(12,13))

# print(res)

# square1 = lambda x : x*x
# print(square1(5))

# add = lambda a,b: a + b

# print(add(12,13))

# isEven = lambda x : "even" if x%2 == 0 else "Odd"

# print(isEven(5))

# num = int(input("enter a number"))

numbers = [1,2,3,4,5,6]
def doub(x):
    return x *2

result = map(lambda x: x*2 , numbers)
result1 = map(doub,numbers)
print(list(result))
print(list(result1))
print(list(map(doub,numbers)))

#filters

numbers1 = [12,13,14,15,16,17]

res1 = filter(lambda x: x%2 == 0 , numbers1)

def checkOddEven(x):
    if(x%2 == 0):
        return True
    else:
        return False
    

print(list(res1))
res2 = filter(checkOddEven,numbers1)
print(list(res2))

names = ["kajal","priya","yukta","apoorva","trisha"]

def checkLen(x):
    if(len(x) > 5):
        return True

res2 = filter(lambda x: len(x)>5,names)
res3 = filter(checkLen,names)
print(list(res2))
print(list(res3))

numbers2 = [1,2,3,4,5]
from functools import reduce

def sum(a,b):
    return a+b
res4 = reduce(lambda a,b:a+b,numbers2)
res5 = reduce(sum,numbers2)
print(res4)
print(res5)

