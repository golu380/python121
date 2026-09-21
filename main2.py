numbers = {12,1,3,1,45,6,7}
print(numbers)

dic = {
    "key":"value"
}

print(dic)

emp = {}
print(type(emp))

emps = set()
print(emps)
print(type(emps))

# print(numbers[0]) we can not access because it is unordered

for i in numbers:
    print(i)

set1 = {10,20,30}
print(set1)
set1.add(40)
print(set1)

set1.update([50,60,70])
print(set1)

set1.remove(20) # will throw error when element is not present
print(set1)
set1.discard(100)
print(set1)

set1.pop()
print(set1)

a = {1,2,3,4}
b = {3,4,5,}

c = a.union(b)
print(c)
print(a  | b)
d = a.intersection(b)
print(d)
print(a & b)

print(a.difference(b))
print(b.difference(a))
print(a-b)
print(b-a)

print(a.symmetric_difference(b))