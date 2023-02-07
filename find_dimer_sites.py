from find_neighbours import find_neighbours

def find_dimer_sites(n, loc, buckets):
    # order is right, left, down, up
    neighbours = find_neighbours(n, loc)
    height = buckets[loc]
    other_poss = find_neighbours(neighbours[0])[2:3] + find_neighbours(neighbours[1])[2:3]
    neighbours.append(other_poss)
    viable_options = [[loc,x] for x in other_poss if buckets[x] == buckets[loc]]
    return viable_options
    