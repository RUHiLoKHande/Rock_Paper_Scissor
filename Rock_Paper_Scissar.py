import random

item_list=["Rock","Paper","Scissor"]
user_input=input("Enter your Move : Rock , Paper ,Scissor : ")
computer_input=random.choice(item_list)

print(f"The user move is : {user_input} and computer move : {computer_input}")

if user_input == computer_input:
    print("Both od f you choose same the match tie")
    print("Thank You")
elif user_input=="Rock":
    if computer_input=="Paper":
        print("Paper cover Rocks : Hence Computer Wins")
    else:
        print("Rock hits Scissor : Hence User Wins")
elif user_input=="Paper":
    if computer_input=="Scissor":
        print("Paper cover Rocks : Hence Computer Wins")
    else:
        print("Rock hits Scissor : Hence User Wins")
elif user_input=="Scissor":
    if computer_input=="Rock":
        print("Paper cover Rocks : Hence Computer Wins")
    else:
        print("Rock hits Scissor : Hence User Wins")