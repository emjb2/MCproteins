from find_neighbours import find_neighbours


def find_type(n, buckets, loc):
    c = find_neighbours(n, loc)
    print(c)
    print(len(buckets))
    heights = [buckets[x] for x in c]
    return sum(x >= buckets[loc] for x in heights)
