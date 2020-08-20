def is_armstrong(n: int) -> bool:
    return n == sum(int(c) ** len(str(n)) for c in str(n))
