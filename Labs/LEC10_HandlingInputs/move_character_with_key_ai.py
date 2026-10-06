from pathlib import Path
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
ASSET_DIR = Path(__file__).resolve().parent
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
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    update_canvas()


def main():
    global tuk_ground

    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    tuk_ground = load_image(str(ASSET_DIR / 'TUK_GROUND.png'))
    while running:
        handle_events()
        update()
        draw()
        delay(0.05)
    close_canvas()


if __name__ == '__main__':
    main()
