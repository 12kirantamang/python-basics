import random

# randNum = random.rand.int(1, 20)
# # print(randNum)

# while True:
#     userchoice = int(input("guess the number:"))
#     if userchoice == target:
#         print("success : correct Guess!!")
#         break
#     if(userchoice < target):
#         print("your choice is small guess bigger")
#     elif(userChoice < target):
#            print("your number is too big guess small") 

#     else:
#          print("you are dumb ass mf")        
import random

target = random.randint(1, 20)
# print(target)

while True:
    user_input = input("Guess the number or quit (Q): ")

    if user_input.upper() == "Q":
        print("Game over! Thanks for playing.")
        break

    # Now safely convert to int because input isn't 'Q'
    try:
        userchoice = int(user_input)
    except ValueError:
        print("Please enter a valid number or 'Q' to quit.")
        continue

    if userchoice == target:
        print("Success: correct guess!!")
        break
    elif userchoice < target:
        print("Your number is too small — guess bigger.")
    elif userchoice > target:
        print("Your number is too big — guess smaller.")
