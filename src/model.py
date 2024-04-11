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