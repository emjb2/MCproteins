from aggregate_model.run_simulationA import run_simulationA
import matplotlib.pyplot as plt
from general_functions.line_to_array import line_to_array
from general_functions.monomer_dimer_tetramer import plot_monomer_dimer_tetramer

def make_plotA_final(n, time, deltas):
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    trial_slope = plot_monomer_dimer_tetramer()
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    #figure, axis = plt.subplots(1, 3, figsize=(15,7))
    #figure.tight_layout(pad=5.0)
    trial_end=[]
    for h in range(1):
        for i in phi(Epb[h]):
            for x in deltaMu:
                growth_rate[h].append(run_simulationA(n, x, i, Epb[h], T, time)[0])
                if x == 12*k*T and h == 0:
                    trial_end.append(growth_rate[h][-1])
                j += 1
                print(j)
    trial_mean = sum(trial_end)/len(trial_end)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(growth_rate)
    intermediate2 = max(growth_rate[0])    
    trial_points = []
    for i in range(13):
        trial_points.append(trial_slope*i+(trial_mean-12*trial_slope))
    for y in range(0,4):

        plt.plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        plt.plot(range(13), trial_points, color=colours[0])
        plt.title(r'$E_{pb}=1kT$')
        plt.xlabel(r'$\Delta$$\mu$ in multiples of $kT$')
        plt.ylabel('Growth Rate')
        plt.ylim([0, 0.6])
        plt.xlim(0,deltas-1)
        plt.legend()
    
    #plt.savefig('IKEA aggregate with line.png')
    plt.show()
