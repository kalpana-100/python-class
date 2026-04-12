#File I/O (Input/Output) in Python is about reading from files and writing to files.
# Modes:
# "r" → Read (default)
# "w" → Write (overwrites file)
# "a" → Append (adds to file)
# "x" → Create new file (error if exists)
# "b" → Binary mode (e.g., images)
# Use with → it automatically closes the file
#Reading a file: 1) data= f.read() ->reads entire lines  2) data=f.readline() ->reads line by line 

# Read mode:
#f  = open("demo.txt","w")

# line1 = f.readline ()
# print(line1)

# line2 = f.readline ()
# print(line2)

# print(type(data))
#f.close()

# write mode:
#f  = open("demo.txt","w")
#f.write("I am a full stack developer. I love python.")
#f.close()

# append mode:
f  = open("demo.txt","a")
f.write("\nPython is very interesting.")
f.close()
