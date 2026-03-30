str1="This is a string. \tWe are creating it in python." #\n for line break.  \t for tab space.
print(str1)

#basic operations
#1)concatenation
val1="Infomax"
val2="college"
final_val= val1 +" " + val2
print(final_val)

#2) length of string
print(len(val2))
print(len(final_val))

#slicing
Name="Infomax college"
# print(Name[0:4])
print(Name[:8])
print(Name[8:])

#string functions
# 1. endswith("er.") = Checks if the string ends with specific letters.
str="I am a coder."
print(str.endswith("er."))      #True

#invalid example 
name="kalpana 26"
print(name.endswith("er."))      #False

#2. capitalize()    = Makes the first letter of the string capital, and the rest small.
var="i am a painter."
print(var.capitalize())         #I am a painter.

#3. replace(old, new)   = Finds a word/letter and replaces it with something else.
Str="I am a dancer."
print(Str.replace ("dancer","coder"))  # I am a coder.

#4. find(word) = Finds where a word starts and gives you its position number.
str="I am a coder."
print(str.find("am"))

#5. count("am")  = Counts how many times a word/letter appears.
str="I am a coder"
print(str.count("am"))      #1




