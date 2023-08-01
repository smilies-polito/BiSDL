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

elif example == "rgb":
    test_module = Rgb()
else:
    print("Insert valid example among the following: bacterial_consortium, rgb")

output_path = os.path.join(".", "examples", example, "results", condition)
s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
s.draw_nets(os.path.join(output_path, "../topology"))

if example == "bacterial_consortium":
    if condition == "noLacI":
        for _ in range(n_steps):
            s.step()

    elif condition == "lowLacI":
        for _ in range(n_steps):
            if _ % 5 == 0:
                marking = test_module.get_marking()
                marking['controller_0_net']['Lac1_protein'].add([BlackToken()] * 1)
                s.step(init_marking=marking)

    elif condition == "highLacI":
        for _ in range(n_steps):
            if _ % 2 == 0:
                marking = test_module.get_marking()
                marking['controller_0_net']['Lac1_protein'].add([BlackToken()] * 1)
                s.step(init_marking=marking)


    else:
        print("Insert valid condition among the following: noLacI, lowLacI, highLacI")

elif example == "rgb":
    if condition == "rgb":
        for _ in range(n_steps):
            s.step()

s.make_charts()
with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
    print(test_module, file=fp)