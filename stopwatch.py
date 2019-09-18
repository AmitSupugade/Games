# template for "Stopwatch: The Game"

# define global variables
import simplegui

count = 0
stop_count = 0
score = 0
status = True
d = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    a = int(t / 600)
    bcd = t % 600
    if (t / 600 == 0):
        b = int(t/100)
    else:
        b = int (bcd/100)
    if(bcd / 100 == 0):
        cd = bcd
        c = int(cd / 10)
    else:
        cd = bcd % 100
        c = int(cd / 10)
    if(cd / 10 == 0):
        d = cd
    else:
        d = cd % 10
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def init():
    timer.stop()
    global count
    global stop_count
    global score
    global status
    count = 0
    stop_count = 0
    score = 0
    status = True

def start():
    global status
    timer.start()
    status = True

def stop():
    timer.stop()
    global stop_count
    global score
    global status
    if (status):
        if(d == 0):
            score = score + 1
            stop_count = stop_count + 1
            status = False
        else:
            stop_count = stop_count + 1
            status = False
    
def counter():
    global count
    count = count + 1

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, counter)

# define draw handler
def draw_handler(canvas):
    global stop_count
    global score
    result = format(count)
    final = str(score)+"/"+str(stop_count)
    canvas.draw_text(result ,[120,140], 40, "White")
    canvas.draw_text(final, [250, 30], 26, "Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 300)
button1 = frame.add_button("Start", start, 200)
button2 = frame.add_button("Stop", stop, 200)
button3 = frame.add_button("Reset", init, 200)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
