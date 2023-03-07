# as in th eother simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep.AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep.AHIR_strep_take_step import AHIR_strep_take_step
from AHIR_strep_pardec.AHIR_strep_pardec_take_step import AHIR_strep_pardec_take_step
from AHIR_strep_pardec.decoration_dist import decoration_dist
from AHIR_strep_pardec.strep_check import strep_check

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation_pardec(n, time, deltaMu, T, Epb, phi):
    track = 0
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

    dist = decoration_dist(deltaMu)
    j = 0
    for i in range(time):  
        j +=1
        #print("count: "+str(j))
        [heights, track] = AHIR_strep_pardec_take_step(n, positions, strep_only, both, heights, deltaMu, T, dist, Epb, phi, track)    
    heights = strep_check(n, positions, strep_only, heights)

    summ = 0

    for i in both:
        summ += (heights[i]-1)
    for i in strep_only:
        summ += (heights[i]-1)//2
    
    
    return [summ/time, track/time, heights]
