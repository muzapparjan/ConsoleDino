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


def init(args: argparse.Namespace) -> None:
    render.set_frame_buffer_size(args.width, args.height)


x = 0
y = 0


def loop(frame: int) -> None:
    render.clear_frame_buffer()
    global x, y
    dino = model.build_deno(False, frame)
    render.draw(x, y, dino) #FIXME the dino can only move horizontally...
    x += 1
    y += 1
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
        help="render resolution width, default is 50, min is 20",
        type=int,
        default=50,
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
    fps: float = max(args.fps, 1)
    frame: int = 0
    init(args)
    while True:
        if input.quit():
            break
        loop(frame)
        frame += 1
        time.sleep(1.0 / fps)


if __name__ == "__main__":
    main()
