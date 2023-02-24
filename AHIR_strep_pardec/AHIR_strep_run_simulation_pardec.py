# as in th eother simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep.AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep.AHIR_strep_take_step import AHIR_strep_take_step
from AHIR_strep_pardec.AHIR_strep_pardec_take_step import AHIR_strep_pardec_take_step
from AHIR_strep_pardec.decoration_dist import decoration_dist
from AHIR_strep_pardec.strep_check import strep_check

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation_pardec(n, time, deltaMu, T):
    positions = list(range(n**2))
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            positions.remove((2*i+1)*n + (2*j+1))

    strep_only = positions.copy()
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            strep_only.remove(2*i*n + 2*j)

    both = [x for x in positions if not x in strep_only]
    # heights list is complete (we start with a fully formed 2D lattice)

    heights = []
    for i in range(n**2):
        if i in positions:
            heights.append(1)
        else:
            heights.append(0)         

    dist = decoration_dist()
    j = 0
    for i in range(time):  
        j +=1
        #print("count: "+str(j))
        heights = AHIR_strep_pardec_take_step(n, positions, strep_only, both, heights, deltaMu, T, dist)    
    heights = strep_check(n, positions, strep_only, heights)

    return [sum(heights)/time, heights]

#AHIR_strep_run_simulation(5, 1, 1, 1)
