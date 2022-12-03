# first program logic
# import random module
import random

card_name = ['Club', 'Heart', 'Diamond', 'Spade']
ls = []
Tre = 1
while Tre <= 13:
    ls += ((Tre, x) for x in card_name)
    Tre += 1

# shuffle cards
random.shuffle(ls)

# draw five cards
print("You got it: ")
for i in range(5):
    print(ls[i][0], 'of', ls[i][1])

# seciend program logic
# importing modules
import itertools, random

# make a deck of cards

deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
print(deck)

# shuffle five cards
random.shuffle(deck)
print(deck)

# draw five cards
print("you got: ")
for i in range(5):
    print(deck[i][0], 'of', deck[i][1])