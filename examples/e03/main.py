from petrisim.utils import *


class simple_process(Module):
    def __init__(self, name: str = None):
        if not name:
            name = __class__.__name__
        super().__init__(name)

    def build_net_structure(self) -> PetriNet:
        super(self.__class__, self).build_net_structure()

        # petri nets
        process_B_0_net = PetriNet("process_B_0_net", timescale=1)
        process_A_0_net = PetriNet("process_A_0_net", timescale=1)
        simple_process_net = PetriNet("simple_process_net", timescale=5)

        # process_B_0_net places
        process_B_0_net.add_place(Place("B_gene", [BlackToken()]))
        process_B_0_net.add_place(Place("B_mrna"))
        process_B_0_net.add_place(Place("B_protein"))
        process_B_0_net.add_place(Place("A_receptor_active_protein"))
        process_B_0_net.add_place(Place("B2_protein"))

        # process_B_0_net transitions
        process_B_0_net.add_transition(Transition("B_gene_transcription_1"))
        process_B_0_net.add_transition(Transition("B_mrna_translation_1"))
        process_B_0_net.add_transition(Transition("enzymatic_reaction_1"))
        process_B_0_net.add_transition(Transition("B_protein_degradation_1"))
        process_B_0_net.add_transition(Transition("B_protein_degradation_1_1"))
        process_B_0_net.add_transition(Transition("B_protein_degradation_2_1"))
        process_B_0_net.add_transition(Transition("A_receptor_active_protein_degradation_1"))

        # process_A_0_net places
        process_A_0_net.add_place(Place("A_gene", [BlackToken()]))
        process_A_0_net.add_place(Place("A_mrna"))
        process_A_0_net.add_place(Place("A_protein"))

        # process_A_0_net transitions
        process_A_0_net.add_transition(Transition("A_gene_transcription_1"))
        process_A_0_net.add_transition(Transition("A_mrna_translation_1"))
        process_A_0_net.add_transition(Transition("A_protein_degradation_1"))

        # simple_process_net places
        simple_process_net.add_place(Place("cell_A", [ process_A_0_net ]))
        simple_process_net.add_place(Place("cell_B", [ process_B_0_net ]))

        # simple_process_net transitions
        simple_process_net.add_transition(Transition("juxtacrine_signaling_A_protein_cell_A_cell_B_1", Expression("str(x) == 'A_protein'")))

        # simple_process_net arcs
        simple_process_net.add_input("cell_A", "juxtacrine_signaling_A_protein_cell_A_cell_B_1", Variable('x'), notify=[process_A_0_net])
        simple_process_net.add_output("cell_B", "juxtacrine_signaling_A_protein_cell_A_cell_B_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[process_B_0_net])

        # process_A_0_net arcs
        process_A_0_net.add_input("A_gene", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_input("A_mrna", "A_mrna_translation_1", Value(dot))
        process_A_0_net.add_input("A_protein", "A_protein_degradation_1", Value(dot), notify=[simple_process_net.place('cell_A')])
        process_A_0_net.add_output("A_gene", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_output("A_mrna", "A_gene_transcription_1", Value(dot))
        process_A_0_net.add_output("A_protein", "A_mrna_translation_1", MultiArc([Value(dot)]*5), notify=[simple_process_net.place('cell_A')])

        # process_B_0_net arcs
        process_B_0_net.add_input("B_gene", "B_gene_transcription_1", Value(dot))
        process_B_0_net.add_input("B_mrna", "B_mrna_translation_1", Value(dot))
        process_B_0_net.add_input("B_protein", "enzymatic_reaction_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_input("A_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_input("B_protein", "B_protein_degradation_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_input("B_protein", "B_protein_degradation_1_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_input("B_protein", "B_protein_degradation_2_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_input("A_receptor_active_protein", "A_receptor_active_protein_degradation_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_output("B_gene", "B_gene_transcription_1", Value(dot))
        process_B_0_net.add_output("B_mrna", "B_gene_transcription_1", Value(dot))
        process_B_0_net.add_output("B_protein", "B_mrna_translation_1", MultiArc([Value(dot)]*3), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_output("B_protein", "enzymatic_reaction_1", Value(dot), notify=[simple_process_net.place('cell_B')])
        process_B_0_net.add_output("B2_protein", "enzymatic_reaction_1", Value(dot), notify=[simple_process_net.place('cell_B')])

        return simple_process_net

if __name__ == "__main__":
    import os
    from petrisim.simulator import *

    test_module = simple_process()
    output_path = os.path.join(".", "results")
    n_steps = 300
    s = Simulator(m=test_module, steps=n_steps, output_path=output_path, draw_nets=False)
    s.draw_nets(os.path.join(output_path, "../topology"))

    s.execute()

    s.make_charts(exclude=['gene', 'mrna'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)
