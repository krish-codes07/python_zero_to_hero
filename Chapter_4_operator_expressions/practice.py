# Problem 1: take two inputs from user and perform arithmetic operations

sign = input("Which operation do you want to perform? +, -, /, %, * : ")
print("Enter two inputs to perform arithmetic operations - ")

a = int(input("Enter first number - "))
b = int(input("Enter second number - "))

if sign == "+":
    print("You have chosen +")
    print("Sum of two numbers is:", a + b)

elif sign == "-":
    print("You have chosen -")
    print("Subtraction of two numbers is:", a - b)

elif sign == "/":
    print("You have chosen /")
    if b == 0:
        print("Division by zero is not allowed")
    else:
        print("Division of two numbers is:", a / b)

elif sign == "*":
    print("You have chosen *")
    print("Multiplication of two numbers is:", a * b)

elif sign == "%":
    print("You have chosen %")
    if b == 0:
        print("Modulus by zero is not allowed")
    else:
        print("Remainder is:", a % b)

else:
    print("ERROR!! Invalid input, please try again.")

# program to check which is greater 
a=5
b=10
print("which is greater?")
if a>b:
    print("a is the greater one - ",a)
else:
    print("B is the greater one - ",b)