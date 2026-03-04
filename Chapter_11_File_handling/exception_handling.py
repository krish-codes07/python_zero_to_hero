# the process of handling the error occuring while file operations are performed by using try and except
# FileNotFoundError  → file doesn't exist
# ValueError         → wrong type of value (e.g. int("hello"))
# ZeroDivisionError  → dividing by zero
# TypeError          → wrong data type used
# IndexError         → accessing list index that doesn't exist
# KeyError           → accessing dict key that doesn't exist
# PermissionError    → no access rights to file


# try:
#     with open("ghost.txt" , "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("this file does not exists. please try again!")

# #different types of error requires different uses of except

# try:
#     file_name = input("Enter the file name : ")
#     with open(f"{file_name}" , "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("The File does not exists.Please try again!")
# except PermissionError:
#     print("sorry you don't have permission for this operation.")

# using else and finally 

# try:
#     file_name = input("enter the name of the file : ")
#     with open(f"{file_name}" , "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("sorry this file does not exists.")

# else : # this block will run only if there is no error.
#     print("File read successfully.")

# finally:    # finally : this block will always run even if there is error or not.
#     print("program has finished successfully.")

#solving problem 7 using try else finally to handle all the errors efficienly

try:
    print("program to divide numbers : ")
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print("Result : ", a/b)
except ValueError:
    print("you entered the wrong value, only enter integer value.")
except ZeroDivisionError:
    print("second number can't be zero, Try again!")
else: 
    print("program successfully completed!")
finally:
    print("calculation completed.")