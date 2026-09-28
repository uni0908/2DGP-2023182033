
import math
from pathlib import Path

from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE,
    clear_canvas, close_canvas, delay, get_events,
    load_image, open_canvas, update_canvas,
)


def line_points(start, end, steps):
    """출발점과 도착점을 포함하는 직선 위의 좌표를 만든다."""
    for step in range(steps + 1):
        t = step / steps
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        yield x, y


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        yield 400 + 200 * math.cos(theta), 300 + 200 * math.sin(theta)


def move_rectangle():
    # 왼쪽 위에서 출발해 시계 방향으로 이동한다.
    yield from line_points((50, 550), (750, 550), 140)
    yield from line_points((750, 550), (750, 50), 100)
    yield from line_points((750, 50), (50, 50), 140)
    yield from line_points((50, 50), (50, 550), 100)


def move_triangle():
    a, b, c = (100, 100), (700, 100), (400, 500)
    yield from line_points(a, b, 100)
    yield from line_points(b, c, 100)
    yield from line_points(c, a, 100)


def draw_boy(boy, x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def main():
    open_canvas(800, 600)
    try:
        image_path = Path(__file__).resolve().with_name('character.png')
        boy = load_image(str(image_path))

        while True:
            for movement in (move_circle, move_rectangle, move_triangle):
                for x, y in movement():
                    for event in get_events():
                        if event.type == SDL_QUIT:
                            return
                        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                            return
                    draw_boy(boy, x, y)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
