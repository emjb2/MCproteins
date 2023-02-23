# as in the other simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep.AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep.AHIR_strep_take_step import AHIR_strep_take_step

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation(n, time, deltaMu, T):
    positions = list(range(n**2))
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            positions.remove((2*i+1)*n + (2*j+1))

    strep_only = positions.copy()
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            strep_only.remove(2*i*n + 2*j)

    both = [x for x in positions if not x in strep_only]

    heights = []
    for i in range(n**2):
        if i in postions:
            heights.append(1)
        else:
            heights.append(0)
    # heights list is complete (we start with a fully formed 2D lattice)

    dist = AHIR_strep_dist()

    for i in range(time):
        heights = AHIR_strep_take_step(n, dist, positions, strep_only, both, heights, deltaMu, T)
    
    return sum(heights)/time

#AHIR_strep_run_simulation(5, 1, 1, 1)
