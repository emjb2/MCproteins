from general_functions.find_neighbours import find_neighbours
from AHIR_or_strep import AHIR_or_strep

def how_many_strep_spaces(n, loc, heights):
    count = 0
    options = []
    current_height = heights[loc]
    # finding what the height would be with another AHIR
    if current_height%2 == 0:
        would_be_height_with_added_AHIR = current_height + 1
    else:
        would_be_height_with_added_AHIR = current_height + 2
        count += 1
        options.append(loc)
    possible_neighbours = [x for x in find_neighbours(n, loc) if heights[x] == would_be_height_with_added_AHIR-1]
    options += possible_neighbours
    #we are not allowing for overhang
    count = count + len(possible_neighbours) + 1 #you have space above
    # note the space above is not explicitly included in options, but is an option
    return [count, options, would_be_height_with_added_AHIR]
