import os
import sys
from petrisim.simulator import *
from snakes.nets import *
from examples.bacterial_consortium.bacterial_consortium import Bacterialconsortium
from examples.atest.atest import Atest
from examples.rgb.rgb import Rgb


experiment = sys.argv[1]
n_steps = int(sys.argv[2])

if experiment == "bacterial_consortium":
    test_module = Bacterialconsortium()

if experiment == "rgb":
    test_module = Rgb()

if experiment == "atest":
    test_module = Atest()

output_path = os.path.join(".", "examples", experiment, "results")
#n_steps = 100
s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
s.draw_nets(os.path.join(output_path, "../topology"))

#print(marking)
#s.set_initial_marking(marking)
#print(marking)

#marking = test_module.get_marking()
#marking['controller_0_net']['SAM_protein'].add([BlackToken()] * 1)
#s.set_initial_marking(marking)

for _ in range(n_steps):

    #if _%2==0:
        #marking = test_module.get_marking()
        #marking['controller_0_net']['Lac1_protein'].add([BlackToken()]*1)
        #s.set_initial_marking(marking)

    s.step()



s.make_charts()#exclude=['gene', 'mrna'])
with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
    print(test_module, file=fp)