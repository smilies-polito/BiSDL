from petrisim.utils import *


class Pennisi2016(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		hs_0_net = PetriNet("hs_0_net", timescale=1)
		pennisi2016_net = PetriNet("pennisi2016_net", timescale=1)

		# hs_0_net places
		hs_0_net.add_place(Place("ANTIGEN_molecule"))
		hs_0_net.add_place(Place("MP_molecule"))
		hs_0_net.add_place(Place("MP_ANTIGEN_molecule"))
		hs_0_net.add_place(Place("MP_ACTIVE_molecule"))
		hs_0_net.add_place(Place("TH_molecule"))
		hs_0_net.add_place(Place("TH_ACTIVE_molecule"))
		hs_0_net.add_place(Place("B_molecule"))
		hs_0_net.add_place(Place("B_ACTIVE_molecule"))
		hs_0_net.add_place(Place("IGM_molecule"))
		hs_0_net.add_place(Place("B_PRESENTING_molecule"))
		hs_0_net.add_place(Place("B_MEMORY_molecule"))
		hs_0_net.add_place(Place("B_PLASMA_molecule"))
		hs_0_net.add_place(Place("IGG_molecule"))
		hs_0_net.add_place(Place("VOID_molecule"))

		# hs_0_net transitions
		hs_0_net.add_transition(Transition("process_1"))
		hs_0_net.add_transition(Transition("process_2"))
		hs_0_net.add_transition(Transition("process_3"))
		hs_0_net.add_transition(Transition("process_4"))
		hs_0_net.add_transition(Transition("process_5"))
		hs_0_net.add_transition(Transition("process_6"))
		hs_0_net.add_transition(Transition("process_7"))
		hs_0_net.add_transition(Transition("process_8"))
		hs_0_net.add_transition(Transition("process_9"))
		hs_0_net.add_transition(Transition("process_10"))
		hs_0_net.add_transition(Transition("process_11"))
		hs_0_net.add_transition(Transition("process_12"))
		hs_0_net.add_transition(Transition("process_13"))
		hs_0_net.add_transition(Transition("process_14"))
		hs_0_net.add_transition(Transition("ANTIGEN_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("MP_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("TH_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("B_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("B_PLASMA_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("IGM_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("IGM_molecule_degradation_1_1"))
		hs_0_net.add_transition(Transition("IGM_molecule_degradation_2_1"))
		hs_0_net.add_transition(Transition("IGG_molecule_degradation_1"))
		hs_0_net.add_transition(Transition("IGG_molecule_degradation_1_1"))
		hs_0_net.add_transition(Transition("IGG_molecule_degradation_2_1"))
		hs_0_net.add_transition(Transition("IGG_molecule_degradation_3_1"))
		hs_0_net.add_transition(Transition("IGG_molecule_degradation_4_1"))

		# pennisi2016_net places
		pennisi2016_net.add_place(Place("victim", [ hs_0_net ]))

		# pennisi2016_net transitions


		# pennisi2016_net arcs



		# hs_0_net arcs
		hs_0_net.add_input("ANTIGEN_molecule", "process_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("MP_molecule", "process_2", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("MP_molecule", "process_3", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_3", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("MP_ANTIGEN_molecule", "process_4", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("TH_molecule", "process_5", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("TH_molecule", "process_6", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("MP_ACTIVE_molecule", "process_6", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_molecule", "process_7", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_molecule", "process_8", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_8", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_ACTIVE_molecule", "process_9", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_9", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_PRESENTING_molecule", "process_10", MultiArc([Value(dot)]*3), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("TH_ACTIVE_molecule", "process_10", MultiArc([Value(dot)]*3), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_MEMORY_molecule", "process_11", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_11", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_PLASMA_molecule", "process_12", MultiArc([Value(dot)]*2), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_13", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "process_13", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "process_14", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGM_molecule", "process_14", MultiArc([Value(dot)]*5), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("ANTIGEN_molecule", "ANTIGEN_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("MP_molecule", "MP_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("TH_molecule", "TH_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_molecule", "B_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("B_PLASMA_molecule", "B_PLASMA_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGM_molecule", "IGM_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGM_molecule", "IGM_molecule_degradation_1_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGM_molecule", "IGM_molecule_degradation_2_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "IGG_molecule_degradation_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "IGG_molecule_degradation_1_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "IGG_molecule_degradation_2_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "IGG_molecule_degradation_3_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_input("IGG_molecule", "IGG_molecule_degradation_4_1", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("ANTIGEN_molecule", "process_1", MultiArc([Value(dot)]*2), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("MP_molecule", "process_2", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("MP_ANTIGEN_molecule", "process_3", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("MP_ACTIVE_molecule", "process_4", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("TH_molecule", "process_5", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("TH_ACTIVE_molecule", "process_6", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("MP_ACTIVE_molecule", "process_6", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_molecule", "process_7", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_ACTIVE_molecule", "process_8", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("IGM_molecule", "process_8", MultiArc([Value(dot)]*5), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_PRESENTING_molecule", "process_9", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_MEMORY_molecule", "process_10", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_PLASMA_molecule", "process_10", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("TH_ACTIVE_molecule", "process_10", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_PLASMA_molecule", "process_11", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_MEMORY_molecule", "process_11", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("B_PLASMA_molecule", "process_12", MultiArc([Value(dot)]*2), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("IGG_molecule", "process_12", MultiArc([Value(dot)]*10), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("VOID_molecule", "process_13", Value(dot), notify=[pennisi2016_net.place('victim')])
		hs_0_net.add_output("VOID_molecule", "process_14", Value(dot), notify=[pennisi2016_net.place('victim')])
		return pennisi2016_net
