# person={
#     "name":"Alice",
#     "age":"28",
#     "gender":"female",
#     "fav_fruits":["Cherry","Banana","Orange","Kiwi"]
# }
# # print(len(person))
# # Dictionaries are unordered (conceptually) and not index-based.
# person["fav_fruits"][0]="cherry"
# print(person["fav_fruits"])

# # person ["name"]="kushal"
# print (person["name"])

#     #person.get will not allow to change.
# print(person.get("name"))
# #print(person["name"])

# print(len(person))

# for k,v in person.items():
#     print(f'{k}={v}')

# for _,v in person.items():
#     print(v)

#Nested Dictionary
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)

# myclass={
#     "name":{
        
#     }
# }

#Dictionary : they are used to store data value in key:value pairs.
info={
    "name":"Kalpana Rana",
    "age":22,
    "Female":True,
    "fav_fruits":["Kiwi","Orange","Banana","Mango"]

}
info["age"]=20    #overwrite
print(info)

# Nested Dictionary
students={
    "name":"Lana",
    "subjects":{
        "phy":66,
        "chem":85,
        "maths":80
    }
}

print(students)
print(students["subjects"])

#dictionary Methods
#myDict.key()  = returs all key value.

