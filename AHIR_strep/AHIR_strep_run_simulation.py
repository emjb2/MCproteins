# as in th eother simulations this will run the sim for a set number of time steps
from math import floor
from AHIR_strep_dist import AHIR_strep_dist
from AHIR_strep_take_step import AHIR_strep_take_step

k = 1.380649*(10**(-23))

def AHIR_strep_run_simulation(n, time, deltaMu, T):
    positions = list(range(n))
    positions += [x+n for x in positions if (x+n)%2==1]
    add_on = []
    for i in range(floor(n/2)):
        add_on += [x+2*(i+1)*n for x in positions]
    positions += add_on
    positions = positions[:-floor(n/2)-1]
    dist = AHIR_strep_dist()
    # positions list is complete
    for i in range(time):
        positions = AHIR_strep_take_step(n, dist, positions, deltaMu, T)
    return sum(positions)/time
