# problem 1: program to take input from user about 7 fruits in a list 
# fruits = []
# f1= input("Enter fruit name : ")
# fruits.append(f1)
# f2= input("Enter fruit name : ")
# fruits.append(f2)
# f3= input("Enter fruit name : ")
# fruits.append(f3)
# f4= input("Enter fruit name : ")
# fruits.append(f4)
# f5= input("Enter fruit name : ")
# fruits.append(f5)
# f6= input("Enter fruit name : ")
# fruits.append(f6)
# f7= input("Enter fruit name : ")
# fruits.append(f7)
# print(fruits)

# using loop to solve the problem
# fruit = []
# for i in range(1,8):
#     i = input("enter fruit name - ")
#     fruit.append(i)
# print(fruit)

#problem 2: take input of 6 student marks and diplay them in a sorted manner 
# marks = []
# for i in range(1,7):
#     a = int(input("Enter marks : ")) 
#     marks.append(a)
# marks.sort()
# print(marks)

# problem 3: check that a tuple cannot be changed
# a = ("krish",12,65)
# a[0] = "hello"    # in the output you can see that a tuple cannot be changed 

# problem 4: find the sum of 4 numbers in a list 

# a = []
# for i in range(1,5):
#     b = int(input("enter numbers : "))
#     a.append(b)
# sum = 0
# for i in range(0,4):
#     sum = sum + a[i]   #we can also use the sum function to find the sum of the list here 
# print("sum of numbers in the list is : ",sum)
# list = [1,2,3,4]
# print(sum(list))

# problem 5: program to count number of zeroes or any number in a tuple
x = [5,0,1,0,3,4,0]
n = x.count(0)
print(n) 