"""Sonic 스프라이트 애니메이션 뷰어."""

import pico2d

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800


def quit_requested():
    return any(event.type == pico2d.SDL_QUIT or
               (event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE)
               for event in pico2d.get_events())


def main():
    pico2d.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        while not quit_requested():
            pico2d.clear_canvas()
            pico2d.update_canvas()
            pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == '__main__':
    main()
