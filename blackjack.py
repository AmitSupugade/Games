# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
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
        self.list = []

    def __str__(self):
        s1 = ""
        if self.list == []:
            s1 = " "
        else:
            for i in range(0, len(self.list), 1):
                s1 = s1 + " " + str(self.list[i])
        s = "Hand contains" + s1
        return s

    def add_card(self, card):
        self.list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = i = ACE = 0	# compute the value of the hand, see Blackjack video
        if self.list != []:
            while i < len(self.list):
                wanted = self.list[i]
                rank = wanted.get_rank()
                value += VALUES[rank]
                if rank == 1:
                    ACE += 1
                i += 1
            if value < 11:
                if ACE == 1:
                    value += 10
        else:
            value = 0
        return value
    
    def draw(self, canvas, pos):
        card_pos = pos
        i = 0
        if card_pos[1] == 230:
            if in_play == True:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [card_pos[0] + CARD_CENTER[0], card_pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                card_pos[0] += 100
                i = 1
   
        while i < len(self.list):	# draw a hand on the canvas, use the draw method for cards
            wanted = (self.list[i])
            wanted.draw(canvas, card_pos)
            card_pos[0] += 100
            i += 1

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []
        for i in range(0, len(SUITS), 1):
            for j in range(0, len(RANKS), 1):
                new = Card(SUITS[i] , RANKS[j])
                self.deck_list.append(new)

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck_list)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        crd = self.deck_list[-1]
        self.deck_list.remove(crd)
        return crd
    
    def __str__(self):
        s1 = ""
        if self.deck_list == []:
            s1 = " "
        else:
            for i in range(0, len(self.deck_list), 1):
                s1 = s1 + " " + str(self.deck_list[i])
        s = "Deck contains" + s1
        return s


player_hand = Hand()
dealer_hand = Hand()
new_deck = Deck()
#define event handlers for buttons
def deal():
    global outcome, in_play
    global player_hand, dealer_hand
    global new_deck
    global score

    if in_play:
        #print "Player Lose"
        outcome = "You Lose!"
        score -= 1
        in_play = False
    else:
        player_hand = Hand()
        dealer_hand = Hand()
        new_deck = Deck()
        new_deck.shuffle()
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        #print "Player's hand = " + str(player_hand)
        #print "Dealer's hand = " + str(dealer_hand)
        in_play = True

def hit():
    global in_play
    global score
    global outcome
    global new_deck
    global player_hand
    if in_play == True:	# replace with your code below
        if player_hand.get_value() <= 21:
            player_hand.add_card(new_deck.deal_card())
            #print "Player's hand = " + str(player_hand)
        if player_hand.get_value() > 21:
            #print "You are Busted"
            outcome = "You are Busted!"
            in_play = False
            score -= 1
    # if the hand is in play, hit the player
    
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player_hand, dealer_hand	# replace with your code below
    global score
    global outcome
    global in_play
    if in_play == True:
        if player_hand.get_value() > 21:
            #print "You are Busted"
            outcome = "You are Busted!"
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(new_deck.deal_card())
            if dealer_hand.get_value() > 21:
                #print "Dealer is Bursted"
                outcome = "Dealer is Busted!"
                score += 1
            elif dealer_hand.get_value() == player_hand.get_value():
                #print "Dealer Wins"
                outcome = "Dealer Win!"
                score -= 1
            elif  dealer_hand.get_value() > player_hand.get_value():
                #print "Dealer Wins"
                outcome = "Dealer Win!"
                score -= 1
            else:
                #print "Player Wins"
                outcome = "Player Win!"
                score += 1
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [100, 230])
    #card = Card("D", "K")
    #card.draw(canvas, [100, 430])
    canvas.draw_text("Blackjack", (100, 100), 50, "White")
    if in_play:
        canvas.draw_text("Hit or Stand?", (300, 400), 30, "Black")
    else:
        canvas.draw_text("New Deal?", (300, 400), 30, "Black")
        canvas.draw_text(outcome, (300, 200), 30, "Black")
    canvas.draw_text("Score = " + str(score), (400, 100), 40, "Black")
    canvas.draw_text("Dealer", (100, 200), 40, "Black")
    canvas.draw_text("Player", (100, 400), 40, "Black")
    dealer_hand.draw(canvas, [100, 230])
    player_hand.draw(canvas, [100, 430])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()

