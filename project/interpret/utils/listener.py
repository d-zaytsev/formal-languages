from antlr4 import ParseTreeListener, TerminalNode

# https://www.antlr.org/api/Java/org/antlr/v4/runtime/tree/ParseTreeListener.html


class NodesCountListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def visitTerminal(self, node: TerminalNode):
        self.__count += 1

    @property
    def nodes_count(self):
        return self.__count


class ProgramTextListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.__terminals_text = []

    def visitTerminal(self, node: TerminalNode):
        self.__terminals_text.append(node.getText())

    @property
    def program_text(self):
        return " ".join(self.__terminals_text)
