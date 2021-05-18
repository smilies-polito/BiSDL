# Generated from /home/lg/PycharmProjects/BiSDL/bisdl/Module.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ModuleParser import ModuleParser
else:
    from ModuleParser import ModuleParser

# This class defines a complete listener for a parse tree produced by ModuleParser.
class ModuleListener(ParseTreeListener):

    # Enter a parse tree produced by ModuleParser#root.
    def enterRoot(self, ctx:ModuleParser.RootContext):
        pass

    # Exit a parse tree produced by ModuleParser#root.
    def exitRoot(self, ctx:ModuleParser.RootContext):
        pass


    # Enter a parse tree produced by ModuleParser#timescale.
    def enterTimescale(self, ctx:ModuleParser.TimescaleContext):
        pass

    # Exit a parse tree produced by ModuleParser#timescale.
    def exitTimescale(self, ctx:ModuleParser.TimescaleContext):
        pass


    # Enter a parse tree produced by ModuleParser#scopes.
    def enterScopes(self, ctx:ModuleParser.ScopesContext):
        pass

    # Exit a parse tree produced by ModuleParser#scopes.
    def exitScopes(self, ctx:ModuleParser.ScopesContext):
        pass


    # Enter a parse tree produced by ModuleParser#scope.
    def enterScope(self, ctx:ModuleParser.ScopeContext):
        pass

    # Exit a parse tree produced by ModuleParser#scope.
    def exitScope(self, ctx:ModuleParser.ScopeContext):
        pass


    # Enter a parse tree produced by ModuleParser#coords.
    def enterCoords(self, ctx:ModuleParser.CoordsContext):
        pass

    # Exit a parse tree produced by ModuleParser#coords.
    def exitCoords(self, ctx:ModuleParser.CoordsContext):
        pass


    # Enter a parse tree produced by ModuleParser#processes.
    def enterProcesses(self, ctx:ModuleParser.ProcessesContext):
        pass

    # Exit a parse tree produced by ModuleParser#processes.
    def exitProcesses(self, ctx:ModuleParser.ProcessesContext):
        pass


    # Enter a parse tree produced by ModuleParser#process.
    def enterProcess(self, ctx:ModuleParser.ProcessContext):
        pass

    # Exit a parse tree produced by ModuleParser#process.
    def exitProcess(self, ctx:ModuleParser.ProcessContext):
        pass


    # Enter a parse tree produced by ModuleParser#process_type.
    def enterProcess_type(self, ctx:ModuleParser.Process_typeContext):
        pass

    # Exit a parse tree produced by ModuleParser#process_type.
    def exitProcess_type(self, ctx:ModuleParser.Process_typeContext):
        pass


    # Enter a parse tree produced by ModuleParser#transcription.
    def enterTranscription(self, ctx:ModuleParser.TranscriptionContext):
        pass

    # Exit a parse tree produced by ModuleParser#transcription.
    def exitTranscription(self, ctx:ModuleParser.TranscriptionContext):
        pass


    # Enter a parse tree produced by ModuleParser#translation.
    def enterTranslation(self, ctx:ModuleParser.TranslationContext):
        pass

    # Exit a parse tree produced by ModuleParser#translation.
    def exitTranslation(self, ctx:ModuleParser.TranslationContext):
        pass


    # Enter a parse tree produced by ModuleParser#degradation.
    def enterDegradation(self, ctx:ModuleParser.DegradationContext):
        pass

    # Exit a parse tree produced by ModuleParser#degradation.
    def exitDegradation(self, ctx:ModuleParser.DegradationContext):
        pass


    # Enter a parse tree produced by ModuleParser#protein_complex_formation.
    def enterProtein_complex_formation(self, ctx:ModuleParser.Protein_complex_formationContext):
        pass

    # Exit a parse tree produced by ModuleParser#protein_complex_formation.
    def exitProtein_complex_formation(self, ctx:ModuleParser.Protein_complex_formationContext):
        pass


    # Enter a parse tree produced by ModuleParser#enzymatic_reaction.
    def enterEnzymatic_reaction(self, ctx:ModuleParser.Enzymatic_reactionContext):
        pass

    # Exit a parse tree produced by ModuleParser#enzymatic_reaction.
    def exitEnzymatic_reaction(self, ctx:ModuleParser.Enzymatic_reactionContext):
        pass


    # Enter a parse tree produced by ModuleParser#custom_process.
    def enterCustom_process(self, ctx:ModuleParser.Custom_processContext):
        pass

    # Exit a parse tree produced by ModuleParser#custom_process.
    def exitCustom_process(self, ctx:ModuleParser.Custom_processContext):
        pass


    # Enter a parse tree produced by ModuleParser#regulation.
    def enterRegulation(self, ctx:ModuleParser.RegulationContext):
        pass

    # Exit a parse tree produced by ModuleParser#regulation.
    def exitRegulation(self, ctx:ModuleParser.RegulationContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_inhibitors.
    def enterType_inhibitors(self, ctx:ModuleParser.Type_inhibitorsContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_inhibitors.
    def exitType_inhibitors(self, ctx:ModuleParser.Type_inhibitorsContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_inducers.
    def enterType_inducers(self, ctx:ModuleParser.Type_inducersContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_inducers.
    def exitType_inducers(self, ctx:ModuleParser.Type_inducersContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_activators.
    def enterType_activators(self, ctx:ModuleParser.Type_activatorsContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_activators.
    def exitType_activators(self, ctx:ModuleParser.Type_activatorsContext):
        pass


    # Enter a parse tree produced by ModuleParser#m_list.
    def enterM_list(self, ctx:ModuleParser.M_listContext):
        pass

    # Exit a parse tree produced by ModuleParser#m_list.
    def exitM_list(self, ctx:ModuleParser.M_listContext):
        pass


    # Enter a parse tree produced by ModuleParser#mult.
    def enterMult(self, ctx:ModuleParser.MultContext):
        pass

    # Exit a parse tree produced by ModuleParser#mult.
    def exitMult(self, ctx:ModuleParser.MultContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_gene.
    def enterType_gene(self, ctx:ModuleParser.Type_geneContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_gene.
    def exitType_gene(self, ctx:ModuleParser.Type_geneContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_mrna.
    def enterType_mrna(self, ctx:ModuleParser.Type_mrnaContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_mrna.
    def exitType_mrna(self, ctx:ModuleParser.Type_mrnaContext):
        pass


    # Enter a parse tree produced by ModuleParser#type_protein.
    def enterType_protein(self, ctx:ModuleParser.Type_proteinContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_protein.
    def exitType_protein(self, ctx:ModuleParser.Type_proteinContext):
        pass


    # Enter a parse tree produced by ModuleParser#paracrine_signals.
    def enterParacrine_signals(self, ctx:ModuleParser.Paracrine_signalsContext):
        pass

    # Exit a parse tree produced by ModuleParser#paracrine_signals.
    def exitParacrine_signals(self, ctx:ModuleParser.Paracrine_signalsContext):
        pass


    # Enter a parse tree produced by ModuleParser#juxtacrine_signal.
    def enterJuxtacrine_signal(self, ctx:ModuleParser.Juxtacrine_signalContext):
        pass

    # Exit a parse tree produced by ModuleParser#juxtacrine_signal.
    def exitJuxtacrine_signal(self, ctx:ModuleParser.Juxtacrine_signalContext):
        pass



del ModuleParser