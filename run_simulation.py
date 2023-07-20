import os
import sys
from petrisim.simulator import *
from examples.bacterial_consortium.bacterial_consortium import Bacterialconsortium
from examples.rgb.rgb import Rgb_Pattern


experiment = sys.argv[1]
n_steps = int(sys.argv[2])

if experiment == "bacterial_consortium":
    test_module = Bacterialconsortium()

if experiment == "rgb":
    test_module = Rgb_Pattern()

output_path = os.path.join(".","examples", experiment, "results")
#n_steps = 100
s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
s.draw_nets(os.path.join(output_path, "../topology"))

for _ in range(n_steps):
    s.step()

s.make_charts(exclude=['gene', 'mrna'])
with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
    print(test_module, file=fp)