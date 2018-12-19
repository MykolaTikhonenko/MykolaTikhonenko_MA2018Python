# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96) 
CARD_CENTER = (36, 48) 
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ''
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank): 
        if (suit in SUITS) and (rank in RANKS): 
            self.suit = suit 
            self.rank = rank 
        else:
            self.suit = None 
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self): 
        return self.suit + self.rank

    def get_suit(self): 
        return self.suit

    def get_rank(self): 
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit)) 
        
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_card = [] 
    
    def __str__(self):
        # return a string representation of a hand
        h_str = ''
        for a in self.hand_card:
            h_str = h_str +str(' ')+ str(a)
        return 'Hand contains ' + h_str
        
    def add_card(self, card):
        # add a card object to a hand
        self.hand_card.append(card) 

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0 
        ace = 0 
        for v in self.hand_card: 
            if Card.get_rank(v) == 'A': 
                ace = 1				
            result = VALUES.get(Card.get_rank(v)) 
            hand_value += result 
        if (ace > 0) and ((hand_value + 10) <= 21): 
            hand_value += 10					
        return hand_value

   
    def draw(self, canvas, pos):
        for z in self.hand_card:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 73 * self.hand_card.index(z), pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_cards = []
        for s in SUITS:
            for r in RANKS:
                title = Card(str(s),str(r))
                self.deck_cards.append(title)
        
    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck_cards)
                
    def deal_card(self):
        # deal a card object from the deck
        length = len(self.deck_cards) - 1
        self.top_card = self.deck_cards[length]
        self.deck_cards.pop()
        return self.top_card
            
    def __str__(self):
        # return a string representing the deck
        deck_str = ' '
        for z in self.deck_cards:
            deck_str = deck_str +' '+ str(z)
        return 'Deck contains ' + deck_str



#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hand, dealer_hand
    game_deck = Deck()
    game_deck.__init__()
    game_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    in_play = True

def hit():
    global outcome, score, in_play
    player_hand.add_card(game_deck.deal_card())
    if player_hand.get_value() > 21:
        outcome = 'You busted'
        score -= 1
        in_play = False
        return score, outcome, in_play
            
def stand():
    global outcome, score, in_play
    in_play = False
    if player_hand.get_value() > 21:
        outcome = 'You busted'
        score -= 1
        return score, outcome, in_play
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
        else:
            if dealer_hand.get_value() > 21:
                outcome = 'Dealer busts'
                score += 1
                return score, outcome, in_play
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = 'Dealer wins'
                score -= 1
                return score, outcome, in_play
            else:
                outcome = 'You win'
                score += 1
                return score, outcome, in_play

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, [0, 100])    
    player_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [0 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[50,250],30,"Black")
    canvas.draw_text("Score: "+str(score),[50,50],30,"Black")
    canvas.draw_text("Black Jack",[250,50],40,"Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
