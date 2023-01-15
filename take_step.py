import math
import random
import find_neighbours
import numpy as np
import find_type
import find_F_type
from find_type_migration import find_type_migration

k = 1.380649*(10**(-23))


def take_step(n, deltaMu, phi, Epb, T, buckets):
    loc = random.randint(0, (n ** 2)-1)
    c = find_neighbours.find_neighbours(n, loc)
    c.append(loc)
    z = random.uniform(0,1)
    attachment = math.e ** (deltaMu / (k * T))
    detachment = math.e ** ((phi / (k * T)) - (1 * Epb / (k * T)))
    migration = math.e ** ((phi / (k * T)) - ((1 * Epb) / (k * T)) + (Epb / (2 * k * T)))
    summ = attachment + detachment + migration
    F_or_S = ""
    F_tried = None
    F_succeed = None
    S_tried = None
    S_succeed = None
    NSi_change_remove = []
    NSi_change_add = []
    NFi_change_remove_F = []
    NFi_change_add_F = []
    if buckets[loc] != 0:
        if z < attachment / summ:
            F_or_S = "F"
            F_tried = find_type.find_type(n, buckets, loc)
            F_succeed = F_tried
            NSi_change_remove = [find_type.find_type(n, buckets, x) for x in c]
            NFi_change_remove_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
            buckets[loc] += 1
            NSi_change_add = [find_type.find_type(n, buckets, x) for x in c]
            NFi_change_add_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
        elif attachment / summ < z < (attachment + detachment) / summ:
            F_or_S = "S"
            S_tried = find_type.find_type(n, buckets, loc)
            z2 = random.uniform(0, 1)
            bond_number = find_type.find_type(n, buckets, loc)
            if z2 < (math.e ** ((phi / (k * T)) - ((bond_number+1) * Epb / (k * T))))/(math.e ** ((phi / (k * T)) - (1 * Epb / (k * T)))):
                NSi_change_remove = [find_type.find_type(n, buckets, x) for x in c]
                NFi_change_remove_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
                buckets[loc] -= 1
                S_succeed = S_tried
                NSi_change_add = [find_type.find_type(n, buckets, x) for x in c]
                NFi_change_add_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
        elif (attachment + detachment) / summ < z:
            c2 = [term for term in c[0:-2] if buckets[term] <= buckets[loc]]
            # we now need to calculate the binding energies of these neighbours, and that of our current stack
            if c2:
                # we want a vector of probabilities of each stack based on the number of neighbours
                c3 = [find_type_migration(n, buckets, x, loc)+1 for x in c2]
                c3 = [term/sum(c3) for term in c3]
                term = random.choices(c2, c3)[0]
                z2 = random.uniform(0, 1)
                if z2 < (find_type.find_type(n, buckets, loc)+1)/(find_type.find_type(n, buckets, loc)+1+find_type_migration(n, buckets, term, loc)+1):
                    c4 = find_neighbours.find_neighbours(n, term)
                    c5 = list(set(c + c4))
                    NSi_change_remove = [find_type.find_type(n, buckets, x) for x in c5]
                    NFi_change_remove_F = [find_F_type.find_F_type(n, buckets, x) for x in c5]
                    buckets[loc] -= 1
                    buckets[term] += 1
                    NSi_change_add = [find_type.find_type(n, buckets, x) for x in c5]
                    NFi_change_add_F = [find_F_type.find_F_type(n, buckets, x) for x in c5]
    else:
        if z < attachment / summ:
            F_or_S = "F"
            F_tried = find_type.find_type(n, buckets, loc)
            F_succeed = F_tried
            NSi_change_remove = [find_type.find_type(n, buckets, x) for x in c]
            NFi_change_remove_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
            buckets[loc] += 1
            NSi_change_add = [find_type.find_type(n, buckets, x) for x in c]
            NFi_change_add_F = [find_F_type.find_F_type(n, buckets, x) for x in c]
    # return [buckets, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    # return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed]