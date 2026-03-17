# problem 1: show information in formatted way
# def display_info():
#     name = input("Enter your name : ")
#     age = int(input("Enter your age : "))
#     city = input("Enter which city do you live in? : ")
#     print("\n---- Your Information ----")
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"City : {city}")
# display_info()

# using error handling problem 1
# def display_info():
#     name = input("Enter your name : ")
#     try:
#         age = int(input("Enter your age : "))
#     except(ValueError):
#         print("invalid input. please try again!")
#         return
#     city = input("Enter which city do you live in? : ")
#     print("\n---- Your Information ----")
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"City : {city}")
# display_info()

# problem 2: find area of rectangle
# def rectangle_area():
#     try:
#         length = int(input("Enter length: "))
#     except ValueError:
#         print("invalid input .please try again!")
#         return
#     try:
#         breadth = int(input("enter breadth : "))
#     except ValueError:
#         print("invalid input .please try again!")
#         return
#     area = length * breadth
#     print(f"Area of Rectangle : {area}")
# rectangle_area()

# problem 3: celsius to fahrenheit

# def converter():
#     try:
#         temp = float(input("Enter temperature in celsius : "))
#     except ValueError:
#         print("invalid input. please try again!")
#     fahrenheit = (temp * (9/5))+32
#     print(f"Temperature in fahrenheit : {fahrenheit}")
# converter()

# problem 4: perform arithmetic operations on two numbers
def arithmetic_operations():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"Addition : {a+b}")
    print(f"Subtraction : {a-b}")
    print(f"Multiplication : {a*b}")
    print(f"Division : {a/b}")
    print(f"Floor Division : {a//b}")
    print(f"Modulus : {a%b}")
    print(f"Power : {a**b}")

arithmetic_operations()