class Dog:
    def sound(self):
        print("dog is barking")
class Cat:
    def sound(self):
        print("cat is mewing..")



animal = [Dog(),Cat()]

for i in animal:
    i.sound()