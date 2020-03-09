from textwrap import indent


INDENTS = 4


def print_hanging_indents(poem):
    for part_poem in poem.split("\n\n"):
        for (i, s) in enumerate(part_poem.split("\n")):
            line = s.strip()
            if not i:
                print(line)
            else:
                print(indent(line, " " * INDENTS))
