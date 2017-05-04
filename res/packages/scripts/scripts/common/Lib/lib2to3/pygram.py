# 2017.05.04 15:33:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/pygram.py
"""Export the Python grammar and symbols."""
import os
from .pgen2 import token
from .pgen2 import driver
from . import pytree
_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'Grammar.txt')
_PATTERN_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'PatternGrammar.txt')

class Symbols(object):

    def __init__(self, grammar):
        """Initializer.
        
        Creates an attribute for each grammar symbol (nonterminal),
        whose value is the symbol's type (an int >= 256).
        """
        for name, symbol in grammar.symbol2number.iteritems():
            setattr(self, name, symbol)


python_grammar = driver.load_grammar(_GRAMMAR_FILE)
python_symbols = Symbols(python_grammar)
python_grammar_no_print_statement = python_grammar.copy()
del python_grammar_no_print_statement.keywords['print']
pattern_grammar = driver.load_grammar(_PATTERN_GRAMMAR_FILE)
pattern_symbols = Symbols(pattern_grammar)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\pygram.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:08 St�edn� Evropa (letn� �as)
