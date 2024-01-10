import os
import sys
from pathlib import Path
from antlr4 import *

from bisdl_language.gen.ModuleLexer import ModuleLexer
from bisdl_language.impl.ModuleListener import *


class BiSDLCompiler(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """

    def __init__(self, src, dest):
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
            print(f'Compiled file saved to {self._dest}')

def main(argc, argv):
    if argc < 2:
        help()
    src = argv[1]
    dest = Path(src).stem + ".py"
    if argc > 2:
        if not Path(argv[2]).exists():
            print(f'Destination folder {argv[2]} does not exist.')
            return
        dest = os.path.join(Path(argv[2]), dest)
    else:
        dest = os.path.join(Path(src).parent, dest)
    compiler = BiSDLCompiler(src, dest)
    try:
        compiler.compile()
    except Exception as e:
        raise e



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
