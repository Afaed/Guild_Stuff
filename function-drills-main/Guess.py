answer = 5
game_start = True

print("-----Welcome To The Guessing Game!-----")
player_name = input("Wait, um what's your name? \n")

while game_start:

    player_guess = int(input(f"What is the random number {player_name}?\n"))

    if player_guess < answer:
        print(f"Too low {player_name}!")
    elif player_guess > answer:
        print(f"Too High {player_name}!")
    else:
        print(f"Correct {player_name}!")
        game_start = False