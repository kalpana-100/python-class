# #looping = doing any tasks in order repeteadly. 
# # Types: for loop, While loop
# #indentation =space        #indentation block,       indentation expexted error= tab key
# for i in range(0,10,2):     #2,4,6,8
#     print(i)

# for i in range(10):        #by default starts with 0 and no gaps like 1,2,3,4
#     print(i)

# fruits=["apple","banana","kiwi","orange"]
# for i in range (0,len(fruits)):
#     print(fruits[i])

# vegetables=["beans","pumpkin","potato","tomato","cabbage"]
# # for i in range (0,len(vegetables)):
# #     print(vegetables[i])

# #for each loop
# for v in vegetables:
#     print(v)

# #while loop = checks conditions "t" or "f"
# a=0
# while a<=10:
#     print(a)
#     a=a+1

# a=0
# while a<=10:
#     print(a)
#     a=a+2

#nested loop
'''
*
* *
* * *
* * * *
'''
# for r in range (5,0,-1):
#     for c in range(0,r):
#         print("*",end =" ")
#     print("\n")

#Task
#if else , experiment on looping
#print multiplication table of number input by user

'''
1*1=1

'''
#In Python, range(start, stop) does NOT include the stop value.
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num, "x", i, "=", num * i)



