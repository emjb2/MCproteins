from data.monomer_dimer_tetramer import monomer_dimer_tetramer
from matplotlib import pyplot as plt

def plot_monomer_dimer_tetramer():
    data = monomer_dimer_tetramer()
    label = ["monomer", "dimer", "tetramer"]
    color =['r', 'g', 'b']
    #for i in range(3):
    #    plt.plot(data[0][i*13:(i+1)*13], data[1][i*13:(i+1)*13], color = color[i], marker = '.', label = label[i])
    #plt.title("Ke et al: Concentration of monomers dimers and tetramers in solution")
    #plt.xlabel("Supersaturation")
    #plt.ylabel("Relative Concentration")
    #plt.legend()
    #plt.show()
    monomers = data[1][0:13]
    dimers = data[1][13:26]
    tetramers = data[1][26:39]
    ratio = []
    for i in range(13):
        ratio.append(monomers[i]/(dimers[i]+tetramers[i]))
    #plt.plot(range(11), ratio[2:])
    #plt.show()
    slope = (ratio[-1]-ratio[8])/5
    return slope

