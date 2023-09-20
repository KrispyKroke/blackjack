# Random library required for shuffling the deck.
import random

# Global variables for card deck
card_suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

card_list = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 
'Jack', 'Queen', 'King']

deck = [(card, category) for category in card_suits
for card in card_list]

# Function which handles the payout for the player based on outcome of game.
def determine_payout(game_result, bet, player_total, dealer_total):
    print('Your total: {}'.format(player_total))
    print('Dealer total: {}'.format(dealer_total))
    if game_result == 'W':
        print('You win ${}!'.format(bet * 2))
        return bet * 2
    elif game_result == 'L':
        print('You lose ${}!'.format(bet))
        return 0
    else:
        print('You tied!')
        return bet

# Function which handles drawing of card from deck for the dealer's turn
def dealer_draw(dealer_hand):
    dealer_hand.append(deck.pop())
    return dealer_hand

# Function which finds winner of game of blackjack.
def determine_winner(player_total, dealer_total):
    if dealer_total > 21 and player_total <= 21 or player_total > dealer_total and player_total <= 21:
        return 'W'
    elif player_total < dealer_total or player_total > 21:
        return 'L'
    else:
        return 'T'

# Function which calculates score of dealer hand.
def calculate_dealer_hand(dealer_hand):
    dealer_total = 0
    for x in dealer_hand:
        dealer_total += calculate_card_value(x, dealer_total)
    return dealer_total

# Function which determines card values.
def calculate_card_value(x, player_total):
    if x[0] == 'Jack' or x[0] == 'Queen' or x[0] == 'King':
        return 10
    elif x[0] == 'Ace':
        if player_total < 11:
            return 11
        else:
            return 1
    else:
        return x[0]

# Function for determining score of player hand.
def calculate_player_hand(player_hand):
    player_total = 0
    for x in player_hand:
        player_total += calculate_card_value(x, player_total)
    return player_total

# Function for player turn.
def continue_playing(player_hand):
    player_hand.append(deck.pop())
    print('Player card drawn: {}'.format(player_hand[len(player_hand) - 1]))
    return player_hand


# Handles betting process.
def betting_phase(bet, balance):
    bet = ''
    while not bet.isdigit():
        print('Please enter a valid bet')
        bet = input('Bet amount: ')
    bet = int(bet)
    while bet > balance or bet < 1: 
            print('Please enter a valid bet')
            bet = int(input('Bet amount: '))
    return bet


# Primary game function that calls a betting function.  First hand is played.  The 
# rest of the code handles the playing of a game of blackjack, calling applicable functions.
def play(balance):
    while balance > 0:
        deck = [(card, category) for category in card_suits
        for card in card_list]
        random.shuffle(deck)
        bet = balance + 1
        bet = betting_phase(bet, balance)
        balance -= bet
        player_hand = []
        dealer_hand = []
        is_natural_player = False
        is_natural_dealer = False
        for x in range(2):
            player_hand.append(deck.pop())
            print('Player card drawn: {}'.format(player_hand[x]))
            dealer_hand.append(deck.pop())
            if x == 0:
                print('Dealer card drawn: {}'.format(dealer_hand[x]))
        if is_natural_player and is_natural_dealer:
            print('Draw!')
            balance += bet
            is_natural_player = False
            is_natural_dealer = False
            continue
        player_total = calculate_player_hand(player_hand)
        while player_total <= 21:
            player_total = calculate_player_hand(player_hand)
            print('Your current score: {}'.format(player_total))
            if player_total == 21 and len(player_hand) == 2:
                is_natural_player = True
                pass
            else:
                pass
            turn_decision = ''
            while not is_natural_player and not turn_decision == 'hit' and not turn_decision == 'pass':
                    turn_decision = input('Do you want to hit or pass? ')
            if turn_decision == 'pass':
                break
            else: 
                player_total = calculate_player_hand(continue_playing(player_hand))
        dealer_total = calculate_dealer_hand(dealer_hand)
        if dealer_total == 21:
            is_natural_dealer = True
        while dealer_total < 17:
            dealer_total = calculate_dealer_hand(dealer_draw(dealer_hand))
        game_result = determine_winner(player_total, dealer_total)
        balance += determine_payout(game_result, bet, player_total, dealer_total)
        print('Your current pot: ${}'.format(balance))
        
            
    






# Typical main function found in all programs.  Contains an infinite loop
# that prompts the user for a balance for playing the game.
def main():
    while (1):
        balance = ''
        while not balance.isdigit() or balance.isdigit() and int(balance) < 1:
            balance = input('How much money do you have?(in dollars) ')
        play(int(balance))

# Main is called to run the game in the console.
main()