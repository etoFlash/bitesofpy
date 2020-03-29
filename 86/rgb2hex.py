def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(255 >= n >= 0 for n in rgb) or len(rgb) != 3:
        raise ValueError
    return "#" + "".join(f"{n:02x}" for n in rgb).upper()
