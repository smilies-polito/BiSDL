if __name__ == "__main__":
    from snakes.nets import BlackToken
    from examples.gregory2008.gregory2008 import Gregory2008
    from petrisim.simulator import *

    test_module = Gregory2008()
    output_path = os.path.join(".", "results_gregory2008/results")
    n_steps = 300
    s = Simulator(m=test_module, output_path=output_path, draw_nets=False, firing_prob=0.75)
    s.draw_nets(os.path.join(output_path, "../topology"))

    marking = test_module.get_marking()
    marking['donor_0_net']['R_plasmid_molecule'].add([BlackToken()] * 1)
    marking['gregory2008_net']['donor'].add(["R_plasmid_molecule"] * 1)
    s.set_initial_marking(marking)

    for i in range(n_steps):
        if i == 50:
            marking = test_module.get_marking()
            marking['donor_0_net']['pilus_molecule'].add([BlackToken()] * 10)
            marking['gregory2008_net']['donor'].add(["pilus_molecule"] * 10)
            s.set_initial_marking(marking)

        s.step()

    s.make_charts(exclude=['gene', 'mrna', 'mediator', 'receptor', 'active', 'mediator', 'activation', 'mod'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)
