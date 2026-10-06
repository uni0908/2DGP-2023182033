from pathlib import Path
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_SIZE = 100
MOVE_SPEED = 5
FRAME_COUNT = 8
FRAME_DELAY = 0.05
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
    half_size = CHARACTER_SIZE // 2
    x = max(half_size, min(TUK_WIDTH - half_size, x + dir_x * MOVE_SPEED))
    dir_y = (SDLK_UP in pressed_keys) - (SDLK_DOWN in pressed_keys)
    y = max(half_size, min(TUK_HEIGHT - half_size, y + dir_y * MOVE_SPEED))
    moving = dir_x != 0 or dir_y != 0
    if moving:
        next_row = 100 if facing == 1 else 0
    else:
        next_row = 300 if facing == 1 else 200
    if next_row != animation_row:
        frame = 0
    else:
        frame = (frame + 1) % FRAME_COUNT
    animation_row = next_row


def draw():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * CHARACTER_SIZE, animation_row,
                        CHARACTER_SIZE, CHARACTER_SIZE, x, y)
    update_canvas()


def main():
    global tuk_ground, character

    open_canvas(TUK_WIDTH, TUK_HEIGHT)
    tuk_ground = load_image(str(ASSET_DIR / 'TUK_GROUND.png'))
    character = load_image(str(ASSET_DIR / 'animation_sheet.png'))
    while running:
        handle_events()
        if not running:
            break
        update()
        draw()
        delay(FRAME_DELAY)
    close_canvas()


if __name__ == '__main__':
    main()
