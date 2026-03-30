# person={
#     "name":"Alice",
#     "age":"28",
#     "gender":"female",
#     "fav_fruits":["Cherry","Banana","Orange","Kiwi"]
# }
# # print(len(person))
# # indexing is allowed in dictionary.
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
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

myclass={
    "name":{
        
    }
}