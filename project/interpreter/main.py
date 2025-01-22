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
from utils.listeners import NodesCountListener, ProgramTextListener
from typechecker.typechecker import GraphLangTyper
from runner.runner import GraphLangRunner


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
    lexer = GraphLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphParser(stream)

    tree = parser.prog()
    types_visitor = GraphLangTyper()

    try:
        types_visitor.visit(tree)

        return True
    except Exception:
        return False


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

        types_visitor = GraphLangTyper()
        typecheck_result = "Good!"

        runner_visitor = GraphLangRunner()
        runner_error_msg = None

        try:
            types_visitor.visit(tree)
        except Exception as ex:
            typecheck_result = str(ex)

        try:
            runner_visitor.visit(tree)
        except Exception as ex:
            runner_error_msg = str(ex)

        print("Length:", nodes_count(tree))
        print("Recovered text:", tree_to_program(tree))
        print("Typechecker:", typecheck_result)

        print("---")
        print("Parser:", tree.toStringTree(recog=parser))

        print("Runner:", runner_error_msg if runner_error_msg else "")
        if not runner_error_msg:
            runner_visitor.printVariables()

        print("Typecheker:")
        types_visitor.printVariables()
        print()
