import random as r


class Particle:
    def __init__(self, pos):
        self.direction = r.randrange(4)
        self.position = pos
