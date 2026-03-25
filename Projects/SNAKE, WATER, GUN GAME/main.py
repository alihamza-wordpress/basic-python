
computer = -1 
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer ==-1 and you == 1):
        print("You Win")
    elif(computer ==-1 and you == 0):
        print("You Lose")
    elif(computer ==1 and you == -1):
        print("You lose")
    elif(computer ==1 and you == 0):
        print("You win")
    elif(computer ==0 and you == -1):
        print("You win")
    elif(computer ==0 and you == 1):
        print("You lose")
    else:
        print("Something went wrong")
