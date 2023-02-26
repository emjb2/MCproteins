from random import sample
from random import uniform
from math import e
from AHIR_strep_twinned.whats_there_now import whats_there_now
from AHIR_strep_twinned.how_many_neighbours import how_many_neighbours
from general_functions.find_neighbours import find_neighbours

k = 1.380649*(10**(-23))

def AHIR_strep_twinned_take_step(n, positions, strep_only, both, heights, deltaMu, T, crysalin_strength, twinned_strength, intra_strength):
    current_stack = sample(positions, k=1)[0]
    current_height = heights[current_stack][1]
    # strep is 0, AHIR is 1
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    attachment_prob = e ** (deltaMu / (k*T))
    detachment_prob = e ** (total_links[whats_there_now(current_stack, heights, both)]-how_many_neighbours(n, current_stack, heights, positions))
    summ = attachment_prob + detachment_prob
    z2 = uniform(0,1)
    if z2 < attachment_prob/summ:
        mol_type = sample(["strep", "AHIR1", "AHIR2"], k=1)
        if mol_type == "strep":
            if current_stack in both:
                if current_height%2 == 1:
                    heights[current_stack] = [heights[current_stack][0], current_height+1]
            else:
                if current_height%2 == 0:
                    #edit this so that if the bridge is between different things then it is unlikely.
                    heights[current_stack][1] += 1
                    tall_neighbours = [x for x in find_neighbours(n, current_stack) if x in positions if heights[x][1] >= heights[current_stack][1]]
                    heights[current_stack][0] == sample([heights[x][0] for x in tall_neighbours], k=1)
                    #check if you can add more strep above
                    taller_neighbours = [x for x in find_neighbours(n, current_stack) if x in positions if heights[x][1] > heights[current_stack][1]+1]
                    if taller_neighbours:
                        heights[current_stack][1] += 1
        elif mol_type == "AHIR1":
            if current_stack in both:
                if current_height%2 == 0:
                    current_type = heights[current_stack][0]
                    attach_mol_type = 1
                    if current_type == 1:
                        strength = crysalin_strength
                    else:
                        strength = intra_strength
                    z3 = uniform(0,1)
                    if z3 < strength/(crysalin_strength+twinned_strength+intra_strength):
                        heights[current_stack] = [attach_mol_type, current_height + 1]
                        #check for surrounding streps that are now possible]
                        neighbours = [x for x in find_neighbours(n, current_stack) if heights[x][1] == current_height - 1]
                        for x in neighbours:
                            heights[x][1] += 1
        else:
            if current_stack in both:
                if current_height%2 == 0:
                    current_type = heights[current_stack][0]
                    attach_mol_type = 2
                    if current_type == 2:
                        strength = twinned_strength
                    else:
                        strength = intra_strength
                    z3 = uniform(0,1)
                    if z3 < strength/(crysalin_strength+twinned_strength+intra_strength):
                        heights[current_stack] = [attach_mol_type, current_height + 1]
                        #check for surrounding streps that are now possible]
                        neighbours = [x for x in find_neighbours(n, current_stack) if heights[x][1] == current_height - 1]
                        for x in neighbours:
                            heights[x][1] += 1
    else:
        if current_stack in both:
            z3  = uniform(0,1)
            current_type = heights[current_stack][0]
            # find how strong these links are:
            neighbour_types = [heights[x][0] for x in find_neighbours(n, current_stack) if x in positions if heights[x][1] == heights[current_stack][1]]
            current_strength = 0       
            for i in neighbour_types:
                if i == 1 and current_type == 1:
                    current_strength += crysalin_strength
                if i == 2 and current_type == 2:
                    current_strength += twinned_strength
                else:
                    current_strength += intra_strength
            total = total_links[whats_there_now(current_stack, heights, both)]*max(crysalin_strength, twinned_strength, intra_strength)
            if z3 < (total - current_strength)/total:
                heights[current_stack] = [0, current_height - 1]
                #check if you reomved an AHIR
                if current_height%2 == 1:
                    # if yes then you need to remove possible loose streps
                    neighbours = [x for x in find_neighbours(n, current_stack) if x in positions]
                    for i in neighbours:
                        neighbours_neighbour = [x for x in find_neighbours(n, i) if x in positions]
                        neighbours_neighbour.remove(current_stack)
                        if not heights[neighbours_neighbour[0]] > heights[current_stack]:
                            heights[i] -= 2
        else:
            # reset current height so you are actually looking at the strep, not the space above it
            if current_height%2 == 0:
                current_height -= 1
            current_type = heights[current_stack][0]
            # find how strong these links are:
            neighbour_types = [heights[x][0] for x in find_neighbours(n, current_stack) if x in positions if heights[x][1] == heights[current_stack][1]]
            current_strength = 0       
            for i in neighbour_types:
                if i == 1 and current_type == 1:
                    current_strength += crysalin_strength
                if i == 2 and current_type == 2:
                    current_strength += twinned_strength
                else:
                    current_strength += intra_strength

                

            
    return heights