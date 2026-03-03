# problem 1: add two number using function
# def add(a,b):
#     return a+b
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = add(a,b)
# print("The Sum is : ",c)

# # problem 2:calculate bill using function keep the tip percent in mind 
# def calculate_bill(amount , tip_percent = 10):
#     amount + ((amount)/100)*tip_percent
#     print(f"Bill with default tip is : {amount + tip_percent}")
#     print("Bill with tip is : ",amount + ((amount)/100)*tip_percent)
# amount = int(input("Your amount is : "))
# tip_percent = int(input("enter the tip (in percent): "))
# calculate_bill(amount , tip_percent)

# retry 
# def calculate_bill(amount , tip = 10):
#     return amount + (amount/100)*tip
# amount = int(input("Your amount is : "))
# print(f"bill with default tip is : {calculate_bill(amount)}")
# a = int(input("do you want to add tip? for yes enter 1, for no press 2 : "))
# if a==1:
#     b = int(input("enter tip percent : "))
#     print(f"bill with additional tip is : {calculate_bill(amount , b)}")
# else:
#     print("thank you")

# problem 3:ticket booking system
# def book_ticket(name , destination , seat_class = "economy" , meal = "veg"):
#     return f"{name} | {destination} | {seat_class} | {meal}"
# a = book_ticket("krish","daltonganj")
# b = book_ticket("krish","daltonganj","first class","non-veg")
# c = book_ticket(destination="delhi",name="krish",meal="non-veg",seat_class="vvip")  #even if arguments are in different order if referred directly 
#                                                                                     #then their value will be assigned in order 
# print(a)
# print(b)
# print(c)

# now moving on to what if there is indefinite number of arguments

# def total(*numbers):
#     print(numbers)
#     print(type(numbers))
# total(10,20,30)

# #problem 4: find sum of n numbers using *args
# def add(*number):
#     result = 0
#     for num in number:
#         result += num
#     return result
# a = add(10,20,30)
# print(a)

#same as above 
# def add(*args):
#     return sum(args)
# a = add(5,6,7,8,9)
# print(a)     #we can also use normal paramters with *args but normal parameter must come first
# problem 5: make a order summary of a customer in a shop
# def order(customer , *items):
#     print(f"Customer : {customer}")
#     print(f"items : {number}")
#     print(f"items ordered : {items}")
# customer = input("what is your name? : ")
# number = int(input("how many items? : "))
# item_list = []
# for i in range(0,number):
#     item = input(f"enter {i+1} item: ")
#     item_list.append(item)
# order(customer,*item_list)

# problem 6: determine the cart total of a customer
# def cart_total(customer, *total):
#     print(f"Customer: {customer}")
#     print(f"Items: {len(total)}")          #len() instead of number
#     return f"{customer}'s cart total: ₹{sum(total)}"  #return not print

# name = input("Enter customer name: ")
# number = int(input("Enter no. of items: "))

# total = []
# for i in range(number):
#     price = int(input(f"Enter price of item {i+1}: "))
#     total.append(price)                    #collecting prices

# result = cart_total(name, *total)          #* unpacks the list
# print(result) 

#using ** as a dictionary for key value pairs 

# def show_info(**dict):  #if we use ** then python automatically pack all the arguments in the dictionary
#                         #with key value pairs 
#     print(dict)
#     print(type(dict))
# show_info(name = "krish",age = 19 , city = "Delhi")

# how to use for loops in ** function
# def show(**args):
#     for key, value in args.items():  #here key, value is needed because dictionary contains value in pairs sor for key : value , we need two variables 
#                                         #so if we ddon't write key, value we won't be able to store the pairs and print them ,
#                                         #keep this is mind always don't forget 
#         print(f"{key} : {value}")
# show(name = "krish" , age = 19 , city = "DTO")

# problem 7:program to show profile using *,** args
def create_profile(name , **details):
    print(f"\nName : {name}")
    for key,value in details.items():
        print(f"{key} : {value}")
name = input("Enter your name : ")
detail = {}
n = int(input("enter how many details you want to enter : "))
for i in range(0,n):
    key = input("Enter details like age,city or any other info : ")
    value = input("Enter value :")
    detail[key] = value
create_profile(name , **detail)

