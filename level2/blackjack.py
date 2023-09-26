import random

# Define the cards and their values
deck = [('Ace', 1), ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5),
        ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10),
        ('Jack', 10), ('Queen', 10), ('King', 10)]

# Function to calculate the hand's score
def calculate_score(hand):
    total = sum(card[1] for card in hand)
    if total <= 11 and any(card[0] == 'Ace' for card in hand):
        total += 10
    return total

# Deal two cards for the player and the dealer
player_hand = [random.choice(deck) for _ in range(2)]
dealer_hand = [random.choice(deck) for _ in range(2)]

# Show the player's cards and one of the dealer's cards
print(f"Your cards: {player_hand[0][0]} and {player_hand[1][0]}")
print(f"Dealer's card: {dealer_hand[0][0]}")

# Player's loop
while True:
    player_score = calculate_score(player_hand)
    
    if player_score == 21:
        print("Blackjack! You win!")
        break
    elif player_score > 21:
        print("Busted! You lose.")
        break
    
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    
    if action == 'hit':
        new_card = random.choice(deck)
        player_hand.append(new_card)
        print(f"New card: {new_card[0]}")
    elif action == 'stand':
        break

# Dealer's loop
while calculate_score(dealer_hand) < 17:
    new_card = random.choice(deck)
    dealer_hand.append(new_card)

# Show the player's and dealer's hands
print(f"\nYour cards: {[card[0] for card in player_hand]} (Total: {player_score})")
print(f"Dealer's cards: {[card[0] for card in dealer_hand]} (Total: {calculate_score(dealer_hand)})")

# Determine the winner
dealer_score = calculate_score(dealer_hand)
if dealer_score > 21:
    print("The dealer busted! You win!")
elif player_score > 21 or dealer_score > player_score:
    print("The dealer wins.")
elif player_score > dealer_score:
    print("You win!")
else:
    print("It's a tie!")