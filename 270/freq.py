def freq_digit(num: int) -> int:
    d = list(str(num))
    t = tuple(d)
    len_ = len(d)
    return int(max(t, key=lambda x: (d.count(x), len_ - d.index(x))))
