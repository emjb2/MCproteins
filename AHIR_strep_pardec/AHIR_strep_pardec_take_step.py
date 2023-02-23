from random import choices
from random import uniform
from math import e
from copy import deepcopy
from AHIR_strep.is_attachment_possible import is_attachment_possible
from AHIR_strep.how_many_neighbours import how_many_neighbours
from AHIR_strep.AHIR_or_strep import AHIR_or_strep
from general_functions.find_neighbours import find_neighbours
from AHIR_strep_pardec.how_many_strep_spaces import how_many_strep_spaces
from AHIR_strep_pardec.attach_pardec_mol import attach_pardec_mol

k = 1.380649*(10**(-23))

def AHIR_strep_pardec_take_step(n, positions, strep_only, both, heights, deltaMu, T, decoration_dist):
    current_stack = choices(positions, k=1)[0]
    current_height = heights[current_stack]
    # strep is 0, AHIR is 1
    whats_there_now = AHIR_or_strep(n, current_stack, strep_only, current_height)
    #what_would_be_added = AHIR_or_strep(n, current_stack, edited_heights[current_stack])
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    attachment_prob = e ** (deltaMu / (k*T))
    detachment_prob = e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights, positions))
    summ = attachment_prob + detachment_prob
    attachment_possible = is_attachment_possible(n, current_stack, heights, strep_only)
        
    if z < attachment_prob/summ and attachment_possible == 1:
        #if we have no strep we're gonna only pick from possible AHIR attachment sites
        if decoration_dist[-1] == 0:
            if current_stack in strep_only:
                current_stack = choices([x for x in find_neighbours(n, current_stack) if x in both])[0]
            mol_type = choices([0, 1, 2, 3, 4, 5, 6, 7], decoration_dist, k=1)[0]
            #checking how many check spaces there are around the AHIR
            [strep_space_count, strep_spaces, would_be_height_with_AHIR] = how_many_strep_spaces(n, current_stack, heights)
            if strep_space_count >= mol_type and not (mol_type == 0):
                heights = attach_pardec_mol(current_stack, heights, strep_spaces, mol_type, would_be_height_with_AHIR)
            elif mol_type == 0:
                if current_stack not in strep_spaces:
                    heights[current_stack] += 1
                    print("here5")
        else:
            mol_type = choices([0, 1, 2, 3, 4, 5, 6, 7], decoration_dist, k=1)[0]
            if mol_type == 7:
                if current_stack in strep_only:
                    if current_height%2 == 0:
                        heights[current_stack] += 1
                        print("here6")
                else:
                    if current_height%2 == 1:
                        heights[current_stack] += 1
                        print("here7")
            else:
                if current_stack in strep_only:
                    current_stack = choices([x for x in find_neighbours(n, current_stack) if x in both])[0]
                mol_type = choices([0, 1, 2, 3, 4, 5, 6, 7], decoration_dist, k=1)[0]
                #checking how many check spaces there are around the AHIR
                [strep_space_count, strep_spaces, would_be_height_with_AHIR] = how_many_strep_spaces(n, current_stack, heights)
                if strep_space_count >= mol_type and not (mol_type == 0):
                    heights = attach_pardec_mol(current_stack, heights, strep_spaces, mol_type, would_be_height_with_AHIR)
                elif mol_type == 0:
                    if current_stack not in strep_spaces:
                        heights[current_stack] += 1
                        print("here8")
                           
    elif z > detachment_prob/summ:
        if current_height > 1:
            z2 = uniform(0,1)
            if z2 < e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights, positions))/ (e ** (total_links[whats_there_now]-1)):
                heights[current_stack] -= 1
    
    return heights
