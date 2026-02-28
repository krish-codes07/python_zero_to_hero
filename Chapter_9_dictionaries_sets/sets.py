# sets is a collection of non-repetitive elements
#sets are unordered , they are also unindexed(i.e. cannot access elements by index)
# sets cannot contain duplicate values
#items in a set cannot be changed
e = {1, 45, 23} #this is a set , both set and dictionary uses curly braces 
x = {}
print(type(x)) # this is a empty dictionary
s = set() #this is an empty set 
print(type(s))

a = {1,2,3,5,5,3,2,1} # sets only print the non-repetitive value of any number , lets say 
                        # i wrote 2 , 3 times but it will only print 2 one time in set 
print(a,type(a))
 
k = {"krish" , "krish"} 
print(k)