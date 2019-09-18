# implementation of card game - Memory

import simplegui
import random

state = n = m = moves = 0
l3 = []
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
paired = []
# helper function to initialize globals
def init():
    global l3
    global state, moves
    global exposed, paired
    l1 = range(0, 8, 1)
    l2 = range(0, 8, 1)
    l3 = l1 + l2
    random.shuffle(l3)
    state = 0
    moves = 0
    label.set_text("Moves = 0")
    paired = []
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, n , m, moves
    global paired, exposed
    position = pos
    c = position[0] // 50
    if exposed[c] == True:
        pass
    else:
        if state == 0:
            state = 1
            moves += 1
            label.set_text("Moves = " + str(moves))
            n = position[0] // 50
            exposed[n] = True
        elif state == 1:
            state = 2
            m = position[0] // 50
            exposed[m] = True
        else:
            state = 1
            moves += 1
            label.set_text("Moves = " + str(moves))
            if l3[n] == l3[m]:
                paired.append(n)
                paired.append(m)
                for i in range(0, len(paired), 1):
                    exposed[paired[i]] = True
                    i += 1
                n = position[0] // 50
                m = position[0] // 50
                exposed[n] = True  
            else:
                exposed[n] = False
                exposed[m] = False
                n = position[0] // 50
                m = position[0] // 50
                exposed[n] = True
                             
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    i = 0
    for i in range(0, 16, 1):
        if exposed[i] == True:
            canvas.draw_polygon([(i*50,0), (i*50,100), ((i+1)*50,100), ((i+1)*50, 0)], 2 , "White", "Black")
            canvas.draw_text(str(l3[i]), (13 + i *50 , 60), 40, "White")
            i += 1
        else:
            canvas.draw_polygon([(i*50,0), (i*50,100), ((i+1)*50,100), ((i+1)*50, 0)], 2 , "White", "Green")
            i += 1
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

