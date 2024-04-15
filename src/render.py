import screen

_frameBuffer: list[str] = []
_frameBufferWidth = 0
_frameBufferHeight = 0


def clear_frame_buffer() -> None:
    global _frameBuffer
    _frameBuffer.clear()
    for j in range(_frameBufferHeight):
        line = []
        for i in range(_frameBufferWidth):
            line.append(" ")
        _frameBuffer.append("".join(line))


def set_frame_buffer_size(width: int, height: int) -> None:
    if width <= 0 or height <= 0:
        raise ValueError("invalid frame buffer size")
    global _frameBufferWidth, _frameBufferHeight
    _frameBufferWidth = width
    _frameBufferHeight = height
    clear_frame_buffer()


def draw(x: int, y: int, object: list[str]) -> None:
    size = get_drawable_size(object)
    if size[0] == 0 or size[1] == 0:
        raise ValueError("invalid drawable object")
    for j in range(size[1]):
        _y = y + j
        if _y >= _frameBufferHeight:
            break
        if _y < 0:
            continue
        pixels = [pixel for pixel in _frameBuffer[_y]]
        pixelsToDraw = [pixel for pixel in object[j]]
        for i in range(size[0]):
            _x = x + i
            if _x >= _frameBufferWidth or _x < 0:
                continue
            pixels[_x] = pixelsToDraw[i]
        _frameBuffer[_y] = "".join(pixels)


def get_drawable_size(object: list[str]) -> tuple[int, int]:
    row = len(object)
    if row <= 0:
        return (0, 0)
    firstLine = object[0]
    column = len(firstLine)
    if column <= 0:
        return (0, 0)
    return (column, row)


def update_screen() -> None:
    screen.clear()
    screen.draw(_frameBuffer)
