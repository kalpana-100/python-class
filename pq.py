# #practice
# #string functions
# #write a program to input 2 numbers and print their sum.
# fnumber=int(input("Enter first number: "))
# Lnumber=int(input("Enter second number: "))
# print("sum =",fnumber+Lnumber)

# #WAP to input user's first name and print its length.
# name=input("Enter Your Name:")
# print(name)
# print ("The length of your name is:",len(name))

# #WAP to find occurance $ of a string.
# var="i am a $string."
# print(var.count("$"))

# #Conditional Statements
# #WAP to check whether number input by user is odd or even.
# Num=int(input("Enter a number:"))
# if Num%2==0:
#     print("The number is even. ")
# else:
#     print("The number is odd.")

# #find the greatest number of there 
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if(a>=b and a>=c):
#     print("first number is largest",a)
# elif(b>=c):
#     print("Second is the largest",b)
# else:
#     print("Third is the largest",c)

#WAP to find whether a number is multiply of 7 or not.
# num=int(input("Enter a number:"))
# if (num%7==0):
#     print("Your Number is Multiply by 7:")
# else:
#     print("Your number is not multiply of 7:")

#arithmetic operations
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     print (f"{num1-num2}")

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1 / num2  

# print(add(num1, num2))
# print(subtract(num1, num2))
# print(multiply(num1, num2))
# print(divide(num1, num2))

#function to find largest of the numbers
def larg_num(numbers):
    maxi=numbers[0]
    for i in range (len(numbers)):
        if maxi<numbers[i]:
          maxi=numbers[i]
    return maxi
numbers=[30,36,70,75,48]
print(larg_num(numbers))
    


