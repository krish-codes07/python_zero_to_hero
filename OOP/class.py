# A **class** is a blueprint — it defines the structure.
# An **object** is a real thing built from that blueprint.

# class dog:
#     pass 
# dog1 = dog()
# dog2 = dog()
# print(type(dog1))
# print(dog2) 

# class cat:
#     name = "billy"  #here in this class for every object name,age is fixed but we don't want that;
#                     #so for getting different values we will be using __init__ constructor
#     age = 2
# cat1 = cat()
# print(cat1.name) 

class dog:
    species = "mammals"          #class variable same value for every object
    def __init__(self,name,age):
        self.name = name         #instance variable : just for this object
        self.age = age           # self is used to refer to specific object
    def bark(self):
        print(f"{self.name} says : Woof! Woof!")
    def info(self):
        print(f"Name : {self.name}, Age : {self.age}")
dog1 = dog("Bruno" , 4)
dog1.info()
dog1.bark()
dog2 = dog("Tommy" , 5)
dog2.bark()
print(dog1.species)
print(dog2.species)