import os
import sys
from petrisim.simulator import *
from snakes.nets import *
from examples.bacterial_consortium.bacterial_consortium import Bacterialconsortium
from examples.rgb.rgb import Rgb


example = sys.argv[1]
condition = sys.argv[2]
n_steps = int(sys.argv[3])

if example == "bacterial_consortium":
    test_module = Bacterialconsortium()

if example == "rgb":
    test_module = Rgb()

output_path = os.path.join(".", "examples", example, "results", condition)
s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
s.draw_nets(os.path.join(output_path, "../topology"))

for _ in range(n_steps):

    marking = test_module.get_marking()
    if _ == 50:
        marking['controller_0_net']['Lac1_protein'].add([BlackToken()]*20)
        s.set_initial_marking(marking)

    s.step()

s.make_charts()
with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
    print(test_module, file=fp)