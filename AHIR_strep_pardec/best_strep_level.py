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

def best_strep_level(n, time):
    dist = decoration_dist()
    dists = [[k*(1-i) for k in dist]+[i] for i in [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45]]
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 2*k*T
    phi = 3*k*T
    deltaMu = 10*k*T
    growth_rate = []
    errors = []
    j=0
    colours = ['mediumvioletred']
    for k in range(10):
            temp=[]
            for i in range(5):
                temp.append((AHIR_strep_run_simulation_pardec(n, time, deltaMu, T, Epb, phi, dists[k]))[0])
            growth_rate.append(mean(temp))
            errors.append(stdev(temp))
            j += 1
            print(j)
    #for y in range(0,1):
    plt.errorbar([0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45], growth_rate, errors, marker='.', color=colours[0])
    #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
    
    limits = min(growth_rate)
    limits2 = max(growth_rate)
    errorlims = max(errors)

    plt.title("AHIR streptavidin: partially decorated by Boltzmann dist.")
    plt.xlabel(r'relative concentration of streptavidin'), 
    plt.ylabel('Growth Rate')
    plt.xlim(0,0.45)
    plt.ylim(0, limits2+errorlims)
    plt.legend()
    print(tme.time() - start_time)
    plt.savefig('IKEA strep conc investigation (Boltzmann with varying strep) 100000.png')
    #plt.show()
    #plt.savefig('Ke_comparison_2_detachment_fixed_scaled.pdf')
   # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # print(line_to_array(dummy2[1],30))
   #    # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
