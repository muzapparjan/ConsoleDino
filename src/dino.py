import argparse
import time
import input
import model
import render


GAME_STATE_START = "GAME_STATE_START"
GAME_STATE_PLAYING = "GAME_STATE_PLAYING"
GAME_STATE_END = "GAME_STATE_END"

GameState = GAME_STATE_START
Score: int = 0
MaxScore: int = 0

Frame = 0
FPS: float = 10
ScreenWidth = 100
ScreenHeight = 50


def init(args: argparse.Namespace) -> None:
    global FPS, ScreenWidth, ScreenHeight
    FPS = max(args.fps, 1)
    ScreenWidth = max(args.width, 20)
    ScreenHeight = max(args.height, 20)
    render.set_frame_buffer_size(ScreenWidth, ScreenHeight)


def flip_y(object: list[str], y: int) -> int:
    size = render.get_drawable_size(object)
    return ScreenHeight - y - size[1]


def render_screen_start() -> None:
    deno = model.build_deno("idle", Frame)
    tip = ["press space to play"]
    render.draw(0, flip_y(deno, 0), deno)
    render.draw(
        int((ScreenWidth - len(tip)) / 2), flip_y(tip, int(ScreenHeight / 2)), tip
    )


def render_screen_playing() -> None:
    pass


def render_screen_end() -> None:
    pass


def loop() -> None:
    render.clear_frame_buffer()
    if GameState == GAME_STATE_START:
        render_screen_start()
    elif GameState == GAME_STATE_PLAYING:
        render_screen_playing()
    elif GameState == GAME_STATE_END:
        render_screen_end()
    render.update_screen()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="Console Dino",
        description="The mini dinosaur escaped from Chrome to console!",
        epilog="dino-dino-dino-dino-dino-dino",
    )
    parser.add_argument(
        "-f",
        "--fps",
        help="render frame per second, default is 10.0, min is 1",
        type=float,
        default=10,
    )
    parser.add_argument(
        "-rw",
        "--width",
        help="render resolution width, default is 100, min is 20",
        type=int,
        default=100,
    )
    parser.add_argument(
        "-rh",
        "--height",
        help="render resolution height, default is 50, min is 20",
        type=int,
        default=50,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    init(args)
    global Frame
    while True:
        if input.quit():
            break
        loop()
        Frame += 1
        time.sleep(1.0 / FPS)


if __name__ == "__main__":
    main()
