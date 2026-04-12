#Looping : Repeating a block of code again and again until a condition is met.
#types: 1. for loop (definite loop): Used when you know how many times to repeat.
#2. while loop (indefinite loop): Used when you repeat until a condition becomes false.

#While Loop
# count=1
# while count<=5:
#     print("Hello World")
#     count+=1
# print(count)

# i=1
# while i <=6:
#     print("Infomax College",i)
#     i+=1
 
 #print number 1 to 5.
# Count=5
# while Count>=1:
#     print(Count)
#     Count-=1
# print("Loop Ended")

# #print number from 1 to 100.
# k=1
# while k <=100:
#     print(k)
#     k+=1

# #print number from 100 to 1.
# k=100
# while k >=1:
#     print(k)
#     k-=1

#print multiplication of number n.
# n=int(input("Enter a number:"))
# num=1
# while num<=10:
#     print(n*num)
#     num+=1

# Print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
indx=0
while indx < len(nums):
    print(nums[indx])
    indx +=1

# Search for a number X in this tuple using loop:
Num=[1,4,9,16,25,36,49,64,81,100,36]
x=36
i=0
while i < len(Num):
    if(Num[i]==x):
        print("FOUND at indx",i)
    else:
        print("Finding..")
    i += 1

