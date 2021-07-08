def ida_star(g, h, w):
    f = g + h
    return f


def weighted_ida_star(g, h, w):
    f = g + h * w
    return f


def decreasing_weighted_ida_star(g, h, w):
    if g < h:
        f = g + h
    else:
        f = (g + (2 * w - 1) * h) / w
    return f


def increasing_weighted_ida_star(g, h, w):
    if g < ((2 * w - 1) * h):
        f = g / (2 * w - 1) + h
    else:
        f = (g + h) / w
    return f


algorithms = {
    'IDA*': ida_star,
    'WIDA*': weighted_ida_star,
    '-DWIDA*': decreasing_weighted_ida_star,
    '+DWIDA*': increasing_weighted_ida_star,
}