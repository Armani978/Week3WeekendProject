import random

suits = ['♣', '♦', '♥', '♠']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10','Jack', 'King', 'Queen']

class Cards:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
    
    def display(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.deck = []
        for s in suits:
            for v in values:
                self.deck.append(Cards(values, suits))
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    
    def draw(self):
        self.deck.extend(self.deck)

class Wager:
    def __init__(self):
        self.limit = 1000
        self.bet = 0
    def win(self):
        self.limit += self.bet
    def lose(self):
        self.limit -=self.bet

def welcome(self):
    while True:
        for w in self.wager:
            wager = input("What is your wager?(Type any amount up to 1000 ")
            if wager <= 1000:
                pass

class Hand:
    def __init__(self, dealer=False):
        self.value = 0
        self.dealer = dealer
        self.cards = []
        self.aces = 0
    

    def currentValue(self, ace_present):
        self.value=0
        ace_present = False
        for card in self.cards:
            if self.cards.isnumeric(self):
                self.value += int(card.value)
            else:
                if card.value == "Ace":
                    ace_present = True
                    self.value += 11
                else:
                    self.value += 1
    
    def addCard(self):
        self.cards.append(self)
        # self.value += int(values)
        if self.value == 'Ace':
            self.aces += 1

    def show(self):
        if self.dealer== True:
            print("******")
            print(self.cards[1])
        else:
            for card in self.cards:
                return card
            return "Value:", self.value




class UI:
    # def __init__(self):
    #     pass
    def hitStand(self):
            self.hand= Hand()
            self.deck = Deck()
            self.deck.shuffle()
            hit_stand = input("Hit Or Stand(type h or s)  ")
            if hit_stand.lower() == "h":
                print(self.deck.draw(Cards(1)))
                
    def gameUI(self):
        while True:
            self.deck = Deck()
            self.deck.shuffle()
            self.wager= Wager()
            
            self.currentCards = Hand()
            self.dealersCards = Hand(dealer=True)
            
            print("Welcome to Blackjack")
            self.deck = Deck()
            for card in range(2):
                self.currentCards.addCard()
                self.dealersCards.addCard()

            wagers = input("Pick your wager. The max bet possible is 1000")
            if int(wagers) <= 1000:
                self.wager.bet += int(wagers)
                self.deck.draw()
                print(f'{self.wager.bet}')
                print(self.currentCards.cards)
                self.hitStand()
            
                  

                
                
            else:
                print("Wager error. Please enter below the limit of 1000")

            
test = UI()
test.gameUI()
