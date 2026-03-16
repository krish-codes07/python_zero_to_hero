#problem 1 : make a Student class and display info of different students and also introduce them
# class Student:
#     def __init__(self,name,age,standard):
#         self.name = name
#         self.age = age
#         self.standard = standard
#     def info(self):
#         print(f"Hi i am{self.name} , {self.age} years old , in grade {self.standard}")

    
# name = input("Name of the Student : ")
# age = int(input("Age : "))
# standard = int(input("Standard : "))
# s1 = Student(name , age , standard)
# s1.info()

# problem 2: create a class bankaccount that works just like the atm in the real world

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def withdraw(self,amount):     #amount as parameter because it is getting value outside the class
        if(amount > self.balance):     #checks if the balance is sufficient to perform withdrawal
            print("Insufficient bank balance!")
        else:
            self.balance -= amount
            print(f"Your remaining bank balance is {self.balance}")
    def deposit(self,deposited):
        self.balance += deposited
        print(f"Your Current balance is {self.balance}")
    def show(self):
        print(f"{self.name} : current balance : {self.balance}")

name = input("Customer Name : ")
balance = int(input("Your Balance : "))
w = BankAccount(name , balance)
a = int(input("Do You want to 1. withdraw\n 2. deposit \n 3. check balance? "))
if(a == 1):
    withdrawal = int(input("How much do you want to withdraw? : "))
    w.withdraw(withdrawal)
elif(a == 2):
    deposited = int(input("How much do you want to deposit? : "))
    w.deposit(deposited)
elif(a == 3):
    w.show()