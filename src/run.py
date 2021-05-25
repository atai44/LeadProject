from generate_mesh import generate
from makeplot import makeplot
import numpy as np

pHvec, Vvec, mesh = generate(1.5e-4)
print(mesh)
makeplot(pHvec, Vvec, mesh)