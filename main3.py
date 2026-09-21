student = {
    "name":"priya",
    "course":"it22",
    "age":22
}

print(student)
print(type(student))

#accessing the elements

print(student["name"])
print(student["age"])
print(student.get("course"))
student["city"] = "Mumbai"
print(student.get("city"))
print(student)
student["age"] = 19
print(student)
a = student.pop("city")
print(student)
print(a)
print(student.keys())
print(student.items())
print(student.values())

student1 = {"name":"kajal","class":"xiii"}

student.update(student1)
print(student)
student.clear()
print(student)

student3 = {
    "student4":{
        "name":"kajal",
        "course" : "it"
    },
    "student5":{
        "name":"priya",
        "course": "It"
    }
}

print(student3["student4"]["name"])
print(student3["student5"]["name"])


# using for loop
student6 = {
    "name":"priya",
    "course":"it22",
    "age":22
}
print("student6")
print(student6.items())
for key,value in student6.items():
    print(key,": ",value)

numbers = {10,20,30,10,20,30}
print(numbers)

# important question

b = {} #is it dict or set

print(type(b))

c = set()
print(type(c))
numbers.add(40)
print(numbers)
print(numbers.update([50,60,70]))
print(numbers)
numbers.remove(20)
print(numbers)
numbers.discard(20)
print(numbers)
numbers.discard(30)
print(numbers)

print(numbers.pop())
print(numbers)

a = {1,2,3,4,5}

b = {4,5,6,7,8,9}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(b.difference(a))
print(a-b)
print(b-a)