from random import sample
from general_functions.find_neighbours import find_neighbours

def attach_pardec_mol(n, positions, loc, heights, strep_spaces, strep_attachments, would_be_height_with_AHIR, track):
    if set(strep_attachments) <= set(strep_spaces):
        if loc in strep_attachments:
            heights[loc] += 2
            track += 2
            strep_spaces.remove(loc)
            strep_attachments.remove(loc)
        else:
            heights[loc] += 1
            track += 1
        if "above" in strep_attachments:
            heights[loc] += 1
            track += 1
            strep_spaces.remove("above")
            strep_attachments.remove("above")
        for i in strep_attachments:
            heights[i] = would_be_height_with_AHIR
            track += 1
            strep_spaces.remove(i)
            #check if another strep is allowed on top of this one
            tall_i_neighbours = [1 for x in find_neighbours(n, i) if x in positions if heights[x] > heights[i]+1]
            if tall_i_neighbours:
                heights[i] += 1
        # now check if any new streps have become available:
        if "above" in strep_spaces:
            # first remove the above thing if it's still there, you don't need to check for this strep
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

    return [heights, track]

        

