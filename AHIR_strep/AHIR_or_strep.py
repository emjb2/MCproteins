#This function should tell me whether the current molecule in a particular stack is AHIR or strep.

def AHIR_or_strep(n, loc, strep_only, height):
    # strep is 0, AHIR is 1
    if loc in strep_only:
        return 0
    else:
        if height%2 == 1:
            return 1
        else:
            return 0
