import random
#Basic Variables we need

def warning(attempts, player_guess, secret_word):
  print(f"The character '{player_guess}' is not in the word")
  if attempts == 0:
    print(f"Supreme failure. Give up on life. The word was {secret_word}. How could you not guess that?!")
  elif(attempts == 1):
    print("WARNING! THIS IS YOUR LAST ATTEMPT!")
  elif (attempts < 5):
    print(f"Be mildly alarmed-you have only {attempts} attempts left")
  else:
    print(f'You have: {attempts} attempts left.')

def attempt_maker(word: str) -> int:
    length = len(word)
    if length < 5: return 3
    elif length < 8: return 5
    return 8

def main():
  game_start = True
  restart = False
  secret_word_list = ['Starman', "Meatloaf", "Garfield", "Pikachu", "Garbador", "Tardy"]
  secret_word = random.choice(secret_word_list)
  #This is the list that will be used to store the letters that have been guessed
  player_list = []
  
  #List to store the answer.
  answer_list = ['_'] * len(secret_word)
  
  #Game Start
  print('------Welcome to the game of Word Game------')
  player_name = input('What is your name? ')
  attempts = attempt_maker(secret_word)
  print(f'Hello {player_name}! You have {attempts} attempt(s) to guess the word')
  
  while game_start:
    already_guessed = False
    player_guess = input('Guess a letter: ')
    player_guess = player_guess[0]
    if player_guess.lower() in "ABCDEFGHIJKLMONPQRSTUVXYZ".lower() :
        if player_guess in player_list and player_guess in secret_word: 
            print(f'You alredy guessed {player_guess} correctly!')
            already_guessed = True
        elif player_guess in player_list and player_guess not in secret_word:
            print(f'You have already guessed {player_guess} incorrectly!')
            already_guessed = True
        
        player_list.append(player_guess)
    
        if player_guess in secret_word:
            print(f"Correct! {player_guess} is in the word")
            
            for i in range(len(secret_word)):
                if player_guess == secret_word[i]:
                        answer_list[i] = player_guess
            print(f"Word so far: {''.join(answer_list)}")
            
            if(''.join(answer_list) == secret_word):
                print(f"Congratulations! The secret word is {secret_word}!")
                restart = True
          
  
    # Already_guessed = false and player_guess not in secret_word:
        if not already_guessed and player_guess not in secret_word:
            attempts-=1
            warning(attempts, player_guess, secret_word)
            if attempts == 0:
                restart = True
                
    else:
        print("Invalid input, must be a number")
    #Restart Flag to restart the game
    if restart:
        prompt = input("Do you want to start over? Press R to restart\n")
        if prompt.lower() == 'r':
            #We can probably turn this into a fuction tbh
            player_list = []
            secret_word = random.choice(secret_word_list)
            answer_list = ['_'] * len(secret_word)
            attempts = attempt_maker(secret_word)
            print(f'Hello {player_name}! You have {attempts} attempt(s) to guess the word')
            restart = False
        else:
            game_start = False
            break

main()
