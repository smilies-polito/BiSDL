import os
import random
import sys
import shutil
import stat
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

if os.path.isdir(output_path):
    shutil.rmtree(output_path)

# use this line, where the mode parameter is set to 'exploration' to explore simulation results more freely
#s = Simulator(m=test_module, output_path=output_path, draw_nets=False, mode='exploration')

# use this line, where the mode parameter is set to 'paperFigures' to generate the figures in Giannantoni et al., 2023
s = Simulator(m=test_module, output_path=output_path, draw_nets=False, mode='paperFigures')

s.draw_nets(os.path.join(output_path, "../topology"))

if example == "bacterial_consortium":
    if condition == "noLacI":
        for _ in range(n_steps):
            marking = test_module.get_marking()

            if _ % 3 == 0:
                marking['AHL_production_0_net']['SAM_molecule'].add([BlackToken()] * random.randint(0,5))

            s.set_initial_marking(marking)
            s.step()

    elif condition == "lowLacI":
        for _ in range(n_steps):
            marking = test_module.get_marking()
            if _ % 3 == 0:
                marking['AHL_production_0_net']['SAM_molecule'].add([BlackToken()] * random.randint(0, 3))

            if _ % 10 == 0:
                marking['AHL_production_0_net']['LacI_protein'].add([BlackToken()] * random.randint(0,3))
            s.set_initial_marking(marking)
            s.step()

    elif condition == "highLacI":
        for _ in range(n_steps):
            marking = test_module.get_marking()
            if _ % 3 == 0:
                marking['AHL_production_0_net']['SAM_molecule'].add([BlackToken()] * random.randint(0, 5))

            if _ % 3 == 0:
                marking['AHL_production_0_net']['LacI_protein'].add([BlackToken()] * random.randint(0,10))
            s.set_initial_marking(marking)
            s.step()

    else:
        print("Insert valid condition among the following: noLacI, lowLacI, highLacI")

elif example == "rgb":
    if condition == "rgb":
        for _ in range(n_steps):
            s.step()

    s.make_spatial_charts()


s.make_charts()