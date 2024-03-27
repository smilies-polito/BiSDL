if __name__ == "__main__":
    import random
    from snakes.nets import BlackToken
    from examples.pennisi2016.pennisi2016_10 import Pennisi2016
    from petrisim.simulator import *

    random.seed(42)

    test_module = Pennisi2016()
    output_path = os.path.join(".", "results_pennisi2016_10/results")
    n_steps = 1000
    s = Simulator(m=test_module, output_path=output_path, draw_nets=False, firing_prob=0.75)
    s.draw_nets(os.path.join(output_path, "../topology"))

    marking = test_module.get_marking()
    marking['hs_0_net']['MP_molecule'].add([BlackToken()] * 10)
    marking["pennisi2016_net"]["victim"].add(["MP_molecule"] * 10)
    marking['hs_0_net']['TH_molecule'].add([BlackToken()] * 10)
    marking["pennisi2016_net"]["victim"].add(["TH_molecule"] * 10)
    marking['hs_0_net']['B_molecule'].add([BlackToken()] * 10)
    marking["pennisi2016_net"]["victim"].add(["B_molecule"] * 10)
    s.set_initial_marking(marking)

    for i in range(n_steps):
        # results 1
        # if (80 <= i < 120) or (380 <= i < 420):
        #     marking = test_module.get_marking()
        #     marking['hs_0_net']['ANTIGEN_molecule'].add([BlackToken()] * 20)
        #     marking["pennisi2016_net"]["victim"].add(["ANTIGEN_molecule"] * 20)
        #     s.set_initial_marking(marking)

        # results 2
        if (i == 100) or (i == 400):
            marking = test_module.get_marking()
            marking['hs_0_net']['ANTIGEN_molecule'].add([BlackToken()] * 500)
            marking["pennisi2016_net"]["victim"].add(["ANTIGEN_molecule"] * 500)
            s.set_initial_marking(marking)

        s.step()

    s.make_charts(exclude=['gene', 'mrna', 'mediator', 'receptor', 'active', 'mediator', 'activation'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)