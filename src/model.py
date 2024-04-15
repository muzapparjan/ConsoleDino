def build_dino(state: str, frame: int) -> list[str]:
    body = build_dino_body()
    if state == "dead":
        build_dino_eye_dead(body)
    elif state == "idle":
        index = frame % 2
        if index == 0:
            build_dino_eye_normal(body)
        elif index == 1:
            build_dino_eye_dead(body)
    else:
        build_dino_eye_normal(body)
        index = frame % 4
        if index == 0:
            build_dino_feet_idle(body)
        elif index == 1:
            build_dino_feet_left_up(body)
        elif index == 2:
            build_dino_feet_idle(body)
        elif index == 3:
            build_dino_feet_right_up(body)
    return body


def build_dino_body() -> list[str]:
    body = []
    body.append("             _____  ")
    body.append("            ■■■■■■■ ")
    body.append("           ■■■■■■■■■")
    body.append("           ■■■■■■■■■")
    body.append("           ■■■■■■■  ")
    body.append("           ■■■      ")
    body.append("■         ■■■■      ")
    body.append("■■       ■■■■■■■■   ")
    body.append("■■     ■■■■■■■  ■   ")
    body.append("■■■■■■■■■■■■■■      ")
    body.append(" ■■■■■■■■■■■■■      ")
    body.append("  ■■■■■■■■■■■       ")
    body.append("   ■■■■■■■■■        ")
    body.append("    ■■■■■■■         ")
    body.append("    ■■■ ■■■         ")
    body.append("    ■■  ■■          ")
    body.append("    ■   ■           ")
    body.append("    ■■  ■■          ")
    body.append("    ■■■ ■■■         ")
    body.append("    ‾‾‾ ‾‾‾         ")
    return body


def build_dino_eye_normal(body: list[str]) -> None:
    body[2] = "           ■■■▪■■■■■"


def build_dino_eye_dead(body: list[str]) -> None:
    body[2] = "           ■■■▢■■■■■"


def build_dino_feet_idle(body: list[str]) -> None:
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "    ■■  ■■          "
    body[-4] = "    ■   ■           "
    body[-3] = "    ■■  ■■          "
    body[-2] = "    ■■■ ■■■         "
    body[-1] = "    ‾‾‾ ‾‾‾         "


def build_dino_feet_left_up(body: list[str]) -> None:
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "  ■■■   ■■          "
    body[-4] = "  ‾‾‾   ■           "
    body[-3] = "        ■■          "
    body[-2] = "        ■■■         "
    body[-1] = "        ‾‾‾         "


def build_dino_feet_right_up(body: list[str]) -> None:
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "    ■■    ■■■       "
    body[-4] = "    ■     ‾‾‾       "
    body[-3] = "    ■■              "
    body[-2] = "    ■■■             "
    body[-1] = "    ‾‾‾             "


def build_cactus() -> list[str]:
    cactus = []
    cactus.append("      ■■       ")
    cactus.append("     ■■■■      ")
    cactus.append("     ■■■■■     ")
    cactus.append("     ■■■■■     ")
    cactus.append("     ■■■■■   ■ ")
    cactus.append("     ■■■■■  ■■ ")
    cactus.append("     ■■■■■■■■  ")
    cactus.append("     ■■■■■■    ")
    cactus.append(" ■   ■■■■■     ")
    cactus.append(" ■■  ■■■■■     ")
    cactus.append("  ■■■■■■■■     ")
    cactus.append("    ■■■■■■     ")
    cactus.append("     ■■■■■     ")
    cactus.append("     ■■■■■     ")
    cactus.append("     ■■■■■     ")
    return cactus
