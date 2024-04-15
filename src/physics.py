import render

AABB = tuple[int, int, int, int]


def get_aabb(object: list[str], x: int, y: int) -> AABB:
    size = render.get_drawable_size(object)
    return (x, y, x + size[0], y + size[1])


def intersect(a: AABB, b: AABB) -> bool:
    return a[0] <= b[1] and a[1] >= b[0] and a[2] <= b[3] and a[3] >= b[2]
