from collections import defaultdict

from bisdl.gen.ModuleParser import ModuleParser
from bisdl.gen.ModuleListener import ModuleListener

#tree = lambda: defaultdict(tree)

class Scope:
    def __init__(self, name: str, coords: (int, int)):
        self.name = name
        self.coords = coords
        self.processes = dict()  # future reti, da leggere dagli oggetti Process e rinominare se necessario

    def __str__(self):
        pass


# il process non ha un tipo, perché è fatto di più parti!!!!!!
class Process:
    def __init__(self, name: str):
        self.name = name
        self.timescale = None
        self.type = None
        self.params = defaultdict()

    def __str__(self):
        if type == ProcessType.TRANSCRIPTION:
            pass
        elif type == ProcessType.TRANSLATION:
            pass
        elif type == ProcessType.DEGRADATION:
            pass
        elif type == ProcessType.PROTEIN_COMPLEX_FORMATION:
            pass
        elif type == ProcessType.ENZYMATIC_REACTION:
            pass
        else:
            pass
            #raise Exception(f'Process type {type} unknown')
        return f'{self.name} {self.timescale} {self.type}'


# This class defines a complete listener for a parse tree produced by ModuleParser.
class ModuleListenerImpl(ModuleListener):

    def __init__(self):
        super().__init__()
        self.__curr_scope = None
        self.__curr_processes = None

    # Enter a parse tree produced by ModuleParser#root.
    def enterRoot(self, ctx: ModuleParser.RootContext):
        pass

    # Exit a parse tree produced by ModuleParser#root.
    def exitRoot(self, ctx: ModuleParser.RootContext):
        #for p in self._processes:
        #    print(p)
        for _p_name, _p in self._processes.items():
            print(_p_name, _p)

    # Enter a parse tree produced by ModuleParser#timescale.
    def enterTimescale(self, ctx: ModuleParser.TimescaleContext):
        self.__timescale = ctx.INT().getText()

    # Exit a parse tree produced by ModuleParser#timescale.
    def exitTimescale(self, ctx: ModuleParser.TimescaleContext):
        pass

    # Enter a parse tree produced by ModuleParser#scopes.
    def enterScopes(self, ctx: ModuleParser.ScopesContext):
        self._scopes = dict()


    # Exit a parse tree produced by ModuleParser#scopes.
    def exitScopes(self, ctx: ModuleParser.ScopesContext):
        pass

    # Enter a parse tree produced by ModuleParser#scope.
    def enterScope(self, ctx: ModuleParser.ScopeContext):
        # print("uno", ctx.ID().getText())
        self.__curr_scope = ctx.ID().getText()

    # Exit a parse tree produced by ModuleParser#scope.
    def exitScope(self, ctx: ModuleParser.ScopeContext):
        # print("quattro", ctx.ID().getText())
        _scope_coords = tuple(int(x) for x in ctx.coords().getText().strip('()').split(","))
        _s = Scope(self.__curr_scope, _scope_coords)
        _s.processes = self.__processes[self.__curr_scope.name]
        self._scopes[_s.name] = _s

    # Enter a parse tree produced by ModuleParser#coords.
    def enterCoords(self, ctx: ModuleParser.CoordsContext):
        # print("due")
        pass

    # Exit a parse tree produced by ModuleParser#coords.
    def exitCoords(self, ctx: ModuleParser.CoordsContext):
        # print("tre")
        pass

    # Enter a parse tree produced by ModuleParser#processes.
    def enterProcesses(self, ctx: ModuleParser.ProcessesContext):
        #self._processes = defaultdict(Process)
        pass

    # Exit a parse tree produced by ModuleParser#processes.
    def exitProcesses(self, ctx: ModuleParser.ProcessesContext):
        print(self._processes)

    # Enter a parse tree produced by ModuleParser#process.
    def enterProcess(self, ctx: ModuleParser.ProcessContext):
        self.__proc = Process(ctx.ID().getText())

    # Exit a parse tree produced by ModuleParser#process.
    def exitProcess(self, ctx: ModuleParser.ProcessContext):
        self.__proc.timescale = self.__timescale
        self.__curr_processes[self.__proc.name] = self.__proc

    # Enter a parse tree produced by ModuleParser#transcription.
    def enterTranscription(self, ctx: ModuleParser.TranscriptionContext):
        self.__proc.type = ProcessType.TRANSCRIPTION.name

    # Exit a parse tree produced by ModuleParser#transcription.
    def exitTranscription(self, ctx: ModuleParser.TranscriptionContext):
        pass

    # Enter a parse tree produced by ModuleParser#translation.
    def enterTranslation(self, ctx: ModuleParser.TranslationContext):
        self.__proc.type = ProcessType.TRANSLATION.name

    # Exit a parse tree produced by ModuleParser#translation.
    def exitTranslation(self, ctx: ModuleParser.TranslationContext):
        pass

    # Enter a parse tree produced by ModuleParser#degradation.
    def enterDegradation(self, ctx: ModuleParser.DegradationContext):
        self.__proc.type = ProcessType.DEGRADATION.name

    # Exit a parse tree produced by ModuleParser#degradation.
    def exitDegradation(self, ctx: ModuleParser.DegradationContext):
        pass

    # Enter a parse tree produced by ModuleParser#protein_complex_formation.
    def enterProtein_complex_formation(self, ctx: ModuleParser.Protein_complex_formationContext):
        self.__proc.type = ProcessType.PROTEIN_COMPLEX_FORMATION.name

    # Exit a parse tree produced by ModuleParser#protein_complex_formation.
    def exitProtein_complex_formation(self, ctx: ModuleParser.Protein_complex_formationContext):
        pass

    # Enter a parse tree produced by ModuleParser#enzymatic_reaction.
    def enterEnzymatic_reaction(self, ctx: ModuleParser.Enzymatic_reactionContext):
        self.__proc.type = ProcessType.ENZYMATIC_REACTION.name

    # Exit a parse tree produced by ModuleParser#enzymatic_reaction.
    def exitEnzymatic_reaction(self, ctx: ModuleParser.Enzymatic_reactionContext):
        pass

    # Enter a parse tree produced by ModuleParser#custom_process.
    def enterCustom_process(self, ctx: ModuleParser.Custom_processContext):
        pass

    # Exit a parse tree produced by ModuleParser#custom_process.
    def exitCustom_process(self, ctx: ModuleParser.Custom_processContext):
        pass

    # Enter a parse tree produced by ModuleParser#regulation.
    def enterRegulation(self, ctx: ModuleParser.RegulationContext):
        pass

    # Exit a parse tree produced by ModuleParser#regulation.
    def exitRegulation(self, ctx: ModuleParser.RegulationContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_inhibitors.
    def enterType_inhibitors(self, ctx: ModuleParser.Type_inhibitorsContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_inhibitors.
    def exitType_inhibitors(self, ctx: ModuleParser.Type_inhibitorsContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_inducers.
    def enterType_inducers(self, ctx: ModuleParser.Type_inducersContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_inducers.
    def exitType_inducers(self, ctx: ModuleParser.Type_inducersContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_activators.
    def enterType_activators(self, ctx: ModuleParser.Type_activatorsContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_activators.
    def exitType_activators(self, ctx: ModuleParser.Type_activatorsContext):
        pass

    # Enter a parse tree produced by ModuleParser#m_list.
    def enterM_list(self, ctx: ModuleParser.M_listContext):
        pass

    # Exit a parse tree produced by ModuleParser#m_list.
    def exitM_list(self, ctx: ModuleParser.M_listContext):
        pass

    # Enter a parse tree produced by ModuleParser#mult.
    def enterMult(self, ctx: ModuleParser.MultContext):
        pass

    # Exit a parse tree produced by ModuleParser#mult.
    def exitMult(self, ctx: ModuleParser.MultContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_gene.
    def enterType_gene(self, ctx: ModuleParser.Type_geneContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_gene.
    def exitType_gene(self, ctx: ModuleParser.Type_geneContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_mrna.
    def enterType_mrna(self, ctx: ModuleParser.Type_mrnaContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_mrna.
    def exitType_mrna(self, ctx: ModuleParser.Type_mrnaContext):
        pass

    # Enter a parse tree produced by ModuleParser#type_protein.
    def enterType_protein(self, ctx: ModuleParser.Type_proteinContext):
        pass

    # Exit a parse tree produced by ModuleParser#type_protein.
    def exitType_protein(self, ctx: ModuleParser.Type_proteinContext):
        pass

    # Enter a parse tree produced by ModuleParser#paracrine_signals.
    def enterParacrine_signals(self, ctx: ModuleParser.Paracrine_signalsContext):
        pass

    # Exit a parse tree produced by ModuleParser#paracrine_signals.
    def exitParacrine_signals(self, ctx: ModuleParser.Paracrine_signalsContext):
        pass

    # Enter a parse tree produced by ModuleParser#juxtacrine_signal.
    def enterJuxtacrine_signal(self, ctx: ModuleParser.Juxtacrine_signalContext):
        pass

    # Exit a parse tree produced by ModuleParser#juxtacrine_signal.
    def exitJuxtacrine_signal(self, ctx: ModuleParser.Juxtacrine_signalContext):
        pass


from enum import Enum


class AdvEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_name_value(cls):
        return list(map(lambda c: (c.name, c.value), cls))


class ProcessType(AdvEnum):
    TRANSCRIPTION = "TRANSCRIPTION"
    TRANSLATION = "TRANSLATION"
    DEGRADATION = "DEGRADATION"
    PROTEIN_COMPLEX_FORMATION = "PROTEIN_COMPLEX_FORMATION"
    ENZYMATIC_REACTION = "ENZYMATIC_REACTION"

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return super.__eq__(self, other)

    def __hash__(self):
        return super().__hash__()
