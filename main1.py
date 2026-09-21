student = {
    "name":"Rahul",
    "age":25,
    "course":"python"
}

print(student)
print(type(student))

print(student["name"])
print(student["age"])
print(student["course"])

print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

student["city"] = "mumbai"
print(student)
student["age"] = 20
print(student)
student["city"] = "pune"
print(student)

#poping

student.pop("city")
print(student)

# student.clear()
# print(student)

print(student.keys())
print(student.items())
print(student.values())

for key, item in student.items():
    print(key,":",item)


students = {
    "student1":{
       "name":"Amit",
       "age":25
    },
    "student2":{
        "name":"tanmay",
        "age" : 22
    }
}

print(students)
print(students["student1"]["name"])
print(students["student2"]["name"])