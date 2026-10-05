"""Sonic 스프라이트 애니메이션 뷰어."""

from pathlib import Path
import sys

import pico2d

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
IMAGE_PATH = Path(__file__).resolve().with_name('sonic-sprite.png')


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
