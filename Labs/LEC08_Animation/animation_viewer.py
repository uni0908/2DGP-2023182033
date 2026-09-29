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

run = (
    (454, 685, 96, 122),
    (588, 685, 108, 118),
    (734, 685, 98, 124),
    (870, 685, 102, 126),
    (1010, 685, 96, 120),
    (1144, 685, 108, 118),
    (1290, 685, 96, 124),
)

run_attack = (
    (454, 477, 112, 150),
    (590, 477, 120, 138),
    (734, 477, 114, 126),
    (872, 477, 130, 124),
    (1026, 477, 128, 124),
    (1178, 477, 136, 116),
)

attack = (
    (454, 66, 84, 150),
    (644, 66, 86, 142),
    (838, 66, 176, 136),
    (1040, 66, 132, 128),
)

frame_index = 0

while True:
    clear_canvas()
    draw_rectangle(0, 0, get_canvas_width() - 1, get_canvas_height() - 1,
                   r=161, g=161, b=161, filled=True)

    frame = attack[frame_index]
    frame_index = (frame_index + 1) % len(attack)

    character.clip_draw(*frame, 400, 300)


    update_canvas()
    get_events()
    delay(0.1)

close_canvas()

