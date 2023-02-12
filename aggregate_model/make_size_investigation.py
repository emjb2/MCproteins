#from numba import jit
import monomer_model.take_step
from aggregate_model.run_simulationA import run_simulationA
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from general_functions.line_to_array import line_to_array
import seaborn
from data.data_Ke_et_al import get_me_data
import data.nadarajah_data as nadarajah_data
import time as tme

# @jit
def make_size_investigation(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 2*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    ke_data = get_me_data()
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for i in phi(Epb):
            j += 1
            print(j)
            for x in deltaMu:
                growth_rate[h].append(run_simulationA(n[h], x, i, Epb, T, time)[0])
                j += 1
                print(j)
    colours = ['b', 'm', 'g', 'r']
    for y in range(0,4):
        axis[0].plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], colours[y], label=y+2)
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
        axis[0].set_title("n is small")
        axis[0].set(xlabel='deltaMu in multiples of kT', ylabel='growth rate')
        axis[0].legend()
        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[1].plot(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], colours[y], label=y+2)
        axis[1].set_title("n is medium")
        axis[1].set(xlabel='deltaMu in multiples of kT', ylabel='growth  rate')
        axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[2].plot(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], colours[y], label=y+2)
        axis[2].set_title("n is large")
        axis[2].set(xlabel='deltaMu in multiples of kT', ylabel='growth rate')
        axis[2].legend()
        
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
