name = input("Enter Your Name : ")
print("Welcome ", name, "to Adventure game")
answer = input("It is Dirt Road Choose You want to Go Right or Left: ").lower()
if answer == "left":
    answer = input("Yor arrived at river choose walk or swim: ").lower()
    if answer == "swim":
        print("Crocodiles are there in the River You lost ")
    elif answer == "walk":
        print("You walked many miles you ran out of water ,You lose")
    else:
        print("Input invalid You lose")

elif answer == "right":
    answer = input("Yor arrived at bridge choose cross or back: ").lower()
    if answer == "cross":
        answer = input("Met a stranger Yes/No: ").lower()
        if answer == "yes":
            print("Stranger gave you jackpot,You Won")
        elif answer == "no":
            print("You lose")
        else:
            print("invalid Input You lose")
    elif answer == "back":
        print("You go back ,You lose")
    else:
        print("Input invalid You lose")
else:
    print("Your Input is invalid ,You lose")
