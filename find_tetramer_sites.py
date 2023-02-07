from find_neighbours import find_neighbours

def find_tetramer_sites(n, loc, buckets):
    # order is right, left, down, up
    neighbours = find_neighbours(n, loc)
    height = buckets[loc]
    viable_locs = []
    last_pieces = [find_neighbours(neighbours[0])[2], find_neighbours(neighbours[1])[2], find_neighbours(neighbours[1])[3], find_neighbours(neighbours[0])[3]]
    if buckets[neighbours[0]] == buckets[neighbours[2]] == buckets[last_pieces[0]] == height:
        viable_locs.append[neighbours[0], neighbours[2], last_pieces[0], loc]
    if buckets[neighbours[2]] == buckets[neighbours[1]] == buckets[last_pieces[1]] == height:
        viable_locs.append[neighbours[2], neighbours[1], last_pieces[0], loc]
    if buckets[neighbours[1]] == buckets[neighbours[3]] == buckets[last_pieces[2]] == height:
        viable_locs.append[neighbours[1], neighbours[3], last_pieces[2], loc]
    if buckets[neighbours[3]] == buckets[neighbours[0]] == buckets[last_pieces[3]] == height:
        viable_locs.append[neighbours[3], neighbours[0], last_pieces[3], loc]
    return viable_locs

