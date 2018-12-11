# implementation of card game - Memory
import simplegui
import random

card_width_position = [25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775]
random_list = []
exposed = []
selected_number = []
indicator = 0
open_card = 'Transparent'
closed_card = 'Green'

def number_generation():
    global random_list
# selection of a number of 8 numbers
    numbers = range(10)
    random.shuffle(numbers)
    numbers.pop()
    numbers.pop()
    folding_numbers = []
    folding_numbers.extend(numbers)
    folding_numbers.extend(numbers)
    random.shuffle(folding_numbers)
    random_list = folding_numbers

# helper function to initialize globals
def new_game():
    global exposed, card_width_position, indicator
    indicator = 0
    number_generation ()
    exposed = []
    card_width_position = [25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775]
# define event handlers
def mouseclick(pos):
    global indicator
    # add game state logic here
    a = list(pos)
    if a[0] < 50:
        b=25
        c=random_list[0]
    elif 50<=a[0]<100:
        b=75
        c=random_list[1]
    elif 100<=a[0]<150:
        b=125
        c=random_list[2]
    elif 150<=a[0]<200:
        b=175
        c=random_list[3]
    elif 200<=a[0]<250:
        b=225
        c=random_list[4]
    elif 250<=a[0]<300:
        b=275
        c=random_list[5]
    elif 300<=a[0]<350:
        b=325
        c=random_list[6]
    elif 350<=a[0]<400:
        b=375
        c=random_list[7]
    elif 400<=a[0]<450:
        b=425
        c=random_list[8]
    elif 450<=a[0]<500:
        b=475
        c=random_list[9]
    elif 500<=a[0]<550:
        b=525
        c=random_list[10]
    elif 550<=a[0]<600:
        b=575
        c=random_list[11]
    elif 600<=a[0]<650:
        b=625
        c=random_list[12]
    elif 650<=a[0]<700:
        b=675
        c=random_list[13]
    elif 700<=a[0]<750:
        b=725
        c=random_list[14]
    elif 750<=a[0]<800:
        b=775
        c=random_list[15]
# passing array values
    if b in card_width_position:
        card_width_position.remove(b)
        exposed.append(b)
        selected_number.append(c)
    else:
        return
# identifying identical cards
    if len(exposed) == 2:
        if selected_number[0]==selected_number[1]:
            exposed.pop()
            exposed.pop()
            selected_number.pop()
            selected_number.pop()
# counting repetitions
            indicator += 1
# closing two different cards when opening the third card
    elif len(exposed) == 3:
        d=b
        exposed.pop()
        card_width_position.extend(exposed)
        exposed.pop()
        exposed.pop()
        exposed.append(d)
        selected_number.pop(0)
        selected_number.pop(0)
# counting repetitions
        indicator += 1

# cards are logically 50x100 pixels in size
def draw(canvas):
# arrangement of numbers
    position = 5
    for numbers in random_list:
        canvas.draw_text(str(numbers), (position, 80), 85, 'White')
        position += 50
# closed card location
    for width_pos1 in card_width_position:
        canvas.draw_line([width_pos1, 0],[width_pos1, 100], 50, closed_card)
# location of open cards
    for width_pos2 in exposed:
        canvas.draw_line([width_pos2, 0],[width_pos2, 100], 50, open_card)
# cards boundaries
    canvas.draw_line([0, 0],[800, 0], 3, 'Brown')
    canvas.draw_line([0, 100],[800, 100], 3, 'Brown')
    canvas.draw_line([0, 0],[0, 100], 3, 'Brown')
    for position_line in card_width_position:
        canvas.draw_line([position_line+25, 0],[position_line+25, 100], 3, 'Brown')
# total number of repetitions
    label.set_text("Turns = " + str(indicator))
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
