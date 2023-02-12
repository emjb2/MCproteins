import math
import random
from general_functions.find_neighbours import find_neighbours
import numpy as np
from general_functions.find_type import find_type
from general_functions.find_F_type import find_F_type
from general_functions.find_type_migration import find_type_migration
from aggregate_model.find_tetramer_sites import find_tetramer_sites
from aggregate_model.find_dimer_sites import find_dimer_sites
from general_functions.return_me import return_me

k = 1.380649*(10**(-23))

def take_stepA(n, deltaMu, phi, Epb, T, buckets, mol_dist, attachment_attempts, attachment_count, removal_count, failed_attachments):
    #mol_type_functions = [return_me(), find_dimer_sites(), find_tetramer_sites()]
    loc = random.randint(0, (n ** 2)-1)
    c = find_neighbours(n, loc)
    c.append(loc)
    # h = find_type(n, buckets, loc)+1
    h = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
    z = random.uniform(0,1)
    attachment = math.e ** (deltaMu / (k * T))
#   h is the number of bonds of that specific molecule! See Ke et al equ (2) 
    detachment = math.e ** ((phi / (k * T)) - (h * Epb / (k * T)))
    migration = math.e ** ((phi / (k * T)) - ((h * Epb) / (k * T)) + (Epb / (2 * k * T)))
    summ = attachment + detachment + migration
    #summ = attachment + detachment
    if buckets[loc] > 1:
        if z < attachment / summ:
            z_mol = random.choices([0,1,2], mol_dist)[0]
            if z_mol == 0:
                attachment_count += 1
                attachment_attempts += 1
                buckets[loc] += 1
            elif z_mol == 1:
                attachment_attempts += 2
                viable_options = find_dimer_sites(n, loc, buckets)
                if viable_options:
                    attachment_count += 2
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1
                else:
                    failed_attachments += 2
            elif z_mol ==2:
                attachment_attempts += 4
                viable_options = find_tetramer_sites(n, loc, buckets)
                if viable_options:
                    attachment_count += 4
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1 
                else:
                    failed_attachments += 4              
        elif attachment / summ < z < (attachment + detachment) / summ:
            # here we're gonna try just detaching, not maybe detaching depending on energy
            # detachment of what kind of molecule            
            z2 = 0
            # z2 = random.choices([0,1,2], mol_dist)[0]
            if z2 == 0:
                z3 = random.uniform(0, 1)
                bond_number = ((find_type(n, buckets, loc)+1)/6)*(phi/Epb)
                if z3 < (math.e ** ((bond_number * Epb / (k * T))))/(2*(math.e ** (((1/6)*(phi/Epb) * Epb / (k * T))))):
                    removal_count += 1
                    buckets[loc] -= 1
            elif z2 == 1:
                viable_options = find_dimer_sites(n, loc, buckets)
                if viable_options:
                    removal_option = random.choice(viable_options)
                    bond_number1 = ((find_type(n, buckets, removal_option[0])+1)/6)*(phi/Epb)
                    bond_number2 = ((find_type(n, buckets, removal_option[1])+1)/6)*(phi/Epb)
                    z3 = random.uniform(0,1)
                    if z3 < (math.e ** ((bond_number1 * Epb / (k * T))) + math.e ** ((bond_number2 * Epb / (k * T))))/(2*(math.e ** (((1/6)*(phi/Epb) * Epb / (k * T))))):
                        buckets[removal_option[0]] -= 1
                        buckets[removal_option[1]] -= 1
                        removal_count += 2
            elif z2 ==2:
                viable_options = find_tetramer_sites(n, loc, buckets)
                if viable_options:
                    removal_option = random.choice(viable_options)
                    bond_number1 = ((find_type(n, buckets, removal_option[0])+1)/6)*(phi/Epb)
                    bond_number2 = ((find_type(n, buckets, removal_option[1])+1)/6)*(phi/Epb)
                    bond_number3 = ((find_type(n, buckets, removal_option[2])+1)/6)*(phi/Epb)
                    bond_number4 = ((find_type(n, buckets, removal_option[3])+1)/6)*(phi/Epb)                    
                    z3 = random.uniform(0,1)
                    if z3 < (math.e ** ((bond_number1 * Epb / (k * T))) + math.e ** ((bond_number2 * Epb / (k * T))) + math.e ** ((bond_number3 * Epb / (k * T))) + math.e ** ((bond_number4 * Epb / (k * T))))/(4*(math.e ** (((1/6)*(phi/Epb) * Epb / (k * T))))):
                        buckets[removal_option[0]] -= 1
                        buckets[removal_option[1]] -= 1
                        buckets[removal_option[2]] -= 1
                        buckets[removal_option[3]] -= 1                        
                        removal_count += 4
        elif (attachment + detachment) / summ < z:
            c2 = [term for term in c[0:-2] if buckets[term] <= buckets[loc]]
            # we now need to calculate the binding energies of these neighbours, and that of our current stack
            if c2:
                # we want a vector of probabilities of each stack based on the number of neighbours
                c3 = [(find_type_migration(n, buckets, x, loc)+1)/6*(phi/Epb) for x in c2]
                c3 = [math.e ** (h * Epb / (k * T)) for h in c3]
                c3 = [term/sum(c3) for term in c3]
                term = random.choices(c2, c3)[0]
                #z2 = random.uniform(0, 1)
                #if z2 < math.e ** ((find_type(n, buckets, loc)+1)/6*phi/(k*T))/(math.e ** ((find_type(n, buckets, loc)+1)/6*phi/(k*T)) + math.e ** ((find_type_migration(n, buckets, term, loc)+1)/6*phi/(k*T))):
                #    c4 = find_neighbours(n, term)
                #    c5 = list(set(c + c4))
                buckets[loc] -= 1
                buckets[term] += 1
    else:
        if z < attachment / summ:
            z_mol = random.choices([0,1,2], mol_dist)[0]
            if z_mol == 0:
                attachment_attempts += 1
                attachment_count += 1
                buckets[loc] += 1
            elif z_mol == 1:
                attachment_attempts += 2
                viable_options = find_dimer_sites(n, loc, buckets)
                if viable_options:
                    attachment_count += 2
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1
                else:
                    failed_attachments += 2
            elif z_mol ==2:
                attachment_attempts += 4
                viable_options = find_tetramer_sites(n, loc, buckets)
                if viable_options:
                    attachment_count += 4
                    add_one = random.choice(viable_options)
                    for x in add_one:
                        buckets[x] += 1     
                else:
                    failed_attachments += 4
    return [buckets, attachment_attempts, attachment_count, removal_count, failed_attachments]
