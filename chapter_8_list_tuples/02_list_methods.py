friends = ["apple","orange",5,345.06, False,"aakash", "rohan"]
print(friends)

friends.append("krish")
print(friends)

l1 = [1,34,56,78,21]
# l1.sort() # sorts the numbers in ascending order
# l1.reverse() # sorts the numbers in descending order

l1.insert(2,45) # insert the element 45 in the list such that 
                # its index becomes 3 in the list
print(l1) 

# l1.pop(3)
print(l1.pop(3)) # it returns the value that is being popped/deleted from the list
print(l1)