from aggregate_model.run_simulationA import run_simulationA
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from general_functions.line_to_array import line_to_array
import seaborn
from data.data_Ke_et_al import get_me_data
import data.nadarajah_data as nadarajah_data
import time as tme
from general_functions.monomer_dimer_tetramer import plot_monomer_dimer_tetramer
from matplotlib import colors

def new_make_plot(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[]]
    def phi(Epb):
        #return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
        return [2*Epb]
    j=0
    #figure, axis = plt.subplots(1, 3, figsize=(15,7))
    #figure.tight_layout(pad=5.0)
    for h in range(1):
        for i in phi(Epb[h]):
            for x in deltaMu:
                growth_rate[h].append(run_simulationA(n, x, i, Epb[h], T, time)[2])
                j += 1
                print(j)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(growth_rate)
    intermediate2 = max(growth_rate[0])    
    for y in range(0,1):
    #    axis[0].plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
    #    axis[0].plot(range(13), trial_points)
    #    axis[0].set_title(r'$E_{pb}=1kT$')
    #    axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
    #    axis[0].set_ylim([0, 0.6])
    #    axis[0].legend()

        plt.plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        plt.title(r'Durbin et al Growth Rate example: $E_{pb}=kT$')
        plt.xlabel(r'$\Delta$$\mu$ in multiples of $kT$')
        plt.ylabel('Growth Rate')
        plt.ylim(min(growth_rate[0]), max(growth_rate[0])*1.05)
        plt.xlim(0,deltas-1)
        plt.legend()


        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
    #    axis[1].plot(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
    #    axis[1].set_title(r'$E_{pb}=2kT$')
    #    axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
    #    axis[1].set_ylim([0, 0.6])
    #    axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
    #    axis[2].plot(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
    #    axis[2].set_title(r'$E_{pb}=3kT$')
    #    axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
    #    axis[2].set_ylim([0, 0.6])
    #    axis[2].legend()
    
    print(tme.time() - start_time)
    #plt.savefig('IKEA aggregate with line.png')
    #plt.savefig('make_plotA_final2.pdf')
    plt.show()
