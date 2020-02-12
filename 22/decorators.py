def make_html(element):
    def decorator(func):
        def wrapped(*args):
            return f"<{element}>{func(*args)}</{element}>"
        return wrapped
    return decorator
