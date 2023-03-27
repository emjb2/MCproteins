import matplotlib.pyplot as plt
import numpy as np
import time as tme
from AHIR_strep_pardec.AHIR_strep_run_simulation_pardec import AHIR_strep_run_simulation_pardec
from general_functions.line_to_array import line_to_array
import seaborn
from AHIR_strep_pardec.decoration_dist import decoration_dist
from math import floor
from statistics import mean, stdev

def run_a_bunch_all_fuldec(n, time, deltas):
    dist = [0, 0, 0, 0, 0, 0, 1]
    dists = [[k/(1+i/2) for k in dist]+[i/(2+i)] for i in range(10)]
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 2*k*T
    phi = 3*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[],[],[],[],[],[],[],[],[],[]]
    errors = [[],[],[],[],[],[],[],[],[],[]]
    j=0
    colours = ['midnightblue', 'lightskyblue', 'aqua', 'forestgreen', 'gold', 'yellow', 'deeppink', 'mediumvioletred', 'dimgrey', 'black']
    for k in range(10):
        for x in deltaMu:
            temp = []
            for i in range(5):
                temp.append((AHIR_strep_run_simulation_pardec(n, time, x, T, Epb, phi, dists[k]))[0])
            growth_rate[k].append(mean(temp))
            errors[k].append(stdev(temp))
            j += 1
            print(j)
    print(growth_rate)
    print(range(0,deltas))
    #for y in range(0,1):
    for k in range(10):
        plt.errorbar(range(0,deltas), growth_rate[k], errors[k], marker='.', color=colours[k], label="strep. conc. "+str(floor(dists[k][-1]*100)/100))
    
    limits = [min(growth_rate[k]) for k in range(10)]
    limits2 = [max(growth_rate[k]) for k in range(10)]
    errorlims = [max(errors[k]) for k in range(10)]


    plt.title("AHIR streptavidin: fully decorated with unattached streptavidin")
    plt.xlabel(r'$\Delta \mu$ in multiples of kT'), 
    plt.ylabel('Growth Rate')
    plt.xlim(0,deltas-1)
    plt.ylim(0, max(limits2)+max(errorlims))
    plt.legend()
    print(tme.time() - start_time)
    # plt.show()
    plt.savefig('IKEA AHIR strep pardec (all full dec, vary strep) 200000.png')
    #plt.savefig('Ke_comparison_2_detachment_fixed_scaled.pdf')
   # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # print(line_to_array(dummy2[1],30))
   #    # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
