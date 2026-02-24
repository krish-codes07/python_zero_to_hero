# list is a container to store values of any data types 
friends = ["apple","orange",5,345.06, False,"aakash", "rohan"]
print(friends[0])  

friends[0] = "sev bhujiya"
print(friends[0]) #in strings we cannot change the existing value (immutable)
                    # but in list we can change the value (mutable)

print(friends[1:4]) #list is the same as string but we can perform modifications in lists 
                    # just like indexing 
