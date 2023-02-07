from find_neighbours import find_neighbours


def find_type_migration(n, buckets, this_one, coming_from):
    c = find_neighbours(n, this_one)
    here = c.index(coming_from)
    heights = [buckets[x] for x in c]
    heights[here] -= 1
    return sum(x >= (buckets[this_one]+1) for x in heights)
