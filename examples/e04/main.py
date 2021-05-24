from petrisim.utils import *


class rgb_pattern(Module):
    def __init__(self, name: str = None):
        if not name:
            name = __class__.__name__
        super().__init__(name)

    def build_net_structure(self) -> PetriNet:
        super(self.__class__, self).build_net_structure()

        # petri nets
        BFP_production_7_net = PetriNet("BFP_production_7_net", timescale=1)
        CD19_mCherry_production_7_net = PetriNet("CD19_mCherry_production_7_net", timescale=1)
        BFP_production_6_net = PetriNet("BFP_production_6_net", timescale=1)
        CD19_mCherry_production_6_net = PetriNet("CD19_mCherry_production_6_net", timescale=1)
        BFP_production_5_net = PetriNet("BFP_production_5_net", timescale=1)
        CD19_mCherry_production_5_net = PetriNet("CD19_mCherry_production_5_net", timescale=1)
        BFP_production_4_net = PetriNet("BFP_production_4_net", timescale=1)
        CD19_mCherry_production_4_net = PetriNet("CD19_mCherry_production_4_net", timescale=1)
        BFP_production_3_net = PetriNet("BFP_production_3_net", timescale=1)
        CD19_mCherry_production_3_net = PetriNet("CD19_mCherry_production_3_net", timescale=1)
        BFP_production_2_net = PetriNet("BFP_production_2_net", timescale=1)
        CD19_mCherry_production_2_net = PetriNet("CD19_mCherry_production_2_net", timescale=1)
        BFP_production_1_net = PetriNet("BFP_production_1_net", timescale=1)
        CD19_mCherry_production_1_net = PetriNet("CD19_mCherry_production_1_net", timescale=1)
        BFP_production_0_net = PetriNet("BFP_production_0_net", timescale=1)
        CD19_mCherry_production_0_net = PetriNet("CD19_mCherry_production_0_net", timescale=1)
        GFP_production_0_net = PetriNet("GFP_production_0_net", timescale=1)
        rgb_pattern_net = PetriNet("rgb_pattern_net", timescale=1)

        # BFP_production_7_net places
        BFP_production_7_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_7_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_7_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_7_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_7_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_7_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_7_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_7_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_7_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_7_net.add_place(Place("BFP_mrna"))
        BFP_production_7_net.add_place(Place("BFP_protein"))

        # BFP_production_7_net transitions
        BFP_production_7_net.add_transition(Transition("GFP_receptor_gene_transcription_2_7"))
        BFP_production_7_net.add_transition(Transition("GFP_receptor_mrna_translation_2_7"))
        BFP_production_7_net.add_transition(Transition("enzymatic_reaction_3_7"))
        BFP_production_7_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_7"))
        BFP_production_7_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_7"))
        BFP_production_7_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_7"))
        BFP_production_7_net.add_transition(Transition("enzymatic_reaction_4_7"))
        BFP_production_7_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_7"))
        BFP_production_7_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_7"))
        BFP_production_7_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_7"))
        BFP_production_7_net.add_transition(Transition("BFP_gene_transcription_2_7"))
        BFP_production_7_net.add_transition(Transition("BFP_mrna_translation_2_7"))

        # CD19_mCherry_production_7_net places
        CD19_mCherry_production_7_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_7_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_7_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_7_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_7_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_7_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_7_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_7_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_7_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_7_net transitions
        CD19_mCherry_production_7_net.add_transition(Transition("GFP_receptor_gene_transcription_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("GFP_receptor_mrna_translation_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("enzymatic_reaction_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("enzymatic_reaction_2_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("BFP_gene_transcription_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("BFP_mrna_translation_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_7"))
        CD19_mCherry_production_7_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_7"))

        # BFP_production_6_net places
        BFP_production_6_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_6_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_6_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_6_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_6_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_6_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_6_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_6_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_6_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_6_net.add_place(Place("BFP_mrna"))
        BFP_production_6_net.add_place(Place("BFP_protein"))

        # BFP_production_6_net transitions
        BFP_production_6_net.add_transition(Transition("GFP_receptor_gene_transcription_2_6"))
        BFP_production_6_net.add_transition(Transition("GFP_receptor_mrna_translation_2_6"))
        BFP_production_6_net.add_transition(Transition("enzymatic_reaction_3_6"))
        BFP_production_6_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_6"))
        BFP_production_6_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_6"))
        BFP_production_6_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_6"))
        BFP_production_6_net.add_transition(Transition("enzymatic_reaction_4_6"))
        BFP_production_6_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_6"))
        BFP_production_6_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_6"))
        BFP_production_6_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_6"))
        BFP_production_6_net.add_transition(Transition("BFP_gene_transcription_2_6"))
        BFP_production_6_net.add_transition(Transition("BFP_mrna_translation_2_6"))

        # CD19_mCherry_production_6_net places
        CD19_mCherry_production_6_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_6_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_6_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_6_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_6_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_6_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_6_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_6_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_6_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_6_net transitions
        CD19_mCherry_production_6_net.add_transition(Transition("GFP_receptor_gene_transcription_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("GFP_receptor_mrna_translation_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("enzymatic_reaction_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("enzymatic_reaction_2_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("BFP_gene_transcription_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("BFP_mrna_translation_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_6"))
        CD19_mCherry_production_6_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_6"))

        # BFP_production_5_net places
        BFP_production_5_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_5_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_5_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_5_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_5_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_5_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_5_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_5_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_5_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_5_net.add_place(Place("BFP_mrna"))
        BFP_production_5_net.add_place(Place("BFP_protein"))

        # BFP_production_5_net transitions
        BFP_production_5_net.add_transition(Transition("GFP_receptor_gene_transcription_2_5"))
        BFP_production_5_net.add_transition(Transition("GFP_receptor_mrna_translation_2_5"))
        BFP_production_5_net.add_transition(Transition("enzymatic_reaction_3_5"))
        BFP_production_5_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_5"))
        BFP_production_5_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_5"))
        BFP_production_5_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_5"))
        BFP_production_5_net.add_transition(Transition("enzymatic_reaction_4_5"))
        BFP_production_5_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_5"))
        BFP_production_5_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_5"))
        BFP_production_5_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_5"))
        BFP_production_5_net.add_transition(Transition("BFP_gene_transcription_2_5"))
        BFP_production_5_net.add_transition(Transition("BFP_mrna_translation_2_5"))

        # CD19_mCherry_production_5_net places
        CD19_mCherry_production_5_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_5_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_5_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_5_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_5_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_5_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_5_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_5_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_5_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_5_net transitions
        CD19_mCherry_production_5_net.add_transition(Transition("GFP_receptor_gene_transcription_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("GFP_receptor_mrna_translation_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("enzymatic_reaction_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("enzymatic_reaction_2_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("BFP_gene_transcription_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("BFP_mrna_translation_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_5"))
        CD19_mCherry_production_5_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_5"))

        # BFP_production_4_net places
        BFP_production_4_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_4_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_4_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_4_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_4_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_4_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_4_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_4_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_4_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_4_net.add_place(Place("BFP_mrna"))
        BFP_production_4_net.add_place(Place("BFP_protein"))

        # BFP_production_4_net transitions
        BFP_production_4_net.add_transition(Transition("GFP_receptor_gene_transcription_2_4"))
        BFP_production_4_net.add_transition(Transition("GFP_receptor_mrna_translation_2_4"))
        BFP_production_4_net.add_transition(Transition("enzymatic_reaction_3_4"))
        BFP_production_4_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_4"))
        BFP_production_4_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_4"))
        BFP_production_4_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_4"))
        BFP_production_4_net.add_transition(Transition("enzymatic_reaction_4_4"))
        BFP_production_4_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_4"))
        BFP_production_4_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_4"))
        BFP_production_4_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_4"))
        BFP_production_4_net.add_transition(Transition("BFP_gene_transcription_2_4"))
        BFP_production_4_net.add_transition(Transition("BFP_mrna_translation_2_4"))

        # CD19_mCherry_production_4_net places
        CD19_mCherry_production_4_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_4_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_4_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_4_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_4_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_4_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_4_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_4_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_4_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_4_net transitions
        CD19_mCherry_production_4_net.add_transition(Transition("GFP_receptor_gene_transcription_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("GFP_receptor_mrna_translation_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("enzymatic_reaction_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("enzymatic_reaction_2_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("BFP_gene_transcription_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("BFP_mrna_translation_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_4"))
        CD19_mCherry_production_4_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_4"))

        # BFP_production_3_net places
        BFP_production_3_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_3_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_3_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_3_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_3_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_3_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_3_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_3_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_3_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_3_net.add_place(Place("BFP_mrna"))
        BFP_production_3_net.add_place(Place("BFP_protein"))

        # BFP_production_3_net transitions
        BFP_production_3_net.add_transition(Transition("GFP_receptor_gene_transcription_2_3"))
        BFP_production_3_net.add_transition(Transition("GFP_receptor_mrna_translation_2_3"))
        BFP_production_3_net.add_transition(Transition("enzymatic_reaction_3_3"))
        BFP_production_3_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_3"))
        BFP_production_3_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_3"))
        BFP_production_3_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_3"))
        BFP_production_3_net.add_transition(Transition("enzymatic_reaction_4_3"))
        BFP_production_3_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_3"))
        BFP_production_3_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_3"))
        BFP_production_3_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_3"))
        BFP_production_3_net.add_transition(Transition("BFP_gene_transcription_2_3"))
        BFP_production_3_net.add_transition(Transition("BFP_mrna_translation_2_3"))

        # CD19_mCherry_production_3_net places
        CD19_mCherry_production_3_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_3_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_3_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_3_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_3_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_3_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_3_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_3_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_3_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_3_net transitions
        CD19_mCherry_production_3_net.add_transition(Transition("GFP_receptor_gene_transcription_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("GFP_receptor_mrna_translation_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("enzymatic_reaction_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("enzymatic_reaction_2_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("BFP_gene_transcription_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("BFP_mrna_translation_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_3"))
        CD19_mCherry_production_3_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_3"))

        # BFP_production_2_net places
        BFP_production_2_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_2_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_2_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_2_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_2_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_2_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_2_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_2_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_2_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_2_net.add_place(Place("BFP_mrna"))
        BFP_production_2_net.add_place(Place("BFP_protein"))

        # BFP_production_2_net transitions
        BFP_production_2_net.add_transition(Transition("GFP_receptor_gene_transcription_2_2"))
        BFP_production_2_net.add_transition(Transition("GFP_receptor_mrna_translation_2_2"))
        BFP_production_2_net.add_transition(Transition("enzymatic_reaction_3_2"))
        BFP_production_2_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_2"))
        BFP_production_2_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_2"))
        BFP_production_2_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_2"))
        BFP_production_2_net.add_transition(Transition("enzymatic_reaction_4_2"))
        BFP_production_2_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_2"))
        BFP_production_2_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_2"))
        BFP_production_2_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_2"))
        BFP_production_2_net.add_transition(Transition("BFP_gene_transcription_2_2"))
        BFP_production_2_net.add_transition(Transition("BFP_mrna_translation_2_2"))

        # CD19_mCherry_production_2_net places
        CD19_mCherry_production_2_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_2_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_2_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_2_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_2_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_2_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_2_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_2_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_2_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_2_net transitions
        CD19_mCherry_production_2_net.add_transition(Transition("GFP_receptor_gene_transcription_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("GFP_receptor_mrna_translation_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("enzymatic_reaction_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("enzymatic_reaction_2_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("BFP_gene_transcription_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("BFP_mrna_translation_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_2"))
        CD19_mCherry_production_2_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_2"))

        # BFP_production_1_net places
        BFP_production_1_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_1_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_1_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_1_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_1_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_1_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_1_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_1_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_1_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_1_net.add_place(Place("BFP_mrna"))
        BFP_production_1_net.add_place(Place("BFP_protein"))

        # BFP_production_1_net transitions
        BFP_production_1_net.add_transition(Transition("GFP_receptor_gene_transcription_2_1"))
        BFP_production_1_net.add_transition(Transition("GFP_receptor_mrna_translation_2_1"))
        BFP_production_1_net.add_transition(Transition("enzymatic_reaction_3_1"))
        BFP_production_1_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2_1"))
        BFP_production_1_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2_1"))
        BFP_production_1_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2_1"))
        BFP_production_1_net.add_transition(Transition("enzymatic_reaction_4_1"))
        BFP_production_1_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2_1"))
        BFP_production_1_net.add_transition(Transition("CD19_mCherry_gene_transcription_2_1"))
        BFP_production_1_net.add_transition(Transition("CD19_mCherry_mrna_translation_2_1"))
        BFP_production_1_net.add_transition(Transition("BFP_gene_transcription_2_1"))
        BFP_production_1_net.add_transition(Transition("BFP_mrna_translation_2_1"))

        # CD19_mCherry_production_1_net places
        CD19_mCherry_production_1_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_1_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_1_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_1_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_1_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_1_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_1_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_1_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_1_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_1_net transitions
        CD19_mCherry_production_1_net.add_transition(Transition("GFP_receptor_gene_transcription_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("GFP_receptor_mrna_translation_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("enzymatic_reaction_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("enzymatic_reaction_2_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("CD19_mCherry_gene_transcription_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("CD19_mCherry_mrna_translation_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("BFP_gene_transcription_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("BFP_mrna_translation_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_1"))
        CD19_mCherry_production_1_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1_1"))

        # BFP_production_0_net places
        BFP_production_0_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        BFP_production_0_net.add_place(Place("GFP_receptor_mrna"))
        BFP_production_0_net.add_place(Place("GFP_receptor_protein"))
        BFP_production_0_net.add_place(Place("GFP_receptor_active_protein"))
        BFP_production_0_net.add_place(Place("GFP_activation_mediator_protein"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        BFP_production_0_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_receptor_protein"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        BFP_production_0_net.add_place(Place("CD19_mCherry_mrna"))
        BFP_production_0_net.add_place(Place("CD19_mCherry_protein"))
        BFP_production_0_net.add_place(Place("BFP_gene", [BlackToken()]))
        BFP_production_0_net.add_place(Place("BFP_mrna"))
        BFP_production_0_net.add_place(Place("BFP_protein"))

        # BFP_production_0_net transitions
        BFP_production_0_net.add_transition(Transition("GFP_receptor_gene_transcription_2"))
        BFP_production_0_net.add_transition(Transition("GFP_receptor_mrna_translation_2"))
        BFP_production_0_net.add_transition(Transition("enzymatic_reaction_3"))
        BFP_production_0_net.add_transition(Transition("GFP_receptor_active_protein_degradation_2"))
        BFP_production_0_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_2"))
        BFP_production_0_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_2"))
        BFP_production_0_net.add_transition(Transition("enzymatic_reaction_4"))
        BFP_production_0_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_2"))
        BFP_production_0_net.add_transition(Transition("CD19_mCherry_gene_transcription_2"))
        BFP_production_0_net.add_transition(Transition("CD19_mCherry_mrna_translation_2"))
        BFP_production_0_net.add_transition(Transition("BFP_gene_transcription_2"))
        BFP_production_0_net.add_transition(Transition("BFP_mrna_translation_2"))

        # CD19_mCherry_production_0_net places
        CD19_mCherry_production_0_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_0_net.add_place(Place("GFP_receptor_mrna"))
        CD19_mCherry_production_0_net.add_place(Place("GFP_receptor_protein"))
        CD19_mCherry_production_0_net.add_place(Place("GFP_receptor_active_protein"))
        CD19_mCherry_production_0_net.add_place(Place("GFP_activation_mediator_protein"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_receptor_gene", [BlackToken()]))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_receptor_mrna"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_receptor_protein"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_receptor_active_protein"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_activation_mediator_protein"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_gene", [BlackToken()]))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_mrna"))
        CD19_mCherry_production_0_net.add_place(Place("CD19_mCherry_protein"))
        CD19_mCherry_production_0_net.add_place(Place("BFP_gene", [BlackToken()]))
        CD19_mCherry_production_0_net.add_place(Place("BFP_mrna"))
        CD19_mCherry_production_0_net.add_place(Place("BFP_protein"))

        # CD19_mCherry_production_0_net transitions
        CD19_mCherry_production_0_net.add_transition(Transition("GFP_receptor_gene_transcription_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("GFP_receptor_mrna_translation_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("enzymatic_reaction_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("CD19_mCherry_receptor_gene_transcription_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("CD19_mCherry_receptor_mrna_translation_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("enzymatic_reaction_2"))
        CD19_mCherry_production_0_net.add_transition(Transition("CD19_mCherry_gene_transcription_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("CD19_mCherry_mrna_translation_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("BFP_gene_transcription_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("BFP_mrna_translation_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1"))
        CD19_mCherry_production_0_net.add_transition(Transition("CD19_mCherry_receptor_active_protein_degradation_1"))

        # GFP_production_0_net places
        GFP_production_0_net.add_place(Place("GFP_gene", [BlackToken()]))
        GFP_production_0_net.add_place(Place("GFP_mrna"))
        GFP_production_0_net.add_place(Place("GFP_protein"))

        # GFP_production_0_net transitions
        GFP_production_0_net.add_transition(Transition("GFP_gene_transcription_1"))
        GFP_production_0_net.add_transition(Transition("GFP_mrna_translation_1"))

        # rgb_pattern_net places
        rgb_pattern_net.add_place(Place("sender_cell", [GFP_production_0_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_5_6", [CD19_mCherry_production_0_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_5_7", [BFP_production_0_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_6_6", [CD19_mCherry_production_1_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_7_7", [BFP_production_1_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_6_5", [CD19_mCherry_production_2_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_7_5", [BFP_production_2_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_6_4", [CD19_mCherry_production_3_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_7_3", [BFP_production_3_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_5_4", [CD19_mCherry_production_4_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_5_3", [BFP_production_4_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_4_4", [CD19_mCherry_production_5_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_3_3", [BFP_production_5_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_4_5", [CD19_mCherry_production_6_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_3_5", [BFP_production_6_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_4_6", [CD19_mCherry_production_7_net]))
        rgb_pattern_net.add_place(Place("receiver_cell_3_7", [BFP_production_7_net]))

        # rgb_pattern_net transitions
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_4_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_5_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_6_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_4_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_6_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_4_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_5_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_6_1",
                                                  Expression("str(x) == 'GFP_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_6_receiver_cell_5_7_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_7_receiver_cell_5_6_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_6_receiver_cell_7_7_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_7_receiver_cell_6_6_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_5_receiver_cell_7_5_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_5_receiver_cell_6_5_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_4_receiver_cell_7_3_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_3_receiver_cell_6_4_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_4_receiver_cell_5_3_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_3_receiver_cell_5_4_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_4_receiver_cell_3_3_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_3_receiver_cell_4_4_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_5_receiver_cell_3_5_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_5_receiver_cell_4_5_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_6_receiver_cell_3_7_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))
        rgb_pattern_net.add_transition(
            Transition("juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_7_receiver_cell_4_6_1",
                       Expression("str(x) == 'CD19_mCherry_protein'")))

        # rgb_pattern_net arcs
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_4_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_5_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_6_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_4_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_6_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_4_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_5_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("sender_cell", "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_6_1",
                                  Variable('x'), notify=[GFP_production_0_net])
        rgb_pattern_net.add_input("receiver_cell_5_6",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_6_receiver_cell_5_7_1",
                                  Variable('x'), notify=[CD19_mCherry_production_0_net])
        rgb_pattern_net.add_input("receiver_cell_5_7",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_7_receiver_cell_5_6_1",
                                  Variable('x'), notify=[BFP_production_0_net])
        rgb_pattern_net.add_input("receiver_cell_6_6",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_6_receiver_cell_7_7_1",
                                  Variable('x'), notify=[CD19_mCherry_production_1_net])
        rgb_pattern_net.add_input("receiver_cell_7_7",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_7_receiver_cell_6_6_1",
                                  Variable('x'), notify=[BFP_production_1_net])
        rgb_pattern_net.add_input("receiver_cell_6_5",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_5_receiver_cell_7_5_1",
                                  Variable('x'), notify=[CD19_mCherry_production_2_net])
        rgb_pattern_net.add_input("receiver_cell_7_5",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_5_receiver_cell_6_5_1",
                                  Variable('x'), notify=[BFP_production_2_net])
        rgb_pattern_net.add_input("receiver_cell_6_4",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_4_receiver_cell_7_3_1",
                                  Variable('x'), notify=[CD19_mCherry_production_3_net])
        rgb_pattern_net.add_input("receiver_cell_7_3",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_3_receiver_cell_6_4_1",
                                  Variable('x'), notify=[BFP_production_3_net])
        rgb_pattern_net.add_input("receiver_cell_5_4",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_4_receiver_cell_5_3_1",
                                  Variable('x'), notify=[CD19_mCherry_production_4_net])
        rgb_pattern_net.add_input("receiver_cell_5_3",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_3_receiver_cell_5_4_1",
                                  Variable('x'), notify=[BFP_production_4_net])
        rgb_pattern_net.add_input("receiver_cell_4_4",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_4_receiver_cell_3_3_1",
                                  Variable('x'), notify=[CD19_mCherry_production_5_net])
        rgb_pattern_net.add_input("receiver_cell_3_3",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_3_receiver_cell_4_4_1",
                                  Variable('x'), notify=[BFP_production_5_net])
        rgb_pattern_net.add_input("receiver_cell_4_5",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_5_receiver_cell_3_5_1",
                                  Variable('x'), notify=[CD19_mCherry_production_6_net])
        rgb_pattern_net.add_input("receiver_cell_3_5",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_5_receiver_cell_4_5_1",
                                  Variable('x'), notify=[BFP_production_6_net])
        rgb_pattern_net.add_input("receiver_cell_4_6",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_6_receiver_cell_3_7_1",
                                  Variable('x'), notify=[CD19_mCherry_production_7_net])
        rgb_pattern_net.add_input("receiver_cell_3_7",
                                  "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_7_receiver_cell_4_6_1",
                                  Variable('x'), notify=[BFP_production_7_net])
        rgb_pattern_net.add_output("receiver_cell_4_4",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_5_net])
        rgb_pattern_net.add_output("receiver_cell_4_5",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_6_net])
        rgb_pattern_net.add_output("receiver_cell_4_6",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_4_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_7_net])
        rgb_pattern_net.add_output("receiver_cell_5_4",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_4_net])
        rgb_pattern_net.add_output("receiver_cell_5_6",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_5_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_0_net])
        rgb_pattern_net.add_output("receiver_cell_6_4",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_3_net])
        rgb_pattern_net.add_output("receiver_cell_6_5",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_2_net])
        rgb_pattern_net.add_output("receiver_cell_6_6",
                                   "juxtacrine_signaling_GFP_protein_sender_cell_receiver_cell_6_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_1_net])
        rgb_pattern_net.add_output("receiver_cell_5_7",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_6_receiver_cell_5_7_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_0_net])
        rgb_pattern_net.add_output("receiver_cell_5_6",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_7_receiver_cell_5_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_0_net])
        rgb_pattern_net.add_output("receiver_cell_7_7",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_6_receiver_cell_7_7_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_1_net])
        rgb_pattern_net.add_output("receiver_cell_6_6",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_7_receiver_cell_6_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_1_net])
        rgb_pattern_net.add_output("receiver_cell_7_5",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_5_receiver_cell_7_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_2_net])
        rgb_pattern_net.add_output("receiver_cell_6_5",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_5_receiver_cell_6_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_2_net])
        rgb_pattern_net.add_output("receiver_cell_7_3",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_6_4_receiver_cell_7_3_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_3_net])
        rgb_pattern_net.add_output("receiver_cell_6_4",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_7_3_receiver_cell_6_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_3_net])
        rgb_pattern_net.add_output("receiver_cell_5_3",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_4_receiver_cell_5_3_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_4_net])
        rgb_pattern_net.add_output("receiver_cell_5_4",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_5_3_receiver_cell_5_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_4_net])
        rgb_pattern_net.add_output("receiver_cell_3_3",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_4_receiver_cell_3_3_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_5_net])
        rgb_pattern_net.add_output("receiver_cell_4_4",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_3_receiver_cell_4_4_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_5_net])
        rgb_pattern_net.add_output("receiver_cell_3_5",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_5_receiver_cell_3_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_6_net])
        rgb_pattern_net.add_output("receiver_cell_4_5",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_5_receiver_cell_4_5_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_6_net])
        rgb_pattern_net.add_output("receiver_cell_3_7",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_4_6_receiver_cell_3_7_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[BFP_production_7_net])
        rgb_pattern_net.add_output("receiver_cell_4_6",
                                   "juxtacrine_signaling_CD19_mCherry_protein_receiver_cell_3_7_receiver_cell_4_6_1",
                                   Expression('x.replace("protein", "receptor_active_protein")'),
                                   notify=[CD19_mCherry_production_7_net])

        # GFP_production_0_net arcs
        GFP_production_0_net.add_input("GFP_gene", "GFP_gene_transcription_1", Value(dot))
        GFP_production_0_net.add_input("GFP_mrna", "GFP_mrna_translation_1", Value(dot))
        GFP_production_0_net.add_output("GFP_gene", "GFP_gene_transcription_1", Value(dot))
        GFP_production_0_net.add_output("GFP_mrna", "GFP_gene_transcription_1", Value(dot))
        GFP_production_0_net.add_output("GFP_protein", "GFP_mrna_translation_1", MultiArc([Value(dot)] * 5),
                                        notify=[rgb_pattern_net.place('sender_cell')])

        # CD19_mCherry_production_0_net arcs
        CD19_mCherry_production_0_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_1",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("BFP_gene", "BFP_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_1",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("BFP_mrna", "BFP_mrna_translation_1", Value(dot))
        CD19_mCherry_production_0_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])
        CD19_mCherry_production_0_net.add_output("BFP_gene", "BFP_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("BFP_mrna", "BFP_gene_transcription_1", Value(dot))
        CD19_mCherry_production_0_net.add_output("BFP_protein", "BFP_mrna_translation_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_6')])

        # BFP_production_0_net arcs
        BFP_production_0_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2", Value(dot))
        BFP_production_0_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2",
                                       Value(dot))
        BFP_production_0_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2",
                                       Value(dot))
        BFP_production_0_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2", Value(dot))
        BFP_production_0_net.add_input("BFP_gene", "BFP_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_input("BFP_mrna", "BFP_mrna_translation_2", Value(dot))
        BFP_production_0_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2",
                                        Value(dot))
        BFP_production_0_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2",
                                        Value(dot))
        BFP_production_0_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])
        BFP_production_0_net.add_output("BFP_gene", "BFP_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("BFP_mrna", "BFP_gene_transcription_2", Value(dot))
        BFP_production_0_net.add_output("BFP_protein", "BFP_mrna_translation_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_7')])

        # CD19_mCherry_production_1_net arcs
        CD19_mCherry_production_1_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_1",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("BFP_gene", "BFP_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("BFP_mrna", "BFP_mrna_translation_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_1", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_1",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_1",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_1",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_1",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_1",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_6')])
        CD19_mCherry_production_1_net.add_output("BFP_gene", "BFP_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("BFP_mrna", "BFP_gene_transcription_1_1", Value(dot))
        CD19_mCherry_production_1_net.add_output("BFP_protein", "BFP_mrna_translation_1_1", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_6')])

        # BFP_production_1_net arcs
        BFP_production_1_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_1", Value(dot))
        BFP_production_1_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_1", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_1", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_1",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_1",
                                       Value(dot))
        BFP_production_1_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_1",
                                       Value(dot))
        BFP_production_1_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_1", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_1", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_1", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_1",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_1", Value(dot))
        BFP_production_1_net.add_input("BFP_gene", "BFP_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_1",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_input("BFP_mrna", "BFP_mrna_translation_2_1", Value(dot))
        BFP_production_1_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_1",
                                        Value(dot))
        BFP_production_1_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_1",
                                        Value(dot))
        BFP_production_1_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_1",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_1",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])
        BFP_production_1_net.add_output("BFP_gene", "BFP_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("BFP_mrna", "BFP_gene_transcription_2_1", Value(dot))
        BFP_production_1_net.add_output("BFP_protein", "BFP_mrna_translation_2_1", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_7')])

        # CD19_mCherry_production_2_net arcs
        CD19_mCherry_production_2_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_2",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("BFP_gene", "BFP_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("BFP_mrna", "BFP_mrna_translation_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_2", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_2", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_2", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_2",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_2",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_5')])
        CD19_mCherry_production_2_net.add_output("BFP_gene", "BFP_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("BFP_mrna", "BFP_gene_transcription_1_2", Value(dot))
        CD19_mCherry_production_2_net.add_output("BFP_protein", "BFP_mrna_translation_1_2", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_5')])

        # BFP_production_2_net arcs
        BFP_production_2_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_2", Value(dot))
        BFP_production_2_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_2",
                                       Value(dot))
        BFP_production_2_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_2",
                                       Value(dot))
        BFP_production_2_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_2", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_2", Value(dot))
        BFP_production_2_net.add_input("BFP_gene", "BFP_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_2",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_input("BFP_mrna", "BFP_mrna_translation_2_2", Value(dot))
        BFP_production_2_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_2",
                                        Value(dot))
        BFP_production_2_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_2",
                                        Value(dot))
        BFP_production_2_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_2",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_2",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])
        BFP_production_2_net.add_output("BFP_gene", "BFP_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("BFP_mrna", "BFP_gene_transcription_2_2", Value(dot))
        BFP_production_2_net.add_output("BFP_protein", "BFP_mrna_translation_2_2", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_5')])

        # CD19_mCherry_production_3_net arcs
        CD19_mCherry_production_3_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_3",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("BFP_gene", "BFP_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("BFP_mrna", "BFP_mrna_translation_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_3", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_3",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_3", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_3",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_3", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_3",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_3",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_3",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_4')])
        CD19_mCherry_production_3_net.add_output("BFP_gene", "BFP_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("BFP_mrna", "BFP_gene_transcription_1_3", Value(dot))
        CD19_mCherry_production_3_net.add_output("BFP_protein", "BFP_mrna_translation_1_3", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_6_4')])

        # BFP_production_3_net arcs
        BFP_production_3_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_3", Value(dot))
        BFP_production_3_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_3",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_3",
                                       Value(dot))
        BFP_production_3_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_3",
                                       Value(dot))
        BFP_production_3_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_3", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_3",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_3", Value(dot))
        BFP_production_3_net.add_input("BFP_gene", "BFP_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_3",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_input("BFP_mrna", "BFP_mrna_translation_2_3", Value(dot))
        BFP_production_3_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_3",
                                        Value(dot))
        BFP_production_3_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_3",
                                        Value(dot))
        BFP_production_3_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_3",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_3",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])
        BFP_production_3_net.add_output("BFP_gene", "BFP_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("BFP_mrna", "BFP_gene_transcription_2_3", Value(dot))
        BFP_production_3_net.add_output("BFP_protein", "BFP_mrna_translation_2_3", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_7_3')])

        # CD19_mCherry_production_4_net arcs
        CD19_mCherry_production_4_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_4",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("BFP_gene", "BFP_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("BFP_mrna", "BFP_mrna_translation_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_4", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_4",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_4", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_4",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_4", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_4",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_4",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_4",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_4')])
        CD19_mCherry_production_4_net.add_output("BFP_gene", "BFP_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("BFP_mrna", "BFP_gene_transcription_1_4", Value(dot))
        CD19_mCherry_production_4_net.add_output("BFP_protein", "BFP_mrna_translation_1_4", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_5_4')])

        # BFP_production_4_net arcs
        BFP_production_4_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_4", Value(dot))
        BFP_production_4_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_4",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_4",
                                       Value(dot))
        BFP_production_4_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_4",
                                       Value(dot))
        BFP_production_4_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_4", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_4",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_4", Value(dot))
        BFP_production_4_net.add_input("BFP_gene", "BFP_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_4",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_input("BFP_mrna", "BFP_mrna_translation_2_4", Value(dot))
        BFP_production_4_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_4",
                                        Value(dot))
        BFP_production_4_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_4",
                                        Value(dot))
        BFP_production_4_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_4",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_4",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])
        BFP_production_4_net.add_output("BFP_gene", "BFP_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("BFP_mrna", "BFP_gene_transcription_2_4", Value(dot))
        BFP_production_4_net.add_output("BFP_protein", "BFP_mrna_translation_2_4", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_5_3')])

        # CD19_mCherry_production_5_net arcs
        CD19_mCherry_production_5_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_5",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("BFP_gene", "BFP_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("BFP_mrna", "BFP_mrna_translation_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_5", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_5",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_5", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_5",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_5", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_5",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_5",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_5",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_4')])
        CD19_mCherry_production_5_net.add_output("BFP_gene", "BFP_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("BFP_mrna", "BFP_gene_transcription_1_5", Value(dot))
        CD19_mCherry_production_5_net.add_output("BFP_protein", "BFP_mrna_translation_1_5", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_4')])

        # BFP_production_5_net arcs
        BFP_production_5_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_5", Value(dot))
        BFP_production_5_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_5", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_5", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_5",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_5",
                                       Value(dot))
        BFP_production_5_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_5",
                                       Value(dot))
        BFP_production_5_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_5", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_5", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_5", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_5",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_5", Value(dot))
        BFP_production_5_net.add_input("BFP_gene", "BFP_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_5",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_input("BFP_mrna", "BFP_mrna_translation_2_5", Value(dot))
        BFP_production_5_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_5",
                                        Value(dot))
        BFP_production_5_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_5",
                                        Value(dot))
        BFP_production_5_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_5",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_5",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])
        BFP_production_5_net.add_output("BFP_gene", "BFP_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("BFP_mrna", "BFP_gene_transcription_2_5", Value(dot))
        BFP_production_5_net.add_output("BFP_protein", "BFP_mrna_translation_2_5", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_3')])

        # CD19_mCherry_production_6_net arcs
        CD19_mCherry_production_6_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_6",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("BFP_gene", "BFP_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("BFP_mrna", "BFP_mrna_translation_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_6", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_6",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_6", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_6",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_6", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_6",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_6",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_6",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_5')])
        CD19_mCherry_production_6_net.add_output("BFP_gene", "BFP_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("BFP_mrna", "BFP_gene_transcription_1_6", Value(dot))
        CD19_mCherry_production_6_net.add_output("BFP_protein", "BFP_mrna_translation_1_6", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_5')])

        # BFP_production_6_net arcs
        BFP_production_6_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_6", Value(dot))
        BFP_production_6_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_6", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_6", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_6",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_6",
                                       Value(dot))
        BFP_production_6_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_6",
                                       Value(dot))
        BFP_production_6_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_6", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_6", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_6", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_6",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_6", Value(dot))
        BFP_production_6_net.add_input("BFP_gene", "BFP_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_6",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_input("BFP_mrna", "BFP_mrna_translation_2_6", Value(dot))
        BFP_production_6_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_6",
                                        Value(dot))
        BFP_production_6_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_6",
                                        Value(dot))
        BFP_production_6_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_6",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_6",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])
        BFP_production_6_net.add_output("BFP_gene", "BFP_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("BFP_mrna", "BFP_gene_transcription_2_6", Value(dot))
        BFP_production_6_net.add_output("BFP_protein", "BFP_mrna_translation_2_6", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_5')])

        # CD19_mCherry_production_7_net arcs
        CD19_mCherry_production_7_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_receptor_gene",
                                                "CD19_mCherry_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_receptor_mrna",
                                                "CD19_mCherry_receptor_mrna_translation_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_7",
                                                Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_2_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("GFP_activation_mediator_protein",
                                                "CD19_mCherry_gene_transcription_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("BFP_gene", "BFP_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_activation_mediator_protein",
                                                "BFP_gene_transcription_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("BFP_mrna", "BFP_mrna_translation_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_input("GFP_receptor_active_protein",
                                                "GFP_receptor_active_protein_degradation_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_input("CD19_mCherry_receptor_active_protein",
                                                "CD19_mCherry_receptor_active_protein_degradation_1_7", Value(dot),
                                                notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_7",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_7", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_7",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_receptor_gene",
                                                 "CD19_mCherry_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_receptor_mrna",
                                                 "CD19_mCherry_receptor_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_receptor_protein",
                                                 "CD19_mCherry_receptor_mrna_translation_1_7", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_2_7",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_2_7",
                                                 Value(dot), notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_1_7",
                                                 MultiArc([Value(dot)] * 5),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_6')])
        CD19_mCherry_production_7_net.add_output("BFP_gene", "BFP_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("BFP_mrna", "BFP_gene_transcription_1_7", Value(dot))
        CD19_mCherry_production_7_net.add_output("BFP_protein", "BFP_mrna_translation_1_7", Value(dot),
                                                 notify=[rgb_pattern_net.place('receiver_cell_4_6')])

        # BFP_production_7_net arcs
        BFP_production_7_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_2_7", Value(dot))
        BFP_production_7_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_3_7", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("GFP_receptor_protein", "enzymatic_reaction_3_7", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_2_7",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_7",
                                       Value(dot))
        BFP_production_7_net.add_input("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_mrna_translation_2_7",
                                       Value(dot))
        BFP_production_7_net.add_input("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_7", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("CD19_mCherry_receptor_protein", "enzymatic_reaction_4_7", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("CD19_mCherry_receptor_active_protein",
                                       "CD19_mCherry_receptor_active_protein_degradation_2_7", Value(dot),
                                       notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_input("GFP_activation_mediator_protein", "CD19_mCherry_gene_transcription_2_7",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("CD19_mCherry_mrna", "CD19_mCherry_mrna_translation_2_7", Value(dot))
        BFP_production_7_net.add_input("BFP_gene", "BFP_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_input("CD19_mCherry_activation_mediator_protein", "BFP_gene_transcription_2_7",
                                       Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_input("BFP_mrna", "BFP_mrna_translation_2_7", Value(dot))
        BFP_production_7_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_2_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_3_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_3_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("CD19_mCherry_receptor_gene", "CD19_mCherry_receptor_gene_transcription_2_7",
                                        Value(dot))
        BFP_production_7_net.add_output("CD19_mCherry_receptor_mrna", "CD19_mCherry_receptor_gene_transcription_2_7",
                                        Value(dot))
        BFP_production_7_net.add_output("CD19_mCherry_receptor_protein", "CD19_mCherry_receptor_mrna_translation_2_7",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("CD19_mCherry_receptor_active_protein", "enzymatic_reaction_4_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("CD19_mCherry_activation_mediator_protein", "enzymatic_reaction_4_7",
                                        Value(dot), notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("CD19_mCherry_gene", "CD19_mCherry_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("CD19_mCherry_mrna", "CD19_mCherry_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("CD19_mCherry_protein", "CD19_mCherry_mrna_translation_2_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])
        BFP_production_7_net.add_output("BFP_gene", "BFP_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("BFP_mrna", "BFP_gene_transcription_2_7", Value(dot))
        BFP_production_7_net.add_output("BFP_protein", "BFP_mrna_translation_2_7", Value(dot),
                                        notify=[rgb_pattern_net.place('receiver_cell_3_7')])

        return rgb_pattern_net


if __name__ == "__main__":
    import os
    from petrisim.simulator import *

    test_module = rgb_pattern()
    output_path = os.path.join(".", "results")
    n_steps = 100
    s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
    s.draw_nets(os.path.join(output_path, "../topology"))

    for _ in range(n_steps):
        s.step()

    s.make_charts(exclude=['gene', 'mrna'])
    with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
        print(test_module, file=fp)
