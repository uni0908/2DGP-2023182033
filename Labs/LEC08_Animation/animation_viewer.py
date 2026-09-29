from pico2d import *

open_canvas()

character = load_image('adventurer_actions.png')

while True:
    clear_canvas()
    draw_rectangle(0, 0, get_canvas_width() - 1, get_canvas_height() - 1,
                   r=0, g=0, b=0, filled=True)
    update_canvas()
    get_events()
    delay(0.01)

close_canvas()

