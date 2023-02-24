from random import sample
from general_functions.find_neighbours import find_neighbours

def attach_pardec_mol(loc, heights, strep_spaces, strep_attachments, would_be_height_with_AHIR):
    if loc in strep_spaces:
        heights[loc] += 2

        strep_attachments = strep_attachments - 1
        strep_spaces.remove(loc)

        if len(strep_spaces) < strep_attachments:
            heights[loc] += 1
            strep_attachments -= 1

            add = sample(strep_spaces, k=strep_attachments)
            for i in add:
                heights[i] = would_be_height_with_AHIR
                strep_spaces.remove(i)
            
            for i in strep_spaces:
                heights[i] == would_be_height_with_AHIR - 1

        else:
            add = sample(strep_spaces, k=strep_attachments)
            for i in add:
                heights[i] = would_be_height_with_AHIR
                strep_spaces.remove(i)
            
            for i in strep_spaces:
                heights[i] == would_be_height_with_AHIR - 1

    else:
        heights[loc] += 1


        if len(strep_spaces) < strep_attachments:
            heights[loc] += 1
            strep_attachments -= 1

            add = sample(strep_spaces, k=strep_attachments)
            for i in add:
                heights[i] = would_be_height_with_AHIR
                strep_spaces.remove(i)
            
            for i in strep_spaces:
                heights[i] == would_be_height_with_AHIR - 1

        else:
            add = sample(strep_spaces, k=strep_attachments)
            for i in add:
                heights[i] = would_be_height_with_AHIR
                strep_spaces.remove(i)
            
            for i in strep_spaces:
                heights[i] == would_be_height_with_AHIR - 1
    
    return heights

        

