class Animal:

    def eat(self):
        print("animal is eating...")


class Dog(Animal):
    def bark(self,name):
        print(name ," is barking")

    
dog = Dog()
dog.bark("tommy")
dog.eat()


class Person:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print("Name is",self.name)
    
    def fun(self):
        print("person is playing games")


class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks
    
    def display_marks(self):
        print("marks is : ",self.marks)
        print("name is : ",self.name)
    
    def fun (self):
        super().fun()
        print("student is palying chesss...")


student = Student("kajal",90)
student.display_name()
student.display_marks()
print(student.name)
student.fun()