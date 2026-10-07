def greet():
    print("Hi i am from function block")
    print("i am in fun")


def greet1(name):
    return "hello " + name


greet()
greet()
for i in range(5):
    greet()

res = greet1("fahad")
print(res)

print(greet1("lucky"))


# class Student:
#     pass

# student1 = Student()

class Student:
    
    def __init__(self,name1,age,marks):
        self.name = name1
        self.age = age
        self.__marks = marks
    
    def displaydata(self):
        print("student name is: ",self.name)
        print("student age is: ",self.age)
        print("student marks is: ",self.__marks)

    

student1 = Student("lucky",20,80)

print(student1.name)
print(student1.age)
# print(student1.__marks)
print("printing with mentod")
student1.displaydata()
