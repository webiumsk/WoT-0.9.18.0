# 2017.05.04 15:31:15 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/compiler/__init__.py
"""Package for parsing and compiling Python source code

There are several functions defined at the top level that are imported
from modules contained in the package.

parse(buf, mode="exec") -> AST
    Converts a string containing Python source code to an abstract
    syntax tree (AST).  The AST is defined in compiler.ast.

parseFile(path) -> AST
    The same as parse(open(path))

walk(ast, visitor, verbose=None)
    Does a pre-order walk over the ast using the visitor instance.
    See compiler.visitor for details.

compile(source, filename, mode, flags=None, dont_inherit=None)
    Returns a code object.  A replacement for the builtin compile() function.

compileFile(filename)
    Generates a .pyc file by compiling filename.
"""
import warnings
warnings.warn('The compiler package is deprecated and removed in Python 3.x.', DeprecationWarning, stacklevel=2)
from compiler.transformer import parse, parseFile
from compiler.visitor import walk
from compiler.pycodegen import compile, compileFile
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\compiler\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:15 St�edn� Evropa (letn� �as)
