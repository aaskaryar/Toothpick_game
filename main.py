print("WELCOME TO THE GAME!")
print("*"*13)

player_1 = input("enter player 1's name: ")
player_2 = input("enter player 2's name: ")
count = 13 

while True:
    print("| " * count)
    print(f"There are {count} toothpicks left")
    move_player1 = int(input(f"How many do you take, {player_1}? ") )
    while move_player1 not in range(1,4):
        move_player1 = int(input(f"Only choose 1,2,3! How many do you take, {player_1}? ") )
    count -= move_player1
    if count <= 0:
        print(f"{player_1} Wins the game!")
        break


    print("| " * count)
    print(f"There are {count} toothpicks left")
    move_player2 = int(input(f"How many do you take, {player_2}? "))
    count -= move_player2
    while move_player2 not in range(1,4):
        move_player2 = int(input(f"Only choose 1,2,3! How many do you take, {player_2}? ") )

    if count <= 0:
        print(f"{player_2} Wins the game!")
        break

print("GAME OVER!!")

        

    
