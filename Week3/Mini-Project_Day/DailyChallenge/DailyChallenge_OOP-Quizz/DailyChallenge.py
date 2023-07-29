import random

class Card:
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f'Card {self.value} of {self.suit}'
        
       
class Deck:
    
    deck = [Card(value, suit) for value in Card.values for suit in Card.suits]

    def shuffle(self):
        if len(self.deck) == 52:
         random.shuffle(self.deck)
        else:
            print('not enough cards')
        
    def deal(self):
        if len(self.deck) == 0:
            print('deck is empty')
        else:
            return self.deck.pop()
            
          
deck_instance = Deck()
deck_instance.shuffle()
print(Deck.deck)
for card in range(53):
 card = deck_instance.deal()
 if card:
  print (card)
 else:
     print('no cards left')