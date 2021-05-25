import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

colordict = {
    "Pb": "#85807b",
    "Pb++": "#db653d",
    "PbO": "#e04a16",
    "PbO2": "#3ec760",
    "Pb3O4": "#2a8744",
    "Pb++++": "#c92840",
    "HPbO2-": "#db7d42", 
    "PbO3--": "#bf3939"
    }

def makeplot(pH_, V_, mesh):
    
    print("making plot")
    
    #identify unique species, turn grid into numbers and make colormap
    nmesh = np.empty(np.shape(mesh), dtype=float)
    present = pd.unique(mesh.flatten())
    print("Species Present: ", present)
    colors_ = []
    for i in range(len(present)):
        nmesh[mesh == present[i]] = i
        colors_.append(colordict[present[i]])
    print(nmesh)
    print(colors_)
    levels = np.arange(len(present)+1)
    levels = levels - .5
    print(levels)
    
    fig, ax = plt.subplots()
    CS = ax.contourf(pH_, V_, nmesh, levels, colors = colors_)
    ax.contour(pH_, V_, nmesh, colors= 'k', linewidths=0.25, antialiased=True)
    plt.savefig('plot', dpi = 300)
    
    