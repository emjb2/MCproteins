from math import e
from numpy import roots 

k = 1.380649*(10**(-23))

def calc_mol_dist(deltaMu, T):
    concentration = e ** (deltaMu/(k*T))*30
    print(concentration)
    #solns = roots([2700000000000, 0, 30000, 1, -0.005])
    #poss = []
    #for x in solns:
    #    if not isinstance(x, complex):
    #        if x>0:
    #            poss.append(x)
    poss = [0.005]            
    dist = [poss[0], 30000*(poss[0] ** 2), 3000 * (poss[0] ** 4)]
    return [x/sum(dist) for x in dist]
