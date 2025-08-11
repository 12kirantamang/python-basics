a = 50
b = 25

print( a == b) #true
print( a != b) #flase
print( a> b) # trure
print( a < b) #flase
print( a >= b) #true
print( a <= b) #flase

#assignment operators
num = 10
# num = num + 5
num += 5 # num = num + 5
print ("this the sum:" ,num)
 #logical operators is worked  in boolean values

a = 20
b = 30
print(not (a > b)) #true
print(not False) #true
print (not True)

val1 = True
val2 = False
print("and opetator:", val1 and val2 )#and operator
print("or operator:", val1 or val2) #or operator


print("or opetator:", (a == b) or (a > b)) #or operator

#type conversion
a = 30
b = 70.3
sum = a+b
print(sum)

#string is not possible to add with int
a,b = 10, "20"
c =int(b)
sum = a + c
print(sum)
print(type(b))