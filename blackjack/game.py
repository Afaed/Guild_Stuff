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
stay = False

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
        elif player_sum == 21:
            print("You win! You have balckjack")
        elif dealer_sum == 21:
            print("Dealer has blackjack! You lose!")
        elif dealer_sum > player_sum:
            print("Dealer wins! They have a higher score more than you!")
        elif player_sum > dealer_sum:
            print("You win! Your score is higher than the dealers")

def start_game():
    global player_hand, dealer_hand, player_sum, dealer_sum
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand = [{'suit': "Clubs", "rank": "A", "value": 11}, {'suit': "Clubs", "rank": 5, "value": 5}]
    player_sum = player_hand[0].get('value') + player_hand[1].get('value') 
    dealer_sum = dealer_hand[0].get('value') + dealer_hand[1].get('value')

def calc_sum_and_draw(val: int, hit_card: dict, name: str):
    score = val+hit_card.get('value')
    return score, f"{name} drew a {hit_card.get('rank')} of {hit_card.get('suit')}", f"{name} sum is: {score}", hit_card   

def aces_adjust(hand: list, score: int):
    #TODO: Change the score so it can be the highest it can be without being greater than 21.
    new_score = 0
    if score > 21:
        for card in hand:
            if card.get('rank') == "Ace":
                card["value"] = 1
    for card in hand:
        new_score += card["value"]
    return new_score

deck = []
card = {}

suits = ['♠️', '♦️', '♣️', '♥️']
ranks = {1:'A', 11: 'J', 12: 'Q', 13: 'K'}
#TODO: Set the 1 to ace and the 11, 12, 13 cards to king, queen, and jack.
#TODO: Set the values from 11 onwards to 10 
values= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

for suit in suits:
    for value in values:
        save_value = value
        if value == 1:
            card = {'suit': suit, 'value': 11, 'rank': ranks[save_value]}
            deck.append(card)     
        elif value > 10:
            value = 10
            card = {'suit': suit, 'value': value, 'rank': ranks[save_value]}
            deck.append(card)     
        else:
            card = {'suit': suit, 'value': value, 'rank': value}
            deck.append(card)

shuffle_deck()

start_game()

while game_start:
    #Blind bid required: subtract 2 from the player
    #Player sum and dealer sum get gard reset-move this outside of the code
    print("Player has a: ")
    #TODO: Turn this into a function!
    for card in player_hand:
        print(f"""        ---- 
        |{card.get('rank')} |
        |{card.get('suit')} |
        ----""")

    print(f"Dealer has a {dealer_hand[0].get('rank')} of {dealer_hand[0].get('suit')} showing.")
    
    if game_over:
        winner()
        restart = input("Do you want to keep going? (y/n)")   
        if restart.lower().startswith('y'):
            for i in range (len(player_hand)):
                deck.append(player_hand.pop())
            for i in range(len(dealer_hand)):
                deck.append(dealer_hand.pop())
            shuffle_deck()
            stay = False
            game_over = False
        else:
            game_start = False
            break

    if player_hand[0].get('value') + player_hand[1].get('value') == 21:
        game_over = True
        stay = True
        print("You have blackjack!")
    #Delete this line below later
    elif player_hand[0].get('value') + player_hand[1].get('value') > 21:
        #TODO: Check the order adjustment
        player_sum = aces_adjust(player_hand, player_sum)
        game_over = True

    hit = input("Do you want to hit?(y/n) ")

    if not hit.lower().startswith('y'):
        stay = True
        game_over = True
    else:
        players_info = calc_sum_and_draw(player_sum, deck.pop(), "You")
        player_sum = players_info[0]
        player_hand.append(players_info[3])
        print(f"{players_info[1]}\nPlayer sum is {player_sum}")   
    
    if stay:
        print(f"Dealer has a {dealer_hand[0].get('rank')} of {dealer_hand[0].get('suit')} and a {dealer_hand[1].get('rank')} of {dealer_hand[1].get('suit')}")

        while dealer_sum < 17:
                dealers_info = calc_sum_and_draw(dealer_sum, deck.pop(), "Dealer")
                dealer_hand.append(dealers_info[3])
                dealer_sum = dealers_info[0]
                if dealer_sum > 21:
                    dealer_sum = aces_adjust(dealer_hand, dealer_sum)
                print(f"{dealers_info[1]}\nDealer's sum is: {dealer_sum}.")
        #TODO: set game_over here to be true.
