# to take input from user and print their information
name = input("Enter your name - ")
age = input("enter your age - ")
city = input("which city do you live in ? -")
print("my name is - ",name,"my age is - ",age,"i live in - ",city)

# problem 2 : to make a simple calculator
print("Simple Calculator : \nchoose add,multiply,divide,subtract")
sign = input("What do you want to perform ? -")
print("You hav chosen - ",sign)

if sign == "add":
    a=int(input("first number - "))
    b=int(input("second number- "))
    print("the sum of the given number is - ",a+b)

elif sign == "subtract": 
    a=int(input("first number - "))
    b=int(input("second number- "))
    print("the subtraction of the given number is - ",a-b)

elif sign == "multiply":
    a=int(input("first number - "))
    b=int(input("second number- "))
    print("the multiplication of the given number is - ",a*b)

elif sign == "divide":
    a=int(input("first number - "))
    b=int(input("second number- "))
    if b == 0 :
        print("Error! division for zero is not allowed")
    else: 
        print("the division of the given number is - ",a/b)    #else is required to prevent division from zero.

else:
    print("invalid input!")

# program to print yes no
print("are you a student?")
ans = input("enter 0 for no and 1 for yes - ")                  # bool("0") is True because it's a non-empty string
                                                                # So we must compare strings instead of using bool(input())

if ans == '1':                              #bool("anything") will always be true , while bool("") is considered false because it is empty
    is_student = True
elif ans =='0':                                 
    is_student = False
else:
    is_student = None
    print("invalid input")

print("am i a student you ask? - ",is_student)