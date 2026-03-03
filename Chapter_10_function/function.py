# function helps us in code reusability, organization , and abstraction
def morning():
    print("Good Morning!")
morning()

# Function definition 
def avg():
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    c = int(input("enter third number : "))
    print("average  = ",(a+b+c)/3)
avg() #function call  

#function with arguments
def hello(name , ending):
    print("Hello, " + name)
    print(ending)

hello("Krish","Thank You!")
hello("shanks","Thank You!")
hello("roger","Thanks")