from AHIR_strep_twinned.AHIR_strep_twinned_take_step import AHIR_strep_twinned_take_step


k = 1.380649*(10**(-23))

def AHIR_strep_twinned_run_simulation(n, time, deltaMu, T):
    positions = list(range(n**2))
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            positions.remove((2*i+1)*n + (2*j+1))

    strep_only = positions.copy()
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            strep_only.remove(2*i*n + 2*j)

    both = [x for x in positions if not x in strep_only]
    # now make heights, we don't hav ea fully formed lattice this time
    # We just start with one crysalin (type 1) AHIR and one twinned (type 2) AHIR.
    # We place them as far as possible apart and see what happens
    heights = [[0,0]] * (n**2)
    split = [x for x in [n//4, n//4 + 1] if x%2 == 0][0]
    ahir_one_loc = (n+1)*split
    ahir_two_loc = (n+1)*3*split
    heights[ahir_one_loc] = [1,1]
    heights[ahir_two_loc] = [2,1]

    for i in range(time):
        heights = AHIR_strep_twinned_take_step(n, positions, strep_only, both, heights, deltaMu, T)
    
    return [sum(heights)/time, heights]



