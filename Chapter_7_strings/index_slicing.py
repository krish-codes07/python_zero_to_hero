text = "krish"
# print(text[0])  #k
# print(text[1])  #r
# print(text[2])  #i
# print(text[3])  #s
# print(text[4])  #h
#string[start : stop] , stop is excluded just like in range 
print(text[0:5])
print(text[2:4])

# text = "python"     #this is not allowed and will give error
# text[0] = "j"

#correct way
text = "python"
next_text = "j" + text[1:]
print(next_text)

text = "python programming" 
print(text.upper())  #all letters in uppercase print
print(text.lower())  #all letters in lowercase print
print(text.strip())  #removes spaces
print(text.replace("python","java"))  #replaces the first string with the second string
print(text.split()) #splits the strings separately using commas
print(len(text))