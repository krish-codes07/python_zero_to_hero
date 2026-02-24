a = (1,2,5,6,False,True,"hello",45,45) #because we are using small braces
print(type(a))
b = () #empty tuple
c = (1,) #we have to use , to tell python that it is a single element tuple otherwise
         #it will interpret it as integer class
friends = ("apple","orange",5,345.06, False,"aakash", "rohan")
print(friends[0])
print(a.count(45)) #count number of occurences

print(a.index(45)) # it will give the index number of the element where it is found first , and will not check further 
print(len(a))