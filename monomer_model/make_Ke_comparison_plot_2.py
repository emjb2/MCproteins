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

def make_Ke_comparison_plot_2(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 3*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = []
    phi = 5*Epb
    j=0
    ke_data = get_me_data()
    for x in deltaMu:
        print(x/(k*T))
        growth_rate.append(run_simulation(n, x, phi, Epb, T, time)[0])
    intermediate = min(growth_rate)
    intermediate2 = max(growth_rate+ke_data[2][0:13])
    [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]
    colours = ['midnightblue', 'lightskyblue', 'forestgreen', 'gold', 'mediumvioletred', 'black']

    plt.plot(range(0,deltas), growth_rate, marker='.', color=colours[1], label="Simulation")
    plt.plot(range(0,13), ke_data[2][0:13], marker='.', color=colours[4], label="Ke et al's Simulation")
    plt.title("$E_{pb}$ = $3kT$, $\phi$ = $5$")
    plt.xlabel('$\Delta$$\mu$ in multiples of $kT$')
    plt.ylabel('Growth Rate')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, 1.05*ymax)
    plt.legend()
    print(tme.time() - start_time)
    plt.savefig('IKEA Ke_comparison_2    2.png')
    #plt.savefig('Ke_comparison_2_detachment_fixed_scaled.pdf')
   # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # dummy2=run_simulation(30, deltaMu[4], phi[2], Epb, T, time)
   # print(line_to_array(dummy2[1],30))
   # seaborn.heatmap(line_to_array(dummy2[1],30))
   # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
