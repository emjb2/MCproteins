#from numba import jit
import matplotlib.pyplot as plt
from AHIR_strep.AHIR_strep_run_simulation_same_detach_AHIR_strep import AHIR_strep_run_simulation_same_detach_AHIR_strep
from statistics import mean, stdev

# @jit
def make_plot_final_AHIR_strep_same_detach(n, time, deltas):
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    errors = [[],[],[]]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for g in range(4):
            for x in deltaMu:
                temp=[]
                for k in range(5):
                    temp = temp + [AHIR_strep_run_simulation_same_detach_AHIR_strep(n, time, x, T, Epb[h], phi(Epb[h])[g])[0]]
                growth_rate[h].append(mean(temp))
                errors[h].append(stdev(temp))
                j += 1
                print(j)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(growth_rate[0]+growth_rate[1]+growth_rate[2])
    intermediate2 = max(growth_rate[0]+growth_rate[1]+growth_rate[2])
    for y in range(0,4):
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]
        axis[0].errorbar(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], errors[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[0].set_title(r'$E_{pb}=1kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[0].set_xlim(xmin, xmax)
        axis[0].set_ylim(ymin, ymax*1.05)
        axis[0].legend()
        axis[1].errorbar(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], errors[1][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
        axis[1].set_xlim(xmin, xmax)
        axis[1].set_ylim(ymin, ymax*1.05)   
        axis[1].legend()
        axis[2].errorbar(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], errors[2][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[2].set_xlim(xmin, xmax)
        axis[2].set_ylim(ymin, ymax*1.05)   
        axis[2].legend()
    
    #plt.savefig('test.png')
    plt.show()
