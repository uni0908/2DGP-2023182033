"""Sonic 스프라이트 애니메이션 뷰어."""

from pathlib import Path
import sys

import pico2d

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SCALE = 4
FRAME_SECONDS = 0.1
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0
POLL_SECONDS = 0.005
IMAGE_PATH = Path(__file__).resolve().with_name('sonic-sprite.png')
# 원본 왼쪽 위 기준 (x, top, width, height).
WALK = (
    (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39),
    (86, 40, 30, 38), (118, 40, 30, 38), (150, 40, 30, 38),
    (182, 40, 29, 38), (211, 39, 29, 38), (240, 39, 29, 38),
    (270, 45, 24, 32), (302, 51, 29, 26),
)
RUN = (
    (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38),
    (97, 80, 37, 37), (135, 80, 32, 35), (170, 79, 32, 38),
    (206, 79, 26, 38), (238, 80, 24, 37), (263, 80, 30, 37),
    (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38),
)
FAST_RUN = (
    (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
    (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40),
)
ROLL = (
    (1, 169, 29, 30), (35, 167, 29, 31), (67, 169, 30, 29),
    (98, 169, 31, 29), (131, 168, 29, 30), (162, 168, 29, 31),
    (193, 170, 30, 29), (230, 170, 31, 29), (268, 170, 30, 30),
)
SPIN = (
    (1, 206, 30, 27), (36, 206, 29, 27), (70, 206, 29, 27),
    (105, 206, 29, 27), (139, 206, 29, 27), (174, 206, 29, 27),
)
ACTIONS = (
    ('걷기 및 회전 진입', WALK), ('달리기', RUN), ('질주', FAST_RUN),
    ('회전', ROLL), ('고속 회전', SPIN),
)


class Playback:
    def __init__(self, now, actions=ACTIONS):
        self.actions = actions
        self.action_index = 0
        self.frame_index = 0
        self.completed_repeats = 0
        self.paused = False
        self.deadline = now + FRAME_SECONDS

    @property
    def frames(self):
        return self.actions[self.action_index][1]

    @property
    def frame(self):
        return self.frames[self.frame_index]

    def update(self, now):
        if now < self.deadline:
            return
        if self.paused:
            self.action_index = min(self.action_index + 1, len(self.actions) - 1)
            self.frame_index = 0
            self.completed_repeats = 0
            self.paused = False
            self.deadline = now + FRAME_SECONDS
            return
        if self.frame_index == len(self.frames) - 1:
            self.completed_repeats += 1
            if self.completed_repeats == REPEAT_COUNT:
                self.paused = True
                self.deadline = now + PAUSE_SECONDS
                return
            self.frame_index = 0
        else:
            self.frame_index += 1
        self.deadline = now + FRAME_SECONDS


def draw_frame(sprite, frame):
    x, top, width, height = frame
    sprite.clip_draw(x, sprite.h - top - height, width, height,
                     CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                     width * SCALE, height * SCALE)


def render(sprite, frame):
    pico2d.clear_canvas()
    pico2d.draw_rectangle(0, 0, CANVAS_WIDTH - 1, CANVAS_HEIGHT - 1,
                         r=160, g=160, b=160, filled=True)
    draw_frame(sprite, frame)
    pico2d.update_canvas()


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


def run_loop(sprite, playback):
    """정지 상태에서도 매 루프 종료 입력을 확인한다."""
    render(sprite, playback.frame)
    playback.deadline = pico2d.get_time() + FRAME_SECONDS
    while not quit_requested():
        playback.update(pico2d.get_time())
        render(sprite, playback.frame)
        pico2d.delay(POLL_SECONDS)


def main():
    pico2d.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_sprite()
        playback = Playback(pico2d.get_time())
        run_loop(sprite, playback)
    finally:
        pico2d.close_canvas()


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
