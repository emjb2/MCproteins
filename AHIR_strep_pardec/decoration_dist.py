

def decoration_dist():
    # there'S space here to define some weird entropy distributions
    # the return is densities of partial decoration from AHIR with 0 to 6 strep attachments
    # the final number is pure strep.

    # equal initial AHIR and strep, equal proportions of AHIR decoration:
    # return [15/36, 1/36, 1/36, 1/36, 1/36, 1/36, 1/36, 0]

    # 50/50 single strep and decorated AHIR, each AHIR decoration is in equal proportion to the others.
    return [1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/2]

    # just super decorated AHIR to check that my model isn't complete bullshit
    #  return [0, 0, 0, 0, 0, 0, 1, 0]