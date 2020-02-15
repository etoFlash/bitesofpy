def binary_search(sequence, target):
    a = 0
    b = len(sequence) - 1
    while True:
        if b - a < 2:
            if sequence[a] == target:
                return a
            if sequence[b] == target:
                return b
            break

        m = (a + b) // 2
        if sequence[m] == target:
            return m
        if sequence[m] > target:
            b = m - 1
        else:
            a = m + 1
