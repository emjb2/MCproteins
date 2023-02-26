from random import choices
from random import sample
from random import uniform
from math import e
from copy import deepcopy
from AHIR_strep.is_attachment_possible import is_attachment_possible
from AHIR_strep.how_many_neighbours import how_many_neighbours
from AHIR_strep.AHIR_or_strep import AHIR_or_strep
from general_functions.find_neighbours import find_neighbours
from AHIR_strep_pardec.how_many_strep_spaces import how_many_strep_spaces
from AHIR_strep_pardec.attach_pardec_mol import attach_pardec_mol
from AHIR_strep_pardec.strep_check import strep_check
from AHIR_strep_pardec.is_the_strep_loose import is_the_strep_loose

k = 1.380649*(10**(-23))

def AHIR_strep_pardec_take_step(n, positions, strep_only, both, heights, deltaMu, T, decoration_dist, Epb):  
    current_stack = choices(positions, k=1)[0]
    #print(current_stack)
    current_height = heights[current_stack]
    # strep is 0, AHIR is 1
    whats_there_now = AHIR_or_strep(n, current_stack, strep_only, current_height)
    #what_would_be_added = AHIR_or_strep(n, current_stack, edited_heights[current_stack])
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    attachment_prob = e ** (deltaMu / (k*T))
    detachment_prob = e ** ((6-how_many_neighbours(n, current_stack, heights, positions))*Epb)
    summ = attachment_prob + detachment_prob
    attachment_possible = is_attachment_possible(n, current_stack, heights, strep_only)
        
    if z < attachment_prob/summ:
        #if we have no strep we're gonna only pick from possible AHIR attachment sites
        mol_type = choices([0, 1, 2, 3, 4, 5, 6, 7], decoration_dist, k=1)[0]
        if mol_type == 7 and attachment_possible == 1:
            if current_stack in strep_only:
                heights[current_stack] += 1
                # now check if strep is allowed to grow above this too!
                allowed = [1 for x in find_neighbours(n, current_stack) if x in positions if heights[x] > (heights[current_stack] + 1)]
                if allowed:
                    heights[current_stack] += 1
            else:
                if heights[current_stack]%2 == 1:
                    heights[current_stack] += 1
        elif mol_type == 0:
            if current_stack in both:
                if heights[current_stack]%2 == 0:
                    heights[current_stack] += 1
                    # now make sure you allow all streps next to it!
                    allowed = [x for x in find_neighbours(n, current_stack) if heights[x] == (heights[current_stack] - 2)]
                    for i in allowed:
                        heights[i] += 1
        else:
            if current_stack in both:
                # select from possibleplaces the attached streps could be
                strep_attachment_locations = sample(find_neighbours(n, current_stack)+[current_stack, "above"], k=mol_type)
                [count, options, would_be_height_with_AHIR] = how_many_strep_spaces(n, current_stack, heights)
                # if you need a strep to attach below, this strep must be on the molecule.
                if current_height%2 == 1:
                    if current_stack in strep_attachment_locations:
                        heights = attach_pardec_mol(current_stack, heights, options, strep_attachment_locations, would_be_height_with_AHIR)
                           
    elif z > attachment_prob/summ:
        if current_stack in strep_only:
            if current_height > 2:
                z2 = uniform(0,1)
                if z2 < e ** ((6-how_many_neighbours(n, current_stack, heights, positions))*Epb)/ (e ** (5*Epb)):       
                    if current_height%2 == 1:
                        heights[current_stack] -= 1
                    else:
                        heights[current_stack] -= 2
        else:
            if current_height > 1:
                z2 = uniform(0,1)
                if z2 < e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights, positions))/ (e ** (total_links[whats_there_now]-1)):       
                        if current_height%2 == 0:
                            heights[current_stack] -= 1
                        else:
                            heights[current_stack] -= 1
                            # check if you need to remove loose streps
                            neighbours = [x for x in find_neighbours(n, current_stack) if x in positions]
                            for i in neighbours:
                                neighbours_neighbour = [x for x in find_neighbours(n, i) if x in positions]
                                neighbours_neighbour.remove(current_stack)
                                if not heights[neighbours_neighbour[0]] > heights[current_stack]:
                                    heights[i] -= 2

    return heights
