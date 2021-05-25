from generate_mesh import generate
from makeplot import makeplot
import numpy as np

mesh = generate(1.5e-4)
print(mesh)
present = np.unique(mesh)
print("Species Present: ", present)
makeplot(mesh)