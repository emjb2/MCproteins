import math
import random
from general_functions.find_neighbours import find_neighbours
import numpy as np
from general_functions.find_type import find_type
from general_functions.find_F_type import find_F_type
from general_functions.find_type_migration import find_type_migration

k = 1.380649*(10**(-23))

def take_step(n, deltaMu, phi, Epb, T, buckets):
    loc = random.randint(0, (n ** 2)-1)
    c = find_neighbours(n, loc)
    c.append(loc)
    h = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
    # h = find_type(n, buckets, loc)+1
    z = random.uniform(0,1)
    attachment = math.e ** (deltaMu / (k * T))
#   h is the number of bonds of that specific molecule! See Ke et al equ (2) 
    detachment = math.e ** (((phi / (k * T)) - (h * Epb / (k * T))))
    migration = math.e ** (((phi / (k * T)) - ((h * Epb) / (k * T))) + (Epb / (2 * k * T)))
    summ = attachment + detachment + migration

    if buckets[loc] != 1:
        if z < attachment / summ:
            buckets[loc] += 1
        elif attachment / summ < z < (attachment + detachment) / summ:
            z2 = random.uniform(0, 1)
            bond_number = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
            if z2 < (math.e ** ((((phi/Epb)-bond_number) * Epb / (k * T))))/(math.e ** (((((5/6)*phi/Epb))* Epb / (k * T)))):
                buckets[loc] -= 1
        elif (attachment + detachment) / summ < z:
            c2 = [term for term in c[0:-2] if buckets[term] <= buckets[loc]]
            # we now need to calculate the binding energies of these neighbours, and that of our current stack
            if c2:
                # we want a vector of probabilities of each stack based on the number of neighbours
                c3 = [(find_type_migration(n, buckets, x, loc)+1)/6*(phi/Epb) for x in c2]
                c3 = [math.e ** (h * Epb / (k * T)) for h in c3]
                c3 = [term/sum(c3) for term in c3]
                term = random.choices(c2, c3)[0]
                z2 = random.uniform(0, 1)
                if z2 < math.e ** ((find_type(n, buckets, loc)+1)/6*phi/(k*T))/(math.e ** ((find_type(n, buckets, loc)+1)/6*phi/(k*T)) + math.e ** ((find_type_migration(n, buckets, term, loc)+1)/6*phi/(k*T))):
                    c4 = find_neighbours(n, term)
                    c5 = list(set(c + c4))
                    buckets[loc] -= 1
                    buckets[term] += 1
    else:
        if z < attachment / summ:
            buckets[loc] += 1
    # return [buckets, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    # return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    # return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed]
    return buckets
