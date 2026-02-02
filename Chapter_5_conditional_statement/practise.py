# Problem 1: Even or Odd
a = int(input("Enter a number to check even or odd: "))
if a % 2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")


# Problem 2: Largest of Two Numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(x, "is greater than", y)
elif x == y:
    print("Both numbers are equal")
else:
    print(y, "is greater than", x)


# Problem 3: Grading System
marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Problem 4: Login System
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
