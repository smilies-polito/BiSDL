from petrisim.utils import *


class Notify(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		notify_net = PetriNet("notify_net", timescale=1)

		# notify_net places
		notify_net.add_place(Place("cell_1"))
		notify_net.add_place(Place("cell_2"))

		# notify_net transitions
		notify_net.add_transition(Transition("juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Expression("str(x) == 'quiquoqua_protein'")))
		notify_net.add_transition(Transition("juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Expression("str(x) == 'paperino_protein'")))
		notify_net.add_transition(Transition("diffusion_aaa_protein_1", Expression("str(x) == 'aaa_protein'")))
		notify_net.add_transition(Transition("diffusion_aaa_protein_2", Expression("str(x) == 'aaa_protein'")))
		notify_net.add_transition(Transition("diffusion_bbb_molecule_1", Expression("str(x) == 'bbb_molecule'")))
		notify_net.add_transition(Transition("diffusion_bbb_molecule_2", Expression("str(x) == 'bbb_molecule'")))

		# notify_net arcs
		notify_net.add_input("cell_1", "juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Variable('x'), notify=[])
		notify_net.add_input("cell_2", "juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Variable('x'), notify=[])
		notify_net.add_input("cell_1", "diffusion_aaa_protein_1", Variable('x'), notify=[])
		notify_net.add_input("cell_2", "diffusion_aaa_protein_2", Variable('x'), notify=[])
		notify_net.add_input("cell_1", "diffusion_bbb_molecule_1", Variable('x'), notify=[])
		notify_net.add_input("cell_2", "diffusion_bbb_molecule_2", Variable('x'), notify=[])
		notify_net.add_output("cell_2", "juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[])
		notify_net.add_output("cell_1", "juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[])
		notify_net.add_output("cell_2", "diffusion_aaa_protein_1", Variable('x'), notify=[])
		notify_net.add_output("cell_1", "diffusion_aaa_protein_2", Variable('x'), notify=[])
		notify_net.add_output("cell_2", "diffusion_bbb_molecule_1", Variable('x'), notify=[])
		notify_net.add_output("cell_1", "diffusion_bbb_molecule_2", Variable('x'), notify=[])
		return notify_net
