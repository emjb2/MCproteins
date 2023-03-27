from numba import jit
import monomer_model.take_step
from monomer_model.run_simulation import run_simulation
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from mpl_toolkits import mplot3d
from general_functions.line_to_array import line_to_array
import seaborn
from data.data_Ke_et_al import get_me_data
import data.nadarajah_data as nadarajah_data
import time as tme

# @jit
def calibrate_time_steps(n, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 2*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[],[],[],[],[],[]]
    errorbars = [[],[],[],[],[],[]]
    phi = 3*Epb
    j=0
    #times=[10, 10, 10, 10, 10, 10]
    times = [1000, 10000, 50000, 100000, 200000, 500000]
    for i in range(0,6):
        for x in deltaMu:
            temp_data = []
            for g in range(2):
                temp_data.append(run_simulation(30, x, phi, Epb, T, times[i])[0])
            growth_rate[i].append(np.mean(temp_data))
            errorbars[i].append(np.std(temp_data))
            j += 1
            print(j)
    intermediate = [min(growth_rate[i]) for i in range(len(growth_rate))]
    intermediate2 = [max(growth_rate[i]) for i in range(len(growth_rate))]
    errorbarlims = [max(errorbars[i]) for i in range(len(errorbars))]
    [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, max(intermediate2)]
    colours = ['midnightblue', 'lightskyblue', 'forestgreen', 'gold', 'mediumvioletred', 'black']
    for y in range(0,6):
        plt.errorbar(range(0,deltas), growth_rate[y], yerr = errorbars[y], marker='.', label="number of moves = "+str(times[y]), color = colours[y])
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
    plt.title(r'$E_{pb}$=2$kT$, $\phi = 3$')
    plt.xlabel(r'$\Delta$$\mu$ in multiples of $kT$')
    plt.ylabel('Growth Rate')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax + max(errorbarlims))
    plt.legend()
    
    plt.savefig('IKEA time step calibration.png')
   # plt.savefig('calibrate_time_steps2.pdf')
    print(tme.time() - start_time)
   # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # dummy2=run_simulation(30, deltaMu[4], phi[2], Epb, T, time)
   # print(line_to_array(dummy2[1],30))
   # seaborn.heatmap(line_to_array(dummy2[1],30))
   # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
