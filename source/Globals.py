import random as r
from source.Particle import Particle

side = 650
# change randrange to Particle((i, j))
startCells = [[r.randrange(2) for i in range(side)] for j in range(side)]
