# Generated from project/task11/parser/Graph.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):

    # Enter a parse tree produced by GraphParser#morse_code.
    def enterMorse_code(self, ctx:GraphParser.Morse_codeContext):
        pass

    # Exit a parse tree produced by GraphParser#morse_code.
    def exitMorse_code(self, ctx:GraphParser.Morse_codeContext):
        pass


    # Enter a parse tree produced by GraphParser#letter.
    def enterLetter(self, ctx:GraphParser.LetterContext):
        pass

    # Exit a parse tree produced by GraphParser#letter.
    def exitLetter(self, ctx:GraphParser.LetterContext):
        pass


    # Enter a parse tree produced by GraphParser#digit.
    def enterDigit(self, ctx:GraphParser.DigitContext):
        pass

    # Exit a parse tree produced by GraphParser#digit.
    def exitDigit(self, ctx:GraphParser.DigitContext):
        pass



del GraphParser
