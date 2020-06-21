class Animal:

    seq = 10000
    animals = []

    def __init__(self, name):
        Animal.seq += 1
        self.name = name.capitalize()
        self.seq = Animal.seq
        Animal.animals.append((self.seq, self.name))

    def __str__(self):
        return f"{self.seq}. {self.name}"

    @classmethod
    def zoo(cls):
        for a in Animal.animals:
            yield f"{a[0]}. {a[1]}"
