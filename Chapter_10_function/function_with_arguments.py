#function with arguments
# def hello(name , ending):
#     print("Hello, " + name)
#     print(ending)

# hello("Krish","Thank You!")

# functions also have return value 
# def hello(name , ending):
#     print("Hello, " + name)
#     print(ending)

# a = hello("Krish","Thank You!")
# print(a) #default return value will be none

# def hello(name , ending):
#     print("Hello, " + name)
#     print(ending)
#     return "Task Done."

# a = hello("Krish","Thank You!")
# print(a)


# default argument value 
def goodDay(name , ending = "Thanks"):  #default value of the parameter is given in the start if the 
                                        # another argument is not passed python will automaticlly 
                                        #assign the defualt value set at the beginning.
                                        #one very important thing to note is that the default 
                                        #argument parameter should always come after the non-default
                                        #parameter , otherwise it will give error
    print(f"hello, {name}")
    print(ending)
goodDay("Krish")
goodDay("Krish" , "goodBye")

#multiple arguments concepts 
# problem 6: determine the cart total of a customer
def cart_total(customer, *total):
    print(f"Customer: {customer}")
    print(f"Items: {len(total)}")          #len() instead of number
    return f"{customer}'s cart total: ₹{sum(total)}"  #return not print

name = input("Enter customer name: ")
number = int(input("Enter no. of items: "))

total = []
for i in range(number):
    price = int(input(f"Enter price of item {i+1}: "))
    total.append(price)                    #collecting prices

result = cart_total(name, *total)          #* unpacks the list
print(result) 
