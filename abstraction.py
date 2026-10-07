from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    

class Car(Vehicle):
    def start(self):
        print("car is starting")

class Bike(Vehicle):
    def start(self):
        print("bike is starting..")


c = Car()
b = Bike()



c.start()
b.start()