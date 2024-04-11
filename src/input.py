import keyboard

def dino_jump() -> bool:
    return keyboard.is_pressed('space')

def quit() -> bool:
    return keyboard.is_pressed('escape')