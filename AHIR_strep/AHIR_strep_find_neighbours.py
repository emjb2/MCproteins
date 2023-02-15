from general_functions.dirac_delta import dirac_delta
from math import floor

def find_neighbours(n, loc, positions):
    theoretical_neighbours = [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n * (n+1)), (loc - n) % (n * (n+1))]
    neighbours = [x for x in theoretical_neighbours if x in positions]
    return neighbours

# find_neighbours(3,2)