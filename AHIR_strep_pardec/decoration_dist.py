from math import e


def decoration_dist():
    # here's Dan's approximation dist, description found in paper.
    k = 1.380649*(10**(-23))
    T = 300
    E = k*T
    beta = 1/(k*T)
    streps = [0,1,2,3,4,5,6]
    partition_intermediate_func = [e**i for i in streps]
    partition_func = sum(partition_intermediate_func)
    probability_dist = [e**(i)/partition_func for i in streps]
    summ = sum(probability_dist)
    distt = [probability_dist[i]/summ for i in streps]

    # equal initial AHIR and strep, equal proportions of AHIR decoration:
    #return [15/36, 1/36, 1/36, 1/36, 1/36, 1/36, 1/36, 0]

    # 50/50 single strep and decorated AHIR, each AHIR decoration is in equal proportion to the others.
    # return [1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/2]

    # just super decorated AHIR to check that my model isn't complete bullshit
    # return [0, 0, 0, 0, 0, 0, 1, 0]

    # make AHIRs more decorated with increasing supersaturation
    #if deltaMu < 10:
    #    [list1, list2] = [[(1-deltaMu/10)*x for x in [7/28, 6/28, 5/28, 4/28, 3/28, 2/28, 1/28, 0]], [deltaMu/10*x for x in [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]]]
    #    distt = [list1[i]+list2[i] for i in range(8)]
    #elif deltaMu == 10:
    #    distt = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]
    #else:
    #    [list1, list2] = [[(1-(deltaMu-10)/10)*x for x in [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 0]], [((deltaMu-10)/10)*x for x in [1/28, 2/28, 3/28, 4/28, 5/28, 6/28, 7/28,0]]]
    ##    distt = [list1[i]+list2[i] for i in range(8)]
    
    return distt
