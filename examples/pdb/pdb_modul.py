def funkcja(*args, **kwargs):
    x = 1
    y = 2
    z = 3
    return x + y + z


def funkcja_broken(*args, **kwargs):
    x = 1
    y = 2
    z = 3
    raise Exception(':(')
    return x + y + z

