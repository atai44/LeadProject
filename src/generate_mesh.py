import numpy as np
import math

#constants
R=.008314 #kJ/mol-K
T=298.15 #K
F=96.485 #kJ/V-g

#Gibbs Free Energy from PBEsol, kJ/mol
GPb = 0
GPbO = -182.179911180077
GPbO2 = -225.05892068112
GPb2O3 = -409.660823950954
GPb3O4 = -606.321927722997
PbCO3 = -636.8927823795264
hc = -1680.6559541150234
pbphos = -2265.1179660491134

#experimental Gibbs Free Energy values for ions, kJ/mol
GPb4 = 302.50074
GPb2 = -23.9743
GHPbO2 = -338.904
GPbO3 = -277.56656
GPbO4 = -282.08946
GPbH2 = 290.788
OH = -157.33514

#set up pH range (consider doing this in input)
pHstart = -2
pHend = 16
dpH = 0.0045
pHvec = np.arange(pHstart, pHend, dpH)

#set up potential range(consider doing this in input)
Vstart = 4
Vend = -2
dV = -0.0015
Vvec = np.arange(Vstart, Vend, dV)

#set up grid
pH_, V_ = np.meshgrid(pHvec, Vvec)
Z = np.empty(np.shape(pH_), dtype = object)

def generate(conc = 1.5e-8, carbonates = False):
    print("calculating stable species")
    print("Pb concentration: ", conc)
    i = 0
    j = 0
    for pH in pHvec:
        i = 0
        for V in Vvec:
            lowpot = 10000000
            stable = "check"
            ue = -F * V
            uH = -R*T*math.log(10)*pH
            uPb = GPb
            uH2O = -237.18
            
            #Pb
            lowpot = uPb
            stable = "Pb"
            
            #Pb2+
            pot = GPb2 + R*T*math.log(conc)
            urxn = pot + 2*ue - uPb
            #print("Pb2+: ", urxn)
            #pb2plus[j] == urxn
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "Pb++"
                
            #PbO
            urxn = GPbO + 2*ue + 2*uH - uPb - uH2O
            #print("PbO: ", urxn)
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "PbO"
                
            #PbO2
            urxn = GPbO2 + 4*ue + 4*uH - uPb - 2*uH2O
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "PbO2"
                
            #Pb3O4
            urxn = (GPb3O4 + 8*ue + 8*uH - 3*uPb -4*uH2O)/3
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "Pb3O4"
                
            #Pb4+
            pot = GPb4 + R*T*math.log(conc)
            urxn = pot + 4*ue - uPb
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "Pb++++"
                
            #HPbO2
            pot = GHPbO2 + R*T*math.log(conc)
            urxn = pot + 3*uH + 2*ue - 2*uH2O - uPb
            #print("HPbO2: ", urxn)
            if (urxn <= lowpot) : 
                lowpot = urxn
                stable = "HPbO2-"
                
            #PbO3--
            pot = GPbO3 + R*T*math.log(conc)
            urxn = pot + 6*uH + 4*ue - 3*uH2O - uPb
            #print("PbO3: ", urxn)
            if (urxn <= lowpot) :
                lowpot = urxn
                stable = "PbO3--"
                
            Z[i,j] = stable
            i+=1
        j+=1
    return pH_, V_, Z