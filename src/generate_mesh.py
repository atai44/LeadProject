import numpy
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

def generate(conc = 1.5e-8, carbonates = False):
    print("calculating stable species")
    print("Pb concentration: ", conc)