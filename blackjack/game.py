#Settings
import random
STARTING_CHIPS = 50
MAX_PLAYERS = 2
MAX_BID = 15

#Initialization
player_hand = []
dealer_hand = []

#game loop settings
game_over = False
game_start = True
dealer_draw = False
#card init
deck = []
card = {}

suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
ranks = ['Ace', 'Jack', 'King', 'Queen']
#TODO: Set the 1 to ace and the 11, 12, 13 cards to king, queen, and jack.
#TODO: Set the values from 11 onwards to 10 
values= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
for suit in suits:
    for value in values:
        card = {'suit': suit, 'value': value}
        deck.append(card)

random.shuffle(deck)

#Program Loop

def shuffle_deck():
    global deck
    random.shuffle(deck)

def winner():
    global player_sum, dealer_sum
    if game_over:
        if player_sum == dealer_sum:
            print("Draw")
        elif player_sum > 21:
            print("BUST!")
        elif dealer_sum > 21:
            print("Dealer busts! You win!")
        elif dealer_sum == 21:
            print("Dealer has blackjack! You lose!")
        elif player_sum == 21:
            print("You win!")
        elif dealer_sum > player_sum:
            print("Dealer wins! They have a higher score more than you!")
        elif player_sum > dealer_sum:
            print("You win!")

def start_game():
    global player_hand, dealer_hand, player_sum, dealer_sum
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_sum = player_hand[0].get('value') + player_hand[1].get('value') 
    dealer_sum = dealer_hand[0].get('value') + dealer_hand[1].get('value')
    print(f"Player has a {player_hand[0].get('value')} of {player_hand[0].get('suit')} and a {player_hand[1].get('value')} of {player_hand[1].get('suit')}")
    print(f"Dealer has a {dealer_hand[0].get('value')} of {dealer_hand[0].get('suit')} showing")

def calc_sum_and_draw(sum: int, hit_card: dict, name: str):
    score = sum+hit_card.get('value')
    return score, f"{name} drew a {hit_card.get('value')} of {hit_card.get('suit')}", f"{name} sum is: {score}", hit_card

while game_start:
    #Blind bid required: subtract 2 from the player
    #Player sum and dealer sum get gard reset-move this outside of the code
    start_game()
    if player_hand[0].get('value') + player_hand[1].get('value') == 21:
        game_over = True
        dealer_draw = True
        print("You have blackjack!")
    elif player_hand[0].get('value') + player_hand[1].get('value') > 21:
        game_over = True

    if not game_over:    
        hit = input("Do you want to hit?(y/n) ")
        while hit.lower() =='Y'.lower():
            players_info = calc_sum_and_draw(player_sum, deck.pop(), "You")
            player_sum = players_info[0]
            print(f"{players_info[1]}\n {players_info[2]}")
            player_hand.append(players_info[3])
            if players_info[0] >= 21:
                hit = "b"
            else:
                    hit = input("Do you want to hit again?(y/n) ")
                    dealer_draw = True
        game_over = True
        dealer_draw = True
    
    if dealer_draw:
        print(f"Dealer has a {dealer_hand[0].get('value')} of {dealer_hand[0].get('suit')} and a {dealer_hand[1].get('value')} of {dealer_hand[1].get('suit')}")
        while dealer_sum < 17:
                dealers_info = calc_sum_and_draw(dealer_sum, deck.pop(), "Dealer")
                dealer_sum = dealers_info[0]
                print(f"{dealers_info[1]}\n {dealers_info[2]}")
                dealer_hand.append(dealers_info[3])

    if game_over:
        winner()
        restart = input("Do you want to keep going? (y/n)")   
        if restart.lower() == "Y".lower():
            for i in range (len(player_hand)):
                deck.append(player_hand.pop())
            for i in range(len(dealer_hand)):
                deck.append(dealer_hand.pop())
            shuffle_deck()
            dealer_draw = False
            game_over = False
        else:
            game_start = False
            break