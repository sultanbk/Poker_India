import random

suits = ['♥️', '♦️', '♣️', '♠️']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []

# Add each card to the deck
for suit in suits:
    for rank in ranks:
        card = f"{rank} of {suit}"
        deck.append(card)

print("Deck:", deck)

random.shuffle(deck)

# print("Shuffled Deck:", deck)

players =int(input("Enter the number of players: "))

# Create a list to hold each player's hand
hands = [[] for _ in range(players)]

print(hands)

# Deal 2 cards to each player
for _ in range(2):
    for i in range(players):
        hands[i].append(deck.pop())

# Players hands, This should only visible to that particular player
for i, hand in enumerate(hands):
    print(f"Player {i+1}'s hand: {hand}")


# flop
flop = [deck.pop() for _ in range(3)]
print("Flop:", flop)

# turn
turn = deck.pop()
print("Turn:", turn)

# river 
river = deck.pop()
print("River:", river)

community_cards = flop + [turn] + [river] # Combine community cards

for i, hand in enumerate(hands):
    best_hand = hand + community_cards
    print(f"Player {i+1}'s best hand: {best_hand}")

# Initialize player chips and pot
player_chips = [100] * players  # Each player starts with 100 chips
pot = 0

# Simulate a betting round
for i in range(players):
    print(f"\nPlayer {i+1}'s turn. Chips: {player_chips[i]}")
    action = input("Do you want to (c)all or (f)old? ").strip().lower()

    if action == 'c':
        bet = 10  # Fixed bet amount for simplicity
        player_chips[i] -= bet
        pot += bet
        print(f"Player {i+1} calls. Pot is now {pot}.")
    elif action == 'f':
        print(f"Player {i+1} folds.")
    else:
        print("Invalid action. Player folds by default.")

# Randomly pick a winner (for now)
winner = random.randint(0, players - 1)
print(f"\nPlayer {winner + 1} wins the pot of {pot} chips!")
player_chips[winner] += pot
pot = 0  # Reset the pot