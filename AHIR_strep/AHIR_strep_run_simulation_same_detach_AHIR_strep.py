# as in the other simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep.AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep.AHIR_strep_take_step_same_detach_strep_AHIR import AHIR_strep_take_step_same_detach_strep_AHIR

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation_same_detach_AHIR_strep(n, time, deltaMu, T, Epb, phi):
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
        if i in positions:
            heights.append(1)
        else:
            heights.append(0)
    # heights list is complete (we start with a fully formed 2D lattice)

    dist = AHIR_strep_dist()
    growth_rate = 0
    for i in range(time):
        #print("Time is: "+str(i))
        ans = AHIR_strep_take_step_same_detach_strep_AHIR(n, dist, positions, strep_only, both, heights, deltaMu, T, Epb, phi)
        heights = ans[0]
        growth_rate += ans[1]
    summ = 0

    for i in both:
        summ += (heights[i]-1)
    for i in strep_only:
        summ += (heights[i]-1)//2
    
    return [summ/time, growth_rate/time, heights]

#AHIR_strep_run_simulation(5, 1, 1, 1)
