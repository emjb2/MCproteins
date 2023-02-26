from random import sample
from general_functions.find_neighbours import find_neighbours

def attach_pardec_mol(loc, heights, strep_spaces, strep_attachments, would_be_height_with_AHIR):
    if set(strep_attachments) <= set(strep_spaces):
        if loc in strep_attachments:
            heights[loc] += 2
            strep_spaces.remove(loc)
            strep_attachments.remove(loc)
        else:
            heights[loc] += 1
        if "above" in strep_attachments:
            heights[loc] += 1
            strep_spaces.remove("above")
            strep_attachments.remove("above")
        for i in strep_attachments:
            heights[i] = would_be_height_with_AHIR
            strep_spaces.remove(i)
        # now check if any new streps have become available:
        if "above" in strep_spaces:
            # first remove the above thing if it's still there, you don' need to check for this strep
            strep_spaces.remove("above")
        for i in strep_spaces:
            heights[i] = would_be_height_with_AHIR - 1




    
    #if loc in strep_spaces:
    #    heights[loc] += 2
    #    strep_attachments = strep_attachments - 1
    #    strep_spaces.remove(loc)

    #strep_spaces.append(loc)
    #add = sample(strep_spaces, k=strep_attachments)
    #if loc in add:
    #    heights[loc] += 1
    #    add.remove(loc)
    #for i in add:
    #    heights[i] = would_be_height_with_AHIR
    #    strep_spaces.remove(i)

    # check if new streps are now possible     
    #if loc in strep_spaces:
    #    strep_spaces.remove(loc)   
    #for i in strep_spaces:
    #    heights[i] == would_be_height_with_AHIR - 1

    return heights

        

