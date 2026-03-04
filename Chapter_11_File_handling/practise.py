# def write_log(message):
#     with open("log.txt", "a") as f:
#         f.write(message + "\n")

# def read_logs():
#     with open("log.txt", "r") as f:
#         for line in f:
#             print(line.strip())

# # writing logs
# write_log("User logged in")
# write_log("File uploaded")
# write_log("Payment processed")

# # reading all logs
# print("---- ALL LOGS ----")
# read_logs()
# ```
# ```
# ---- ALL LOGS ----
# User logged in
# File uploaded
# Payment processed
# ```

# ---

# Question 7

# **Q7.** Write a program that:
# 1. Takes a `filename` from user input
# 2. Asks how many lines they want to write
# 3. Takes each line as input and writes it to the file
# 4. After writing — reads the file back and prints each line with a **line number**

# Expected output:
# ```
# Enter filename: notes.txt
# How many lines? 3
# Enter line 1: Python is awesome
# Enter line 2: File handling is easy
# Enter line 3: I love coding

# file_name = input("Enter the file name : ")
# lines = int(input("How many lines do you want to write? : "))
# with open(f"{file_name}" , "w") as f:
#     for i in range(0,lines):
#         line = input(f"Enter {i+1} line : \n") 
#         f.write(f"{line}\n")
# with open(f"{file_name}" , "r") as f:
#     for line in f: 
#         print(line.strip())


file_name = input("Enter the file name : ")
lines = int(input("How many lines do you want to write? : "))
with open(f"{file_name}" , "w") as f:
    for i in range(0,lines):
        line = input(f"Enter {i+1} line : \n") 
        f.write(f"{line}\n")
with open(f"{file_name}" , "r") as f:
    for i, line in enumerate(f , start = 1):   #enumerate is used to mark index and value of each line
        print(f"{i} : {line.strip()}")

# problem 2: 