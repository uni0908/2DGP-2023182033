"""Sonic 스프라이트 애니메이션 뷰어."""

from pathlib import Path
import sys

import pico2d

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SCALE = 4
IMAGE_PATH = Path(__file__).resolve().with_name('sonic-sprite.png')
# 원본 왼쪽 위 기준 (x, top, width, height).
FIRST_FRAME = (1, 37, 29, 41)


def draw_frame(sprite, frame):
    x, top, width, height = frame
    sprite.clip_draw(x, sprite.h - top - height, width, height,
                     CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                     width * SCALE, height * SCALE)


def load_sprite(path=IMAGE_PATH):
    if not path.is_file():
        raise RuntimeError(f'스프라이트 파일을 찾을 수 없습니다: {path}')
    try:
        return pico2d.load_image(str(path))
    except Exception as error:
        raise RuntimeError(f'스프라이트 파일을 불러올 수 없습니다: {path}') from error


def quit_requested():
    return any(event.type == pico2d.SDL_QUIT or
               (event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE)
               for event in pico2d.get_events())


def main():
    pico2d.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_sprite()
        while not quit_requested():
            pico2d.clear_canvas()
            draw_frame(sprite, FIRST_FRAME)
            pico2d.update_canvas()
            pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
