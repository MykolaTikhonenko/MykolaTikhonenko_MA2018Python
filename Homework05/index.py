# implementation of card game - Memory
import simplegui
import random

card_width_position = [25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775]
card_width_position_list = (25,75,125,175,225,275,325,375,425,475,525,575,625,675,725,775)
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
    pos_click = list(pos)
    for num in card_width_position:
        distance=(num-pos_click[0])
        if distance < 0:
            distance=-distance
        if distance<25:
            idexs = card_width_position_list.index(num)
            random_num = random_list[idexs]
            if num in card_width_position:
                f=num
                card_width_position.remove(num)
                exposed.append(num)
                selected_number.append(random_num)
            else:
                return
    
# identifying identical cards   
    if len(exposed) == 2:
# counting repetitions
        indicator += 1
        if selected_number[0]==selected_number[1]:
            exposed.pop()
            exposed.pop()
            selected_number.pop()
            selected_number.pop()

# closing two different cards when opening the third card
    elif len(exposed) == 3:
        exposed.pop()
        card_width_position.extend(exposed)
        card_width_position.sort()
        exposed.pop()
        exposed.pop()
        exposed.append(f)
        selected_number.pop(0)
        selected_number.pop(0)
        
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
