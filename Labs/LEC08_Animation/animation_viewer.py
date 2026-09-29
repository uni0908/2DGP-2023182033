from pico2d import *

open_canvas()

character = load_image('knight1_spritelist_1.png')

walk = (
    (454, 869, 80, 128),
    (586, 869, 86, 126),
    (724, 869, 96, 126),
    (872, 869, 94, 128),
    (1028, 867, 92, 128),
    (1133, 868, 86, 126),
    (1260, 869, 86, 128),
    (1398, 869, 88, 128),
)

frame_index = 0

while True:
    clear_canvas()
    draw_rectangle(0, 0, get_canvas_width() - 1, get_canvas_height() - 1,
                   r=161, g=161, b=161, filled=True)

    frame = walk[frame_index]
    frame_index = (frame_index + 1) % len(walk)

    character.clip_draw(*frame, 400, 300)


    update_canvas()
    get_events()
    delay(0.1)

close_canvas()

