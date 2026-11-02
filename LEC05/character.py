from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.

character = load_image('character.png')
grass = load_image('grass.png')

while True:   

    x = 0
    while x < 400:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90)
        update_canvas()
        x += 2
        delay(0.01)

    y = 0
    while y < 300:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90+y)
        update_canvas()
        y += 2
        delay(0.01)


    while x > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90+y)
        update_canvas()
        x -= 2
        delay(0.01)

    while y > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90+y)
        update_canvas()
        y -= 2
        delay(0.01)

    

update_canvas() 
delay(2)

close_canvas()

