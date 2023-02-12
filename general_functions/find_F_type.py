from general_functions.find_neighbours import find_neighbours


def find_F_type(n, buckets, loc):
    c = find_neighbours(n, loc)
    heights = [buckets[x] for x in c]
    return sum(x >= (buckets[loc]+1) for x in heights)