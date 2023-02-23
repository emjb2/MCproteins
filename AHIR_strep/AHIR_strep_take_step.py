from random import choices
from random import uniform
from math import e
from copy import deepcopy
from AHIR_strep.is_attachment_possible import is_attachment_possible
from AHIR_strep.how_many_neighbours import how_many_neighbours
from AHIR_strep.AHIR_or_strep import AHIR_or_strep
from general_functions.find_neighbours import find_neighbours

k = 1.380649*(10**(-23))

def AHIR_strep_take_step(n, AHIR_strep_dist, positions, strep_only, both, heights, deltaMu, T):
    current_stack = choices(positions, k=1)[0]
    current_height = heights[current_stack]
    edited_heights = heights
    edited_heights[current_stack] += 1
    # strep is 0, AHIR is 1
    whats_there_now = AHIR_or_strep(n, current_stack, strep_only, current_height)
    #what_would_be_added = AHIR_or_strep(n, current_stack, edited_heights[current_stack])
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    attachment_prob = e ** (deltaMu / (k*T))
    detachment_prob = e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights, positions))
    summ = attachment_prob + detachment_prob
    attachment_possible = is_attachment_possible(n, current_stack, heights, strep_only)
    if current_height > 1:
        if z < attachment_prob/summ and attachment_possible == 1:
            heights[current_stack] += 1
            if current_stack in both:
                if heights[current_stack]%2 == 1:
                    neighbours = find_neighbours(n, current_stack)
                    for i in neighbours:
                        heights[i] == heights[current_stack]-1

        elif z > detachment_prob/summ:
            z2 = uniform(0,1)
            if z2 < e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights, positions))/ (e ** (total_links[whats_there_now]-1)):
                heights[current_stack] -= 1
    else:
        if z < attachment_prob/summ and is_attachment_possible == 1:
            heights[current_stack] += 1
    
    return heights
