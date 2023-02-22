# as in th eother simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep.AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep.AHIR_strep_take_step import AHIR_strep_take_step
from AHIR_strep_pardec.AHIR_strep_pardec_take_step import AHIR_strep_pardec_take_step
from AHIR_strep_pardec.decoration_dist import decoration_dist

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation_pardec(n, time, deltaMu, T):
    positions = list(range(n))
    positions += [x+n for x in positions if (x+n)%2==1]
    add_on = []
    for i in range(floor(n/2)):
        add_on += [x+2*(i+1)*n for x in positions]
    positions += add_on
    # positions list is complete
    heights = []
    for i in range(n * (n+1)):
        if i in positions:
            heights.append(1)
        else:
            heights.append(0)
    # heights list is complete (we start with a fully formed 2D lattice)
    
    dist = decoration_dist()

    for i in range(time):
        heights = AHIR_strep_pardec_take_step(n, positions, heights, deltaMu, T, dist)    
        
    return [sum(heights)/time, heights]

#AHIR_strep_run_simulation(5, 1, 1, 1)
