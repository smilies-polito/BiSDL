if __name__ == "__main__":
    from snakes.nets import BlackToken
    from examples.mozhayskiy2011.mozhayskiy2011 import Mozhayskiy
    from petrisim.simulator import *
    import random

    random.seed(42)

    test_module = Mozhayskiy()
    output_path = os.path.join(".", "results_mozhayskiy2011/results")
    n_steps = 500
    s = Simulator(m=test_module, output_path=output_path, draw_nets=False, firing_prob=0.75)
    s.draw_nets(os.path.join(output_path, "../topology_start"))

    marking = test_module.get_marking()
    marking['donor_0_net']['T0_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T1_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T2_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T3_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T4_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T5_plasmid_molecule'].add([BlackToken()] * 1)
    marking['donor_0_net']['T6_plasmid_molecule'].add([BlackToken()] * 1)
    marking['mozhayskiy_net']['donor'].add(['T0_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T1_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T2_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T3_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T4_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T5_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['donor'].add(['T6_plasmid_molecule'] * 1)
    marking['recipient_0_net']['T0_plasmid_molecule'].add([BlackToken()] * 1)
    marking['recipient_0_net']['T1_plasmid_molecule'].add([BlackToken()] * 1)
    marking['recipient_0_net']['T2_plasmid_molecule'].add([BlackToken()] * 1)
    marking['recipient_0_net']['T3_plasmid_molecule'].add([BlackToken()] * 1)
    marking['mozhayskiy_net']['recipient'].add(['T0_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['recipient'].add(['T1_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['recipient'].add(['T2_plasmid_molecule'] * 1)
    marking['mozhayskiy_net']['recipient'].add(['T3_plasmid_molecule'] * 1)

    s.set_initial_marking(marking)

    for i in range(n_steps):
        if i == 100 or i == 300:
            marking = test_module.get_marking()
            marking['mozhayskiy_net']['donor'].add(['pilus_molecule'] * 20)
            marking['donor_0_net']['pilus_molecule'].add([BlackToken()] * 20)
            s.set_initial_marking(marking)
        # S1 signal
        if random.random() < 0.8:
            S1_amount = random.randint(10, 20)
            marking['mozhayskiy_net']['donor'].add(['S1_molecule'] * S1_amount)
            marking['donor_0_net']['S1_molecule'].add([BlackToken()] * S1_amount)
            marking['mozhayskiy_net']['recipient'].add(['S1_molecule'] * S1_amount)
            marking['recipient_0_net']['S1_molecule'].add([BlackToken()] * S1_amount)
        # S2 signal
        if random.random() < 0.8:
            S2_amount = random.randint(10, 20)
            marking['mozhayskiy_net']['donor'].add(['S2_molecule'] * S2_amount)
            marking['donor_0_net']['S2_molecule'].add([BlackToken()] * S2_amount)
            marking['mozhayskiy_net']['recipient'].add(['S2_molecule'] * S2_amount)
            marking['recipient_0_net']['S2_molecule'].add([BlackToken()] * S2_amount)

        s.step()
    s.draw_nets(os.path.join(output_path, "../topology_end"))
    s.make_charts(exclude=['gene', 'mrna', 'mediator', 'receptor', 'active', 'mediator', 'activation', 'mod', 'plasmid_strand'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)