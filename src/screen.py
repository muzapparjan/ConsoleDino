import os


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def draw(frame: list[str]) -> None:
    for line in frame:
        print(line)
