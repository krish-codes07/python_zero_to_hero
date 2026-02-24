#problem 1 : print the string entered by the user and its length
text = input("enter a anything: ")
print(text)
print(len(text))

#problem 2: print the first and the last letter of the string 

text = input("enter anything: ")
if len(text) == 0:
    print("empty string")
else:
    print(text[0])
    print(text[-1])

#problem 3: take a string and print its reverse
text = input("enter anything : ")
print(text[::-1])
