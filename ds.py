# #Data Structure (multiple data structure)
# fruits=["apple","banana","kiwi","orange"]
# fruits.append("mango")
# print(fruits)

# print(fruits[-1]) #last item

# fruits[0]="grapes" #first item
# print(fruits)

# fruits.pop() #remove last items
# print(fruits)

# #list Key Features: - Ordered (keeps insertion order) - Mutable (you can change elements) - Allows duplicate values []
# # tuples : A tuple is an ordered - immutable (cannot change after creation) - Allows duplicates ()
# # set : Unordered (not structured) cant be index - No duplicate values (removes duplicates ) - Mutable (can add/remove items) {}

# marks= [22.2,20.0,60.4,23.2,80.1]
# marks[0]="99.9"

# print(marks)
# print(type(marks))
# print (marks[0])
# print(marks[-1])
# print(marks [0:4])

#list methods
# list=[2,1,3]
# list.append(4)             #to add number on list
# print (list.sort())           #ascending order
# print(list.sort(reverse=True))     #descending orde
# print(list)

List=['a','b','c','d','e','f','g']      #reverse
List.reverse()
print(List)

num=[2,1,3]
num.insert(1,5)   # 5 is the value to be added in index '1'
print(num)

num=[2,1,3]
num.pop(1)
print(num)

#tuples
tup=(2,3,4)
print(type(tup))          #tuple
print(tup[0])
# tup[0]=5 #invalid becuase tuples are immutable   tup=(1,) "," is compulsory for tuples if there is only one value.

#dictionary
