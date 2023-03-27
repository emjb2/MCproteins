import matplotlib.pyplot as plt
import numpy as np
import time as tme
from AHIR_strep_pardec.AHIR_strep_run_simulation_pardec import AHIR_strep_run_simulation_pardec
from general_functions.line_to_array import line_to_array
import seaborn
from AHIR_strep_pardec.decoration_dist import decoration_dist
from math import floor
from statistics import mean
from statistics import stdev

def check_different_phi(n, time, deltas):
    dist = [k*(1-0.2) for k in decoration_dist()]+[0.2]
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [k*T, 2*k*T, 3*k*T]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[],[],[]]
    errors = [[],[],[]]
    j=0
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for i in phi(Epb[h]):
            for x in deltaMu:
                temp = []
                for g in range(3):
                    temp.append(AHIR_strep_run_simulation_pardec(n, time, x, T, Epb[h], i, dist)[0])
                growth_rate[h].append(mean(temp))
                errors[h].append(stdev(temp))
                j += 1
                print(j)
    print(errors)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(growth_rate[0]+growth_rate[1]+growth_rate[2])
    intermediate2 = max(growth_rate[0]+growth_rate[1]+growth_rate[2]) 
    errorbarlims = [max(errors[i]) for i in range(len(errors))]  
    for y in range(0,4):
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]
        axis[0].errorbar(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], errors[0][deltas * y:deltas * (y+1)], marker = '.', color=colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
        axis[0].set_title(r'$E_{pb}=1kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[0].set_xlim(0, deltas-1)
        axis[0].set_ylim(ymin, ymax+max(errorbarlims))         
        axis[0].legend()
        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[1].errorbar(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], errors[1][deltas * y:deltas * (y+1)], marker = '.', color=colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[1].set_xlim(0, deltas-1)
        axis[1].set_ylim(ymin, ymax+max(errorbarlims))        
        axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[2].errorbar(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], errors[2][deltas * y:deltas * (y+1)], marker = '.', color=colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[2].set_xlim(0, deltas-1)
        axis[2].set_ylim(ymin, ymax+max(errorbarlims))        
        axis[2].legend()
    
    print(tme.time() - start_time)
    plt.savefig('IKEA check phi, Epb (Boltzmann, ideal strep) 50000.png')
    #plt.show()
    #plt.savefig('make_plotA_final2.pdf')