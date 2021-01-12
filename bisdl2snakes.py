import os
import sys
from pathlib import Path
from antlr4 import *

from gen.ModuleLexer import ModuleLexer
from ModuleListenerImpl import *


class BiSDLCompiler(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """

    def __init__(self, src, dest):  # this method creates the class object.
        self._src = src
        self._dest = dest

    # function used to parse an input file
    def compile(self):
        fin = FileStream(self._src)  # read the first argument as a filestream
        lexer = ModuleLexer(fin)  # call your lexer
        stream = CommonTokenStream(lexer)
        parser = ModuleParser(stream)
        tree = parser.root()  # start from the entry rule for our grammar.

        with open(self._dest, "w") as output:
            model = ModuleListenerImpl()
            walker = ParseTreeWalker()
            walker.walk(model, tree)
            output.write("\n".join(model.buf))


# TODO controllo errori
def main(src, dest=None):
    src_path = Path(src)
    if dest is None:
        dest = os.path.join(src_path.parent, src_path.stem + ".py")
    print(dest)
    compiler = BiSDLCompiler(src, dest)
    compiler.compile()


if __name__ == '__main__':
    main(sys.argv[1])
