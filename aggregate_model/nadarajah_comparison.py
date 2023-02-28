from aggregate_model.run_simulationA import run_simulationA
from data.more_nadarajah_data import more_nadarajah_data
from matplotlib import pyplot as plt

def nadarajah_comparison(n, time, deltas):
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = 3*k*T
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = []
    phi = 5*Epb
    data = more_nadarajah_data()
    def phi(Epb):
        return 5*Epb
    data_format = [data[0][:12], data[1][:12]]
    max_y = max(data_format[1])
    max_x = max(data_format[0])
    min_x = min(data_format[0])
    j=0
    for x in deltaMu:
        growth_rate.append((run_simulationA(n, x, phi(Epb), Epb, T, time)[0]))
    max_growth = max(growth_rate)
    for i in range(len(growth_rate)):
        j += 1
        print(j)
        growth_rate[i] = growth_rate[i]/max_growth*max_y
    x_axis = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(13):
        x_axis[i] = i/12*(max_x-min_x)
        x_axis[i] += min_x
    plt.plot(data_format[0], data_format[1], marker='.', color = 'r', label = "Nadarajah data: 50mg/ml lysozyme")
    plt.plot(x_axis, growth_rate, marker='.', color = 'b', label = r"Simulation: $E_{pb}=3kT$ and $\phi=5$")
    plt.xlabel('Supersaturation')
    plt.ylabel('Growth Rate')
    plt.title("A comparison of the simulation with the results of Nadarajah et al")
    plt.legend()
    plt.show()
    
