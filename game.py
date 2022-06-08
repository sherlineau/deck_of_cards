from classes.deck import Deck

bicycle = Deck()

print("Black Jack")
number_players = int(input("Enter number of players:"))

for i in range(0, number_players):
    
    bicycle.randomCard()


bicycle.show_scoreboard()