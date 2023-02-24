from general_functions.find_neighbours import find_neighbours
from AHIR_strep.AHIR_or_strep import AHIR_or_strep

def how_many_strep_spaces(n, loc, heights):
    count = 0
    options = []
    current_height = heights[loc]
    # find what the height would be if we add the AHIR
    if heights[loc]%2 == 1:
        height_with_new_AHIR = current_height + 2
        options.append(loc)
    else:
        height_with_new_AHIR = current_height + 1

    options = options + [x for x in find_neighbours(n, loc) if heights[x] in [height_with_new_AHIR-1, height_with_new_AHIR-2]]
    # count will also count the strep you can place above.
    count += len(options) + 1

    return [count, options, height_with_new_AHIR]
