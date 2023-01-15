import take_step
import run_simulation
import matplotlib.pyplot as plt


def make_plot(n, time):
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    # try doing Epb is 3 but capping the bonds?
    Epb = 3*k*T
    deltaMu = [x*k*T for x in range(0, 13)]
    growth_rate = []
    phi = [2*k*T, 3*k*T, 4*k*T, 5*k*T]
    for i in phi:
        for x in deltaMu:
            growth_rate.append(run_simulation.run_simulation(n, x, i, Epb, T, time))
    for y in range(0,4):
        plt.plot(deltaMu, growth_rate[13 * y:13 * (y+1)], label=y+2)
    plt.xlabel('deltaMu in multiples of kT')
    plt.ylabel('growth rate')
    plt.title('Monomers only: phi/kT is the legend, Epb/kT is 1')
    plt.legend()
    plt.show()
