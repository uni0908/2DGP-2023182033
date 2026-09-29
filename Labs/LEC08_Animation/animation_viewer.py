from pico2d import *

open_canvas()

character = load_image('adventurer_actions.png')

walk = (
    (98, 744, 156, 184),
    (298, 744, 172, 184),
    (498, 744, 166, 184),
    (712, 744, 146, 184),
    (888, 744, 190, 184),
    (1106, 744, 142, 184),
)

frame_index = 3

while True:
    clear_canvas()
    draw_rectangle(0, 0, get_canvas_width() - 1, get_canvas_height() - 1,
                   r=0, g=0, b=0, filled=True)

    frame = walk[frame_index]

    character.clip_draw(*frame, 400, 300)


    update_canvas()
    get_events()
    delay(0.1)

close_canvas()

