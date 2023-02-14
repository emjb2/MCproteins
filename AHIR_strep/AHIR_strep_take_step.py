from random import choices
from random import uniform
from math import e
from copy import deepcopy
from is_attachment_possible import is_attachment_possible
from how_many_neighbours import how_many_neighbours
from AHIR_or_strep import AHIR_or_strep

k = 1.380649*(10**(-23))

def AHIR_strep_take_step(n, AHIR_strep_dist, positions, heights, deltaMu,T):
    current_stack = choices(positions)
    current_height = heights(current_stack)
    edited_heights = heights
    edited_heights[current_stack] += 1
    whats_there_now = AHIR_or_strep(n, current_stack, current_height)
    what_would_be_added = AHIR_or_strep(n, current_stack, edited_heights)
    edited_heights == heights
    edited_heights[current_stack] += 1
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    attachment_prob = e ** (deltaMu / (k*T) + (how_many_neighbours(n, current_stack, edited_heights)/total_links[what_would_be_added]))
    detachment_prob = e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights))
    summ = attachment_prob + detachment_prob
    is_attachment_possible = is_attachment_possible(n, current_stack, heights)
    if z < attachment_prob/summ and is_attachment_possible == 1:
        heights[current_stack] += 1
    elif z > detachment_prob/summ:
        z2 = uniform(0,1)
        if z2 < e ** (total_links[whats_there_now]-how_many_neighbours(n, current_stack, heights))/ (e ** (total_links[whats_there_now]-1)):
            heights[current_stack] -= 1
    return heights
