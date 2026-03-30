#conditional statements
#if-elif-else
#if the statement is not true in if then we go for elif
age=20
if (age >= 18):
    print ("can vote")
    print ("can drive")

#if → first condition
#elif → another condition if the first is false. (checks multiple condtions)
#else → runs if all conditions are false,written at last and only once.

light="pink"
if (light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")
print("end of the code")

marks=int (input("Enter Your Mark:"))
if(marks>=90):
    grade ="A"
elif(marks>=80 and marks <90 ):
    grade ="B"
elif(marks>=70 and marks <80):
    grade ="C"
else:
    grade ="D"
print("grade of the students ->", grade)
    
# #nesting = Placing one statement inside another.
# #Same line/level → not nesting , Inside (indented) → nesting
age=88
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

a= 5
if a<0:
    print("Negative")
elif a>0:
    print("Positive")
else:
    print("Zero")
    
