from antlr4 import (
    CommonTokenStream,
    ParserRuleContext,
    InputStream,
    ParseTreeWalker,
)
from parser.GraphLexer import GraphLexer
from parser.GraphParser import GraphParser
from antlr4.error.ErrorListener import ErrorListener

# from infer.graph_typing import GraphTyping
from utils.listener import NodesCountListener, ProgramTextListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"error while parsing ({line},{column}): {msg}\n")


def program_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    program = program.replace("<EOF>", "EOF")
    error_listener = MyErrorListener()

    lexer = GraphLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphParser(stream)

    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    try:
        tree = parser.prog()

        return (tree, True)
    except Exception as e:
        print(e)

        return (None, False)


def nodes_count(tree: ParserRuleContext) -> int:
    listener = NodesCountListener()
    ParseTreeWalker().walk(listener, tree)

    return listener.nodes_count


def tree_to_program(tree: ParserRuleContext) -> str:
    listener = ProgramTextListener()
    ParseTreeWalker().walk(listener, tree)

    return listener.program_text


def typing_program(program: str) -> bool:
    pass


def exec_program(program: str) -> dict[str, set[tuple]]:
    pass


if __name__ == "__main__":
    while True:
        program = input("-> ")

        if program == "exit":
            break

        lexer = GraphLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = GraphParser(stream)

        tree = parser.prog()
        # typecheck = GraphTyping(tree)

        print()
        print("Length:", nodes_count(tree))
        print("Recovered text:", tree_to_program(tree))
        print("Typechecker: ", True)
        print("---")
        print("Result:", tree.toStringTree(recog=parser))
