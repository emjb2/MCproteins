import math
import random
from find_neighbours import find_neighbours
import numpy as np
from find_type import find_type
from find_F_type import find_F_type
from find_type_migration import find_type_migration
from find_tetramer_sites import find_tetramer_sites
from find_dimer_sites import find_dimer_sites
from return_me import return_me

k = 1.380649*(10**(-23))

def take_stepA(n, deltaMu, phi, Epb, T, buckets, mol_dist):
    #mol_type_functions = [return_me(), find_dimer_sites(), find_tetramer_sites()]
    loc = random.randint(0, (n ** 2)-1)
    c = find_neighbours(n, loc)
    c.append(loc)
    h = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
    # h = find_type(n, buckets, loc)+1
    z = random.uniform(0,1)
    attachment = math.e ** (deltaMu / (k * T))
#   h is the number of bonds of that specific molecule! See Ke et al equ (2) 
    detachment = math.e ** ((phi / (k * T)) - (h * Epb / (k * T)))
    migration = math.e ** ((phi / (k * T)) - ((h * Epb) / (k * T)) + (Epb / (2 * k * T)))
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
    if buckets[loc] != 1:
        if z < attachment / summ:
            z_mol = random.choices([0,1,2], mol_dist)[0]
            if z_mol == 0:
                #F_or_S = "F"
                #F_tried = find_type(n, buckets, loc)
                #F_succeed = F_tried
                #NSi_change_remove = [find_type(n, buckets, x) for x in c]
                #NFi_change_remove_F = [find_F_type(n, buckets, x) for x in c]
                buckets[loc] += 1
                #NSi_change_add = [find_type(n, buckets, x) for x in c]
                #NFi_change_add_F = [find_F_type(n, buckets, x) for x in c]
            elif z_mol == 1:
                viable_options = find_dimer_sites(n, loc, buckets)
                if viable_options:
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1
            elif z_mol ==2:
                viable_options = find_tetramer_sites(n, loc, buckets)
                if viable_options:
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1               
        elif attachment / summ < z < (attachment + detachment) / summ:
            #F_or_S = "S"
            #S_tried = find_type(n, buckets, loc)
            z2 = random.uniform(0, 1)
            bond_number = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
            if z2 < (math.e ** ((bond_number * Epb / (k * T))))/(math.e ** (((1/6)*(phi/Epb) * Epb / (k * T)))):
                #NSi_change_remove = [find_type(n, buckets, x) for x in c]
                #NFi_change_remove_F = [find_F_type(n, buckets, x) for x in c]
                buckets[loc] -= 1
                #S_succeed = S_tried
                #NSi_change_add = [find_type(n, buckets, x) for x in c]
                #NFi_change_add_F = [find_F_type(n, buckets, x) for x in c]
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
                    #NSi_change_remove = [find_type(n, buckets, x) for x in c5]
                    #NFi_change_remove_F = [find_F_type(n, buckets, x) for x in c5]
                    buckets[loc] -= 1
                    buckets[term] += 1
                    #NSi_change_add = [find_type(n, buckets, x) for x in c5]
                    #NFi_change_add_F = [find_F_type(n, buckets, x) for x in c5]
    else:
        if z < attachment / summ:
            z_mol = random.choices([0,1,2], mol_dist)[0]
            if z_mol == 0:
                #F_or_S = "F"
                #F_tried = find_type(n, buckets, loc)
                #F_succeed = F_tried
                #NSi_change_remove = [find_type(n, buckets, x) for x in c]
                #NFi_change_remove_F = [find_F_type(n, buckets, x) for x in c]
                buckets[loc] += 1
                #NSi_change_add = [find_type(n, buckets, x) for x in c]
                #NFi_change_add_F = [find_F_type(n, buckets, x) for x in c]
            elif z_mol == 1:
                viable_options = find_dimer_sites(n, loc, buckets)
                if viable_options:
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1
            elif z_mol ==2:
                viable_options = find_tetramer_sites(n, loc, buckets)
                if viable_options:
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1      
    # return [buckets, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    # THIS ONE return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
    return [buckets]
    # return [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed]
