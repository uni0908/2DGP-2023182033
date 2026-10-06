from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
running = True


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def update():
    pass


def draw():
    clear_canvas()
    update_canvas()


def main():
    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    while running:
        handle_events()
        update()
        draw()
        delay(0.05)
    close_canvas()


if __name__ == '__main__':
    main()
