from random import choices
from general_functions.find_neighbours import find_neighbours

def attach_pardec_mol(loc, heights, strep_spaces, strep_attachments, would_be_height_with_AHIR):
    current_height = heights[loc]
    if loc in strep_spaces:
        heights[loc] = current_height + 2
        strep_attachments -= 1
        strep_spaces.remove(loc)
    if strep_attachments <= 4:
        add = choices(strep_spaces, k=strep_attachments)
        for i in add:
            heights[i] = would_be_height_with_AHIR
            strep_spaces.remove(i)
    else:
        for i in strep_spaces:
            heights[i] = would_be_height_with_AHIR
        heights[loc] += 1
    # now check if any strep places next to the now attached AHIR have become available
    for i in strep_spaces:
        heights[i] = would_be_height_with_AHIR - 1
    return heights

        

