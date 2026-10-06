from pathlib import Path
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
ASSET_DIR = Path(__file__).resolve().parent
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
facing = 1  # 1: 오른쪽, -1: 왼쪽
pressed_keys = set()
animation_row = 300


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


def update():
    global x, y, frame, facing, animation_row
    dir_x = (SDLK_RIGHT in pressed_keys) - (SDLK_LEFT in pressed_keys)
    if dir_x != 0:
        facing = dir_x
    x = max(50, min(TUK_WIDTH - 50, x + dir_x * 5))
    dir_y = (SDLK_UP in pressed_keys) - (SDLK_DOWN in pressed_keys)
    y = max(50, min(TUK_HEIGHT - 50, y + dir_y * 5))
    moving = dir_x != 0 or dir_y != 0
    if moving:
        animation_row = 100 if facing == 1 else 0
    else:
        animation_row = 300 if facing == 1 else 200
    frame = (frame + 1) % 8


def draw():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, animation_row, 100, 100, x, y)
    update_canvas()


def main():
    global tuk_ground, character

    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    tuk_ground = load_image(str(ASSET_DIR / 'TUK_GROUND.png'))
    character = load_image(str(ASSET_DIR / 'animation_sheet.png'))
    while running:
        handle_events()
        update()
        draw()
        delay(0.05)
    close_canvas()


if __name__ == '__main__':
    main()
