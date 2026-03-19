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
# class Student:
#     def __init__(self,name, roll_no , *marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def get_total(self):
#         return sum(self.marks)
#     def get_average(self):
#         return round(self.get_total()/5,2)
#     def get_grade(self):
#         average = self.get_average()
#         if(average >= 90):
#             return "A"
#         elif(average >= 75 and average < 90):
#             return "B"
#         elif(average >=60 and average < 75):
#             return "C"
#         elif(average < 60):
#             return "F"
#     def show_report(self):
#         print("-----Report Card-----")
#         print(f"Name : {self.name}")
#         print(f"Roll No : {self.roll_no}")
#         print(f"Total : {self.get_total()}")
#         print(f"Average : {self.get_average()}")
#         print(f"Grade : {self.get_grade()}")
# name = input("Student name : ")
# roll_no = int(input("student roll no : "))
# marks = []
# for i in range(5):
#     m = int(input(f"enter marks of {i+1} subject : "))
#     marks.append(m)
# s = Student(name , roll_no , *marks)
# s.show_report()

# problem 4 : library book system which has methods issue book , Return book , book info 
# class Book:
#     def __init__(self,total_copies , title, author , issued_copies = 0):
#         self.title = title
#         self.author = author 
#         self.total_copies = total_copies
#         self.issued_copies = issued_copies

#     def issue_book(self):
#         if(self.total_copies > 0):
#             self.total_copies -= 1
#             self.issued_copies += 1
#             print(f"Book Issued! Remaining copies {self.total_copies}")
#         elif(self.total_copies == 0):
#             print("No copies available for this book.")
#         else:
#             print("Please choose another book.")

#     def return_book(self):
#         if(self.issued_copies > 0):
#             print("Book Returned.")
#             self.total_copies += 1
#             self.issued_copies -= 1
#             print(f"Total copies = {self.total_copies}")
#         elif(self.issued_copies == 0 ):
#             print("Nothing to return. ")

#     def available_copies(self):
#         if (self.total_copies > 0):
#             return (self.total_copies - self.issued_copies)
        
#     def show_info(self):
#         print("-----Book Info-----\n\n")
#         print(f"Title : {self.title}")
#         print(f"Author : {self.author}")
#         print(f"Total Copies : {self.total_copies}")
#         print(f"issued : {self.issued_copies}")
#         print(f"Avaiable copies : {self.available_copies()}")

# title = input("Enter Book name : ")
# author = input("Author Name : ")
# total_copies = int(input("Copies : "))
# l = Book(total_copies , title , author)
# while(True):
#     a = int(input("What do you want to do?\n1.Issue Book\n2.Return book\n3.Show Info\n4.Exit\n"))
#     if(a == 1):
#         l.issue_book()
#     elif(a == 2):
#         l.return_book()
#     elif(a == 3):
#         l.show_info()
#     elif(a == 4):
#         break

# problem 5:employee salary system and bonuses based on their roles

class Employee:
    def __init__(self , name, role, base_salary):
        self.name = name
        self.role = role
        self.base_salary = base_salary
    def get_bonus(self):
        if(self.role == "Manager"):
            return (self.base_salary*(20/100))
        elif(self.role == "Developer"):
            return (self.base_salary*(15/100))
        elif(self.role == "Intern"):
            return (self.base_salary*(5/100))
        else:
            print("No bonus salary!")
            return 0
    def total_salary(self):
        return self.base_salary + self.get_bonus()
    def show_details(self):
        print("-----Employee Details-----")
        print(f"Name : {self.name}")
        print(f"Role : {self.role}")
        print(f"Base Salary : {self.base_salary}")
        print(f"Bonus : {self.get_bonus()}")
        print(f"Total Salary : {self.total_salary()}")
employee = []
for i in range(3):
    print(f"Employee {i+1} details :")
    name = input("Employee Name : ")
    role = input("Role : ")
    base_salary = int(input("Base salary : "))
    employee.append(Employee(name, role, base_salary))
for emp in employee:
    emp.show_details()