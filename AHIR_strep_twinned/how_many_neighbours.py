from general_functions.find_neighbours import find_neighbours


def how_many_neighbours(n, loc, heights, positions):
    neighbours = [x for x in find_neighbours(n, loc) if x in positions if heights[x][1] >= heights[loc][1]]
    
    return len(neighbours)