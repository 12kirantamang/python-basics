marks = [94.4, 20, 60.4, 34.5]
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))

# we can  store str and int in list
# strings is immutabe it mean you cannot changed 
# lists is mutable it means you can changed
student = ["kiran", "shyam", "harry", 23.5]
print(student[0])
student[0] = "karan"
print(student)
print(len(student))
print(type(student))
print(student[2])
print(student[1:3])


#list.append(4) adds one element at the end [2, 1 ,3, 4]
#list.short() sorts in ascending order [1, 2, 3]
#list.sort() in ascending order [1,2, 3]
#list.sort(reverse=ture)sotrs in descending order[3,2,1]
#list.reverse()#reverse list [3,1,2]
#list.insert(idx,el)insert element at index

list = [2, 1, 3]
list.append(4)
print(list)
print(list.sort(reverse=True))
print(list)

fruit = ["banana", "apple", "mango"]
fruit.append("oranange")
print(fruit.sort(reverse=True))
print(fruit)
fruit.remove("banana")
print(fruit)
#tuple
tup = (1, 2, 3, 4, 1, )
print(type(tup))
print(tup.count(1))
movies = []
# movies.append(input("enter 1st Movies:"))
# mov1 = input("enter 1st movies:")
# mov2 = input("enter 2nd movies:")

# mov3 = input("enter 3rd movies:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
# print(movies)

num1 = [1, 2, 3, 4]
num2 = [4, 3, 2, 1]
num1 = list.copy()
num1.reverse()

if (num1 == num2):
    print("this is palindrom")
else:
    print("this not")    


