def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath, encoding="utf-8") as f:
        return f.read().splitlines(keepends=False)[-n:]
