from random import choices
from random import uniform
from math import e
from copy import deepcopy
from AHIR_strep.is_attachment_possible import is_attachment_possible
from AHIR_strep.how_many_neighbours import how_many_neighbours
from AHIR_strep.AHIR_or_strep import AHIR_or_strep
from general_functions.find_neighbours import find_neighbours

k = 1.380649*(10**(-23))

def AHIR_strep_take_step_same_detach_strep_AHIR(n, AHIR_strep_dist, positions, strep_only, both, heights, deltaMu, T, Epb, phi):
    track = 0
    current_stack = choices(positions, k=1)[0]
    current_height = heights[current_stack]
    # strep is 0, AHIR is 1
    whats_there_now = AHIR_or_strep(n, current_stack, strep_only, current_height)
    #what_would_be_added = AHIR_or_strep(n, current_stack, edited_heights[current_stack])
    total_links = {0: 2, 1: 6}
    z = uniform(0,1)
    if whats_there_now == 0:
        if current_height%2 == 1:
        #h = ((how_many_neighbours(n, current_stack, heights, positions))/total_links[whats_there_now])*(phi/Epb)
            h = ((how_many_neighbours(n, current_stack, heights, positions))/6)*(phi/Epb)
        else:
            h=(1/6)*(phi/Epb)
    else:
        #h = ((how_many_neighbours(n, current_stack, heights, positions)+1)/total_links[whats_there_now])*(phi/Epb)
        h = ((how_many_neighbours(n, current_stack, heights, positions)+1)/6)*(phi/Epb)
    attachment_prob = e ** (deltaMu / (k*T))
    detachment_prob = e ** ((phi / (k * T)) - (h * Epb / (k * T)))
    summ = attachment_prob + detachment_prob
    attachment_possible = is_attachment_possible(n, current_stack, heights, strep_only)
    if current_height > 1:
        if z < attachment_prob/summ and attachment_possible == 1:
            heights[current_stack] += 1
            track += 1
            # check if any heights need to be adjusted
            if current_stack in both:
                if heights[current_stack]%2 == 1:
                    neighbours = find_neighbours(n, current_stack)
                    for i in neighbours:
                        if heights[i] == heights[current_stack]-2:
                            heights[i] = heights[current_stack]-1
            # check if you're allowed to build on top of the strep you've added
            elif current_stack in strep_only:
                neighbours = find_neighbours(n, current_stack)
                is_tall = [1 for x in neighbours if x in positions if heights[x] >= heights[current_stack]+2]
                if is_tall:
                    heights[current_stack] += 1

        elif z > attachment_prob/summ:
            z2 = uniform(0,1)
            max_frac = {0: 1/2, 1: 5/6}
            if z2 < (e ** ((((phi/Epb)-h) * Epb / (k * T))))/(e ** (((((5/6)*phi/Epb))* Epb / (k * T)))):
            #if z2 < (e ** ((((phi/Epb)-h) * Epb / (k * T))))/(e ** (((((max_frac[whats_there_now])*phi/Epb))* Epb / (k * T)))):
                if current_stack in both:
                    heights[current_stack] -= 1
                    track -= 1
                    #if you removed an AHIR then also remove loose streps and strep possibilities
                    if heights[current_stack]%2 == 0:
                        neighbours = find_neighbours(n, current_stack)
                        for i in neighbours:
                            if heights[i] == heights[current_stack]+1:
                                i_neighbours_heights = [1 for x in find_neighbours(n, i) if x in positions if heights[x] >= heights[i]]
                                if not i_neighbours_heights:
                                    heights[i] -= 2
                                    track -= 1
                            elif heights[i] == heights[current_stack]:
                                i_neighbours_heights = [1 for x in find_neighbours(n, i) if x in positions if heights[x] >= heights[current_stack]+1]
                                if not i_neighbours_heights:
                                    heights[i] -= 1
                if current_stack in strep_only:
                    if heights[current_stack]%2 == 1:
                        heights[current_stack] -= 1
                        track -= 1
                    else:
                        heights[current_stack] -= 2
                        track -= 1

    else:
        #print(attachment_possible)
        #print(z)
        #print(attachment_prob/summ)
        if z < attachment_prob/summ and attachment_possible == 1:
            heights[current_stack] += 1
            track += 1
    
    if track > 1:
        print("PROBLEM")
    return [heights, track]
