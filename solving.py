#problem 1: take two number and print their total 
# a = int(input("enter first number - "))
# b = int(input("enter second number - "))
# print("total of two number is = ",a+b)
# print("difference of two number is = ",a-b)
# print("multiplication of two number is = ",a*b)
# print("division of two number is = ",a/b)

# problem 2: take a float input and convert it into string and int and print its type
# a = float(input("enter a number - "))
# b = int(a)
# c = str(a)
# print(type(a),a)
# print(type(b),b)
# print(type(c),c)

#problem 3: take a input from user and print its square and cube 
# a = int(input("enter a number - "))
# print("square of the number is - ",a*a)
# print("cube of the number is - ",a*a*a)

# problem 4: take input of 5 subject and find the average marks 
# print("enter the marks of 5 subject in order - ")
# n = int(input("enter number of subjects - "))
# total = 0
# for i in range(0,n):
#     if a<0:
#         print("")
#     a = int(input("enter marks - "))
#     total = total + a
# print("total marks is - ",total)
# print("averag marks is - ", total/n)





# problem 5: check positive negative and zero 

# a = int(input("enter a number - "))
# if a >0 :
#     print("the number is positive")
# elif a<0:
#     print("the number is negative")
# elif a==0:
#     print("the number is zero ")
# else:
#     print("invalid input")

# problem 6: program to print the max number 
# a = int(input("enter first number - "))
# b = int(input("enter second number - "))
# if a>b:
#     print("a",a,"is greater than b",b)
# else:
#     print("b",b,"is greater than a",a)

# problem 7: program to check vowel or consonant
# a = str(input("enter an alphabet - "))
# if a == 'a' or a == 'e' or a=='i' or a == 'o' or a== 'u':
#     print("the entered alphabet is vowel")
# else:
#     print("the entered alphabet is consonant")

# problem 8: print from 1 to 50 using loop
# for i in range(1,51):
#     print(i)

# problem 9: print even number from 1 t 100
# for i in range(1,101):
#     if i%2==0:
#         print(i)

# problem 10: print sum of n natural numbers 
# n = int(input("enter number of terms - "))
# add = 0
# for i in range(1,n):
#     add += i
#     print(add)

# proboem 11:print multiplication table of a number
# a = int(input("enter a number to print its table - "))
# for i in range(1,11):
#     print(a,"*",i, " = ",a*i)

# problem 12: count the digits of a number given by user 
# a = int(input("enter a number to check its digit count - "))
# i=0
# while a!=0:
#     a = a%10


# problem 13: to print star pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# problem 14: palindrome checker 

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
a = input("enter word : ")
print(is_palindrome(a))

# problem 15: creating a calculator function 
def calculate(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        print("wrong input! try again.")
operator = input("choose which operation to perform +,-,*,/ : ")
a = int(input("enter first number : "))
b = int(input("enter first number : "))
c = calculate(a,b,operator)
print(c)