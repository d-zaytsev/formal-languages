from antlr4 import ParseTreeListener, ParserRuleContext


class NodesCountListener(ParseTreeListener):
    def __init__(self):
        super().__init__()

    def enterEveryRule(self, ctx: ParserRuleContext):
        ctx.getRuleIndex()
        pass
