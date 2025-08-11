class students:
    # name = "kiran"
    def __init__(self, fullname):
        # print(self)
        self.name = fullname
        print("adding new student in database")


s1 = students("kiran") #object
print(s1.name)
s2 = students("karan")
print(s2.name)
# print(s1.name)  

# class car:
#     color = "blue"
#     brand = "tesla"

# car1 = car()
# print(car1.color) 
# print(car1.brand)   