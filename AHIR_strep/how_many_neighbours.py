# This function needs to tell us how many neighbours a given molecule has
from general_functions.find_neighbours import find_neighbours

def how_many_neighbours(n, loc, heights, positions):
    theoretical_neighbours = find_neighbours(n, loc)
    neighbours = [x for x in theoretical_neighbours if x in positions if heights[x] >= heights[loc]]
    return len(neighbours)