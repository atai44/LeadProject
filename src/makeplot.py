import matplotlib.pyplot as plt
import numpy as np

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

def makeplot(pHvec, Vvec, mesh):
    present = np.unique(mesh)
    print("Species Present: ", present)
    print("making plot")