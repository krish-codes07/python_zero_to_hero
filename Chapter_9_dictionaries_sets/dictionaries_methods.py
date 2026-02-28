marks = {
    "krish" : 87,
    "saurabh" : 65,
    "rohit" : 78
}

# print(marks, type(marks))

print(marks.items())  # provides info about key - value pairs
print(marks.keys())   # mention the keys
print(marks.values())   # mention the values
marks.update({"krish" : 95}) # if the key value pair does not exists it will create a new one and add it in th dictionary

print(marks)
print(marks.get("krish2")) #prints none focus on the brackets(small bracket)
print(marks["krish2"]) # this will give error in return value [big bracket]
