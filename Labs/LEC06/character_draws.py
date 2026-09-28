# 실습 과제 진행


from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)
close_canvas()
