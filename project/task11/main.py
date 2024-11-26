from antlr4 import *
from parser.GraphLexer import GraphLexer
from parser.GraphParser import GraphParser

def program_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    try:
        lexer = GraphLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = GraphParser(stream)

        return (parser.prog(), True)
    except Exception:
        return (None, False)

def nodes_count(tree: ParserRuleContext) -> int:
    count = 1
    for child in tree.children:
        if isinstance(child, ParserRuleContext):
            count += nodes_count(child)
    return count


def tree_to_program(tree: ParserRuleContext) -> str:
    result = ""
    for child in tree.children:
        if isinstance(child, TerminalNode):
            result += child.getText() + " "
        elif isinstance(child, ParserRuleContext):
            result += tree_to_program(child)
    return result


if __name__ == '__main__':
    program = input("-> ")
    lexer = GraphLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphParser(stream)

    tree = parser.prog()

    print('Length:', nodes_count(tree))
    print('Result:', tree.toStringTree(recog=parser))
    print('Recovered text:', tree_to_program(tree))
