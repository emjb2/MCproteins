from random import sample
from general_functions.find_neighbours import find_neighbours

def attach_pardec_mol(loc, heights, strep_spaces, strep_attachments, would_be_height_with_AHIR):
    current_height = heights[loc]
    if loc in strep_spaces:
        heights[loc] += 2
        strep_attachments -= 1
        strep_spaces.remove(loc)
    else:
        heights[loc] += 1

    if len(strep_spaces) < strep_attachments:
        heights[loc] += 1
        strep_attachments -= 1
    add = sample(strep_spaces, k=strep_attachments)
    for i in add:
        heights[i] = would_be_height_with_AHIR
        strep_spaces.remove(i)

    # now check if any strep places next to the now attached AHIR have become available
    for i in strep_spaces:
        heights[i] = would_be_height_with_AHIR - 1
    
    return heights

        

