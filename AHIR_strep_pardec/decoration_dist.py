

def decoration_dist(deltaMu):
    # there'S space here to define some weird entropy distributions
    # the return is densities of partial decoration from AHIR with 0 to 6 strep attachments
    # the final number is pure strep.

    # equal initial AHIR and strep, equal proportions of AHIR decoration:
    #return [15/36, 1/36, 1/36, 1/36, 1/36, 1/36, 1/36, 0]

    # 50/50 single strep and decorated AHIR, each AHIR decoration is in equal proportion to the others.
    # return [1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/2]

    # just super decorated AHIR to check that my model isn't complete bullshit
    #  return [0, 0, 0, 0, 0, 0, 1, 0]

    # make AHIRs more decorated with increasing supersaturation
    if deltaMu < 10:
        [list1, list2] = [[(1-deltaMu/10)*x for x in [7/28, 6/28, 5/28, 4/28, 3/28, 2/28, 1/28, 0]], [deltaMu/10*x for x in [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]]]
        distt = [list1[i]+list2[i] for i in range(8)]
    elif deltaMu == 10:
        distt = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]
    else:
        [list1, list2] = [[(1-(deltaMu-10)/10)*x for x in [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]], [((deltaMu-10)/10)*x for x in [1/28, 2/28, 3/28, 4/28, 5/28, 6/28, 7/28,0]]]
        distt = [list1[i]+list2[i] for i in range(8)]
    
        return distt
