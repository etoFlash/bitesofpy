from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    # move these into an Enum:
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {THUMBS_UP * self.value}"

    @classmethod
    def average(cls):
        return sum(a.value for a in cls) / len(cls)
