from petrisim.utils import *


class E02(Module):
    def __init__(self, name: str = None):
        if not name:
            name = __class__.__name__
        super().__init__(name)

    def build_net_structure(self) -> PetriNet:
        # petri nets
        process_B_0_net = PetriNet("process_B_0_net", timescale=1)
        process_A_0_net = PetriNet("process_A_0_net", timescale=1)
        e02_net = PetriNet("e02_net", timescale=1)

        # process_B_0_net places
        process_B_0_net.add_place(Place("A_receptor_active_protein"))

        # process_B_0_net transitions
        process_B_0_net.add_transition(Transition("A_receptor_active_protein_degradation_1"))

        # process_A_0_net places
        process_A_0_net.add_place(Place("A_gene", [BlackToken()]))
        process_A_0_net.add_place(Place("A_mrna"))
        process_A_0_net.add_place(Place("A_protein"))

        # process_A_0_net transitions
        process_A_0_net.add_transition(Transition("A_gene_transcription_1"))
        process_A_0_net.add_transition(Transition("A_mrna_translation_1"))
        process_A_0_net.add_transition(Transition("A_protein_degradation_1"))

        # e02_net places
        e02_net.add_place(Place("cell_A", [process_A_0_net]))
        e02_net.add_place(Place("cell_B", [process_B_0_net]))

        # e02_net transitions
        e02_net.add_transition(
            Transition("juxtacrine_signaling_A_protein_cell_A_cell_B_1", Expression("str(x) == 'A_protein'")))

        # e02_net arcs
        e02_net.add_input("cell_A", "juxtacrine_signaling_A_protein_cell_A_cell_B_1", Variable('x'),
                          notify=[process_A_0_net])
        e02_net.add_output("cell_B", "juxtacrine_signaling_A_protein_cell_A_cell_B_1",
                           Expression('x.replace("protein", "receptor_active_protein")'), notify=[process_B_0_net])

        # process_A_0_net arcs
        process_A_0_net.add_input("A_gene", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_input("A_mrna", "A_mrna_translation_1", Value(dot))
        process_A_0_net.add_input("A_protein", "A_protein_degradation_1", Value(dot), notify=[e02_net.place('cell_A')])
        process_A_0_net.add_output("A_gene", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_output("A_mrna", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_output("A_protein", "A_mrna_translation_1", MultiArc([Value(dot)] * 3),
                                   notify=[e02_net.place('cell_A')])

        # process_B_0_net arcs
        process_B_0_net.add_input("A_receptor_active_protein", "A_receptor_active_protein_degradation_1", Value(dot),
                                  notify=[e02_net.place('cell_B')])

        return e02_net


if __name__ == "__main__":
    import os
    from petrisim.simulator import *

    test_module = E02()
    output_path = os.path.join(".", "results")
    n_steps = 100
    s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
    s.draw_nets(os.path.join(output_path, "../topology"))

    for _ in range(n_steps):
        s.step()

    s.make_charts(exclude=['gene', 'mrna'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)
