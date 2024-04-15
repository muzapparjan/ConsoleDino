import argparse
import time
import input
import model
import render
import random
import physics


GAME_STATE_START: str = "GAME_STATE_START"
GAME_STATE_PLAYING: str = "GAME_STATE_PLAYING"
GAME_STATE_END: str = "GAME_STATE_END"
DINO_SPEED_MIN: float = 3
DINO_SPEED_MAX: float = 20
DINO_JUMP_SPEED: float = 30
DINO_JUMP_ACC: float = -15
GROUND_Y: int = 2


GameState = GAME_STATE_START
Score: int = 0
MaxScore: int = 0
DinoX: int = 0
DinoY: int = GROUND_Y
DinoSpeed: float = DINO_SPEED_MIN
DinoJumpDuration: float = 100
CactusList = []

Frame: int = 0
FPS: float = 10
ShowFPS: bool = False
ScreenWidth: int = 100
ScreenHeight: int = 50
DeltaTime: float = 0


def init(args: argparse.Namespace) -> None:
    global FPS, ScreenWidth, ScreenHeight, ShowFPS
    FPS = max(args.fps, 1)
    ShowFPS = args.showfps
    ScreenWidth = max(args.width, 20)
    ScreenHeight = max(args.height, 20)
    render.set_frame_buffer_size(ScreenWidth, ScreenHeight)


def flip_y(object: list[str], y: int) -> int:
    size = render.get_drawable_size(object)
    return ScreenHeight - y - size[1]


def new_game() -> None:
    global GameState, Score, DinoSpeed, DinoX, DinoY, CactusList, DinoJumpDuration
    GameState = GAME_STATE_PLAYING
    Score = 0
    DinoX = 0
    DinoY = GROUND_Y
    DinoSpeed = DINO_SPEED_MIN
    DinoJumpDuration = 0
    CactusList = []


def end_game() -> None:
    global GameState
    GameState = GAME_STATE_END


def reset_game() -> None:
    global GameState
    GameState = GAME_STATE_START


def render_screen_start() -> None:
    dino = model.build_dino("idle", Frame)
    tip = ["press space to play"]
    render.draw(0, flip_y(dino, GROUND_Y), dino)
    render.draw(
        int((ScreenWidth - len(tip[0])) / 2),
        flip_y(tip, int((ScreenHeight - len(tip)) / 2)),
        tip,
    )
    if input.dino_jump():
        new_game()


def render_screen_playing() -> None:
    global DinoY, DinoJumpDuration
    dino = model.build_dino("", Frame)
    DinoJumpDuration += DeltaTime
    if input.dino_jump() and DinoY <= GROUND_Y:
        DinoJumpDuration = 0
    DinoY = int(
        DINO_JUMP_SPEED * DinoJumpDuration
        + 0.5 * DINO_JUMP_ACC * DinoJumpDuration * DinoJumpDuration
        + GROUND_Y
    )
    DinoY = max(DinoY, GROUND_Y)
    dinoBox = physics.get_aabb(dino, DinoX, DinoY)
    cactus = model.build_cactus()

    while len(CactusList) < 5:
        minDistance = ScreenWidth
        if len(CactusList) > 0:
            minDistance = max(CactusList[-1], minDistance)
        CactusList.append(minDistance + random.randint(30, 100))

    for index, distance in enumerate(CactusList):
        CactusList[index] = distance - DinoSpeed
        cactusBox = physics.get_aabb(cactus, distance, GROUND_Y)
        if physics.intersect(dinoBox, cactusBox):
            end_game()

    render.draw(DinoX, flip_y(dino, DinoY), dino)
    for index, distance in enumerate(CactusList):
       render.draw(distance, flip_y(cactus, GROUND_Y), cactus)


def render_screen_end() -> None:
    global MaxScore

    dino = model.build_dino("dead", Frame)
    render.draw(GROUND_Y, flip_y(dino, GROUND_Y), dino)

    tips = []
    tips.append("     GAME OVER      ")

    scoreTip = "YOUR SCORE: " + str(Score)
    flip: bool = False
    while len(scoreTip) < 20:
        if flip:
            scoreTip = scoreTip + " "
        else:
            scoreTip = " " + scoreTip
        flip = not flip
    tips.append(scoreTip)

    highestScoreTip = "HIGHEST SCORE: " + str(MaxScore)
    flip = False
    while len(highestScoreTip) < 20:
        if flip:
            highestScoreTip = highestScoreTip + " "
        else:
            highestScoreTip = " " + highestScoreTip
        flip = not flip
    tips.append(highestScoreTip)

    if Score >= MaxScore:
        tips.append("   NEW RECORD!!!    ")
        MaxScore = Score
    tips.append("press space to play ")
    render.draw(
        int((ScreenWidth - len(tips[0])) / 2),
        flip_y(tips, int((ScreenHeight - len(tips)) / 2)),
        tips,
    )
    if input.dino_jump():
        reset_game()


def loop() -> None:
    render.clear_frame_buffer()
    if GameState == GAME_STATE_START:
        render_screen_start()
    elif GameState == GAME_STATE_PLAYING:
        render_screen_playing()
    elif GameState == GAME_STATE_END:
        render_screen_end()
    # if ShowFPS:
    if True:
        render.draw(0, 0, ["fps: " + str(1 / DeltaTime)])
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
    parser.add_argument(
        "-sf",
        "--showfps",
        help="show render fps on left top corner",
        action="store_true",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    init(args)
    global Frame, DeltaTime
    lastTime: float = time.time()
    while True:
        if input.quit():
            break
        now = time.time()
        DeltaTime = now - lastTime
        lastTime = now
        loop()
        Frame += 1
        time.sleep(1.0 / FPS)


if __name__ == "__main__":
    main()
