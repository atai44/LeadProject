from generate_mesh import generate
from makeplot import makeplot
import numpy as np

pH_, V_, mesh = generate(1.5e-4)
print(mesh)
makeplot(pH_, V_, mesh)