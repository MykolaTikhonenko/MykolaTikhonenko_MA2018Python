# Mini-project - "Stop: Game"

import simplegui
# initial value output
number_results = '0/0'
n1 = 0
n2 = 0
selected_number = '0:00.0'
s5 = '0'
s3 = '0'
s2 = '0'
s0 = '0'

interval = 100
seconds_counter = 0
minute_counter = 0
# switch value
clik = 'Start'
# assigning a stopwatch value to variables
def stopwatch():
    global selected_number, minute_counter, seconds_counter, clik, s5, s3, s2, s0
    seconds_counter = seconds_counter + 1
    if (seconds_counter < 10):
        s5 = str(seconds_counter)
    elif (10 <= seconds_counter < 100):
        a1 = str(seconds_counter)
        s5 = a1[1]
        s3 = a1[0]
    elif 100 <= seconds_counter < 600:
        a2 = str(seconds_counter)
        s5 = a2[2]
        s3 = a2[1]
        s2 = a2[0]
    elif seconds_counter == 600:
        minute_counter = minute_counter + 1
        s5 = str(0)
        s3 = str(0)
        s2 = str(0)
        seconds_counter = 0
        s0 = str(minute_counter)
        if minute_counter == 10:
            stop()
# inability to enable the Start function
            clik = 'Reset'
# assignment of received values to a variable
    selected_number = s0 + selected_number[1:2] + s2 + s3 + selected_number[4:5] + s5
# performance when pressing the button
def start():
    global n2,number_results, clik
# protection of secondary allocation during execution
    if clik == 'Start':
        clik = 'Stop'
        n2=n2 + 1
        number_results = number_results[:2] + str(n2)
        timer.start ()
# performance when pressing the button
def stop():
    global n1,n2,number_results, clik
# protection of secondary allocation during execution
    if clik == 'Stop':
        clik = 'Start'
        timer.stop()
        if selected_number [5] == '0':
            n1=n1 + 1
            number_results = str(n1)+number_results[1:]
# performance when pressing the button
def reset():
    global n1, n2, minute_counter, seconds_counter, s5, s3, s2, s0, selected_number, number_results,clik
    if (clik == 'Start') or (clik == 'Stop')or (clik == 'Reset'):
        timer.stop()
        s5 = '0'
        s3 = '0'
        s2 = '0'
        s0 = '0'
        seconds_counter = 0 
        minute_counter = 0
        n1 = 0
        n2 = 0
        selected_number = '0:00.0'
        number_results = '0/0'
        clik = 'Start'
# screen output and output parameters
def draw(canvas):
    canvas.draw_text(str(selected_number) ,[90, 115], 48, "White")
    canvas.draw_text(str(number_results) ,[250, 30], 24, "Red")

# invoice and function call
timer = simplegui.create_timer(interval, stopwatch)
# launch of the screen and its parameters
frame = simplegui.create_frame("Have you press", 300, 200)
frame.set_canvas_background("blue")
frame.set_draw_handler(draw)
#function buttons on the screen
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

frame.start()

