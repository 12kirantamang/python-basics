info  = {
    "key" : "value",
    "name" : "kiran",
    "learning" : "python"
}
# print(info["key"])
info["key"] = "tamang"
print(info)

null_dic = {}
null_dic["name"] = "kiran"
print(null_dic)

# nasted dictionary
# students.key() Return all the value
# student.values() #Return all values
# stu
students = {
    "name" : "kiran",
    "sub" : {
        "py" : 76,
        "java": 34,
    }
}
new_students = {"city" : "kathmandu"}
students.update(new_students)
print(students)
# print(students.keys())
# print(list(students))
# print(list(students.values()))
# print(list(students.items()))
# print(students.get("name"))

dic = {
    "apple" : ("the fruit", "it is good for health"), 
    "cow" : "the animal",
    "city" : "the palce of name"
}
print(dic)
print(list(dic))
print(tuple(dic))

user = {
    "name":input("enter your name:"),
    "age" :input("enter your age:"),
    "city":input("enter your city:")

}
print(user)