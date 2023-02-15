#from numba import jit
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time as tme
from AHIR_strep.AHIR_strep_run_simulation import AHIR_strep_run_simulation

# @jit
def make_plot_AHIR_strep(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 2*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = []
    j=0
    for x in deltaMu:
        growth_rate.append(AHIR_strep_run_simulation(n, time, x, T)/2)
        j += 1
        print(j)
    print(growth_rate)
    print(range(0,deltas))
    #for y in range(0,1):
    plt.plot(range(0,deltas), growth_rate)
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
    plt.title("AHIR and strep: run 1")
    plt.xlabel('deltaMu in multiples of kT'), 
    plt.ylabel('growth rate')
    plt.legend()
        #data_check = data.get_me_data()
        #axis[0].plot(data_check[0],data_check[1], 'yx')
        #axis[1].plot(data_check[0],data_check[1], 'yx')
        #axis[2].plot(data_check[0],data_check[1], 'yx')
    print(tme.time() - start_time)
    #plt.savefig('Ke_comparison_2_detachment_fixed_scaled.png')
    #plt.savefig('Ke_comparison_2_detachment_fixed_scaled.pdf')
    plt.show()
   # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # dummy2=run_simulation(30, deltaMu[4], phi[2], Epb, T, time)
   # print(line_to_array(dummy2[1],30))
   # seaborn.heatmap(line_to_array(dummy2[1],30))
   # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
