from . import card
from random import seed
from random import choice

seed(1)

class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        self.scoreboard = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()


    def randomCard(self):
        #initialize empty list and integer for score
        #set to empty list and score every time the function is run
        

        #loops two times
        for _ in range(2): 
            # _ means literally nothing, it just a placeholder
            #choice() takes a random index from list cards and assigns it to selection
            selection = choice(self.cards)
            
            #selection is added to hand list
            self.hand.append(selection)

            selection.card_info()

        #loops for the length of hand list
        for i in range (0,len(self.hand)):
            #adds point value of card in hand[index] to score
            self.score += self.hand[i].point_val
        print(self.score)
        self.scoreboard.append(self.score)

    def show_scoreboard(self):
        
        for i in range(0,len(self.scoreboard)):
            if (self.scoreboard[i] > 21):
                print(f"Player {i+1} Bust with {self.scoreboard[i]}")
            elif(self.scoreboard[i] == 21):
                print(f"Player {i+1} blackjack with {self.scoreboard[i]}")
            else:
                print(f"Player {i+1} wins with {self.scoreboard[i]}")
            

    #  def loop_until_hit(self):
    #     self.hand = []
    #     self.score = 0
    #     while (self.score < 21):
    #         self.randomCard()