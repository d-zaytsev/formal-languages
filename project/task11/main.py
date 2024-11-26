from antlr4 import *
from parser.GraphLexer import GraphLexer
from parser.GraphParser import GraphParser


input_text = input(": ")
lexer = GraphLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = GraphParser(stream)

tree = parser.morse_code()

print(tree.toStringTree(recog=parser))
