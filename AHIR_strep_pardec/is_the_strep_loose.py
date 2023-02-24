from general_functions.find_neighbours import find_neighbours

def is_the_strep_loose(n, loc, heights, strep_only, both):
# 1 is yes, 0 is no
    if loc in strep_only:
        # counts heights above and equal to the strep
        count = [1 for x in find_neighbours(n, loc) if x in both if heights[x] >= heights[loc]]
        if count:
            return 0
        else:
            return 1