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

# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#     def withdraw(self,amount):     #amount as parameter because it is getting value outside the class
#         if(amount > self.balance):     #checks if the balance is sufficient to perform withdrawal
#             print("Insufficient bank balance!")
#         else:
#             self.balance -= amount
#             print(f"Your remaining bank balance is {self.balance}")
#     def deposit(self,deposited):
#         self.balance += deposited
#         print(f"Your Current balance is {self.balance}")
#     def show(self):
#         print(f"{self.name} : current balance : {self.balance}")

# name = input("Customer Name : ")
# balance = int(input("Your Balance : "))
# w = BankAccount(name , balance)
# a = int(input("Do You want to 1. withdraw\n 2. deposit \n 3. check balance? "))
# if(a == 1):
#     withdrawal = int(input("How much do you want to withdraw? : "))
#     w.withdraw(withdrawal)
# elif(a == 2):
#     deposited = int(input("How much do you want to deposit? : "))
#     w.deposit(deposited)
# elif(a == 3):
#     w.show()

# problem 3: student report card show student info , average marks, total marks, grade 
class Student:
    def __init__(self,name, roll_no , *marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_total(self):
        return sum(self.marks)
    def get_average(self):
        return round(self.get_total()/5,2)
    def get_grade(self):
        average = self.get_average()
        if(average >= 90):
            return "A"
        elif(average >= 75 and average < 90):
            return "B"
        elif(average >=60 and average < 75):
            return "C"
        elif(average < 60):
            return "F"
    def show_report(self):
        print("-----Report Card-----")
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Total : {self.get_total()}")
        print(f"Average : {self.get_average()}")
        print(f"Grade : {self.get_grade()}")
name = input("Student name : ")
roll_no = int(input("student roll no : "))
marks = []
for i in range(5):
    m = int(input(f"enter marks of {i+1} subject : "))
    marks.append(m)
s = Student(name , roll_no , *marks)
s.show_report()