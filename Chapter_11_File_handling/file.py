# Mode    Meaning                          File exists?    File missing?
# ─────────────────────────────────────────────────────────────────────
# "r"   → read only                        opens it        ❌ ERROR
# "w"   → write (fresh start)              overwrites it   creates new
# "a"   → append (add to end)              adds to end     creates new
# "r+"  → read AND write                   opens it        ❌ ERROR

# f = open("readme.md" , "r") #if we use f = .... ; then we have to manually close the file 
# with open("myfile.txt" , "mode(r,w,a,r+)") as f: ; we use this so that the file automatically closes
    #do stuff here 
# file automatically closes

with open("myfile.txt" , "w") as f:
    f.write("Hello this is line 1\n")
    f.write("Hello this is line 2\n")
    f.write("Hello this is line 3\n") 

with open("myfile.txt" , "r") as f:
    content = f.read()        #reads the whole file as one string 
    print(content)

with open("myfile.txt" , "r") as f:
    line1 = f.readline() #reads first line
    line2 = f.readline() #reads second line 
    print(line1)
    print(line2)

with open("myfile.txt" , "r") as f:
    line = f.readlines()  #read all lines as list 
    print(line)

# APPENDING TO A FILE :
with open("myfile.txt" , "w") as f: #"w" mode does not erase anything it is used to add content at the end 
    f.write("this is written by using write mode.")

# USING LOOP AND STRIP 
with open("myfile.txt" , "r") as f:
    for line in f:
        print(line.strip())    #strip() removes the \n at the every end of line 
