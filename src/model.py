def build_deno_body() -> list[str]:
    body = []
    body.append("             _____  ")
    body.append("            ■■■■■■■ ")
    body.append("           ■■■■■■■■■")
    body.append("           ■■■■■■■■■")
    body.append("           ■■■■■■■  ")
    body.append("           ■■■      ")
    body.append("■         ■■■■      ")
    body.append("■■       ■■■■■      ")
    body.append("■■     ■■■■■■■      ")
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

def build_deno_eye_normal(body: list[str]):
    body[2] = "           ■■■▪■■■■■"

def build_deno_eye_dead(body: list[str]):
    body[2] = "           ■■■▢■■■■■"

def build_deno_feet_idle(body: list[str]):
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "    ■■  ■■          "
    body[-4] = "    ■   ■           "
    body[-3] = "    ■■  ■■          "
    body[-2] = "    ■■■ ■■■         "
    body[-1] = "    ‾‾‾ ‾‾‾         "

def build_deno_feet_left_up(body: list[str]):
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "  ■■■   ■■          "
    body[-4] = "  ‾‾‾   ■           "
    body[-3] = "        ■■          "
    body[-2] = "        ■■■         "
    body[-1] = "        ‾‾‾         "

def build_deno_feet_right_up(body: list[str]):
    body[-6] = "    ■■■ ■■■         "
    body[-5] = "    ■■    ■■■       "
    body[-4] = "    ■     ‾‾‾       "
    body[-3] = "    ■■              "
    body[-2] = "    ■■■             "
    body[-1] = "    ‾‾‾             "