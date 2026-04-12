#functions (reuseable)
#functions may return value.
# defination and calling
# we can pass parameter and make function dynamic. (params)
# argument data = as many as we data we passed in params. 

# def hi():
#     print("Hello!!")
# hi() #calling function

# def machine(grains):     #parameter
#     print(f"This will give you flour of {grains}")      #f = format
#     return f"This will give you flour of {grains}"
# machine("maize")
# machine("rice")           #argument

# def machine(grains):     #parameter
#     a=False
#     if a:
#        return f"This will give you flour of {grains}" 
#     else:
#         return "Hello"
   
# sudeshna=machine("maize")
# print(sudeshna)

# kalpana=machine("rice")
# print("kalpana")

#define function def..()
# def num(a,b):    #parameter
#     return a+b

# sum_result = num(2,6)    #function call
# print(sum_result)


# #average of three
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# calc_avg(1,2,3)

#1. Function to print the length of a list
# def print_length(lst):
#     print(f"Length of list: {len(lst)}")

# # Example usage:
# my_list = [10, 20, 30, 40, 50]
# print_length(my_list)  # Output: Length of list: 5

#write a function that accepts list as parameter and return the sum of elements in the list.
# def list_sum (a,b):
#     sum=a+b
#     print(sum)
#     return sum
# list_sum(2,2)

# #write a function that accepts list as parameter and return largest number of that list.

# def large_num(numbers):
#     max = numbers[0]
#     for i in range(len(numbers)):
#         if max < numbers[i]:
#             max = numbers[i]
#     return max

# numbers=[20,22,30,19]
# print(large_num(numbers))
   
# #write a function that acepts list as parameter and a key and returns if that key is in the list.
# def search_num(numbers, key):
#     for i in range(len(numbers)):
#         if numbers[i]==key:
#             return "Found"
            
#     return "not found"
    
# print(search_num([1,2,5,8,9],4))
# print(search_num([1,2,88,99,456,80],456))

# # sum of the list
# def list_sum (numbers):
#     sum =0
#     for i in range (len(numbers)):
#         sum=numbers[i]+sum
#     return sum

# print(list_sum([2,3,4,5,6]))
    
# #WAF to print the length of a list. (list is the parameter)
# Countries=["Nepal","Japan","UK","Canada","Korea","China"]
# Heroes=["Thor","Spidy","Iron-man","Hulk"]
# Numbers=[1,2,3,4,5,6,7,8,9,2]

# def print_len(list):
#     print("The length of a list is :",len(list))

# print_len(Countries)
# print_len(Heroes)
# print_len(Numbers)

#WAF to find the factorial of a n.(n is the parameter)
def cal_function(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_function(6)


