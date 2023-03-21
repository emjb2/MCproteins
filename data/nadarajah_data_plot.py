import more_nadarajah_data
from matplotlib import pyplot as plt

def nadarajah_data_plot():
    data2 = more_nadarajah_data.more_nadarajah_data()
    growth_rates = [[], [], []]
    supersaturation = [[], [], []]
    for j in range(12):
        supersaturation[0].append(data2[0][j])
        growth_rates[0].append(data2[1][j])
    for i in range(1,2):
        for j in range(9):
            supersaturation[i].append(data2[0][12*i+j])
            growth_rates[i].append(data2[1][12*i+j])
    for j in range(9):
            supersaturation[2].append(data2[0][21+j])
            growth_rates[2].append(data2[1][21+j])        
    
    colours = ['royalblue', 'tomato', 'gold']
    for i in range(3):
        plt.plot(supersaturation[i], growth_rates[i], color = colours[i], marker = '.', label = str(50-i*10)+'mg/ml lysozyme')
    plt.title("Nadarajah et al: Lysozyme Crystal Growth Rates")
    plt.xlabel('Supersaturation'), 
    plt.ylabel('Growth Rate')
    plt.xlim(min(data2[0]), max(data2[0]))
    plt.ylim(min(data2[1]), max(data2[1])+(max(data2[1])-min(data2[1]))/25)
    plt.legend()
    plt.show()

nadarajah_data_plot()
