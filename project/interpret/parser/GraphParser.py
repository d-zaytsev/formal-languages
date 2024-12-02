# Generated from project/task11/parser/Graph.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        1,
        31,
        174,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        2,
        4,
        7,
        4,
        2,
        5,
        7,
        5,
        2,
        6,
        7,
        6,
        2,
        7,
        7,
        7,
        2,
        8,
        7,
        8,
        2,
        9,
        7,
        9,
        2,
        10,
        7,
        10,
        2,
        11,
        7,
        11,
        2,
        12,
        7,
        12,
        2,
        13,
        7,
        13,
        2,
        14,
        7,
        14,
        2,
        15,
        7,
        15,
        2,
        16,
        7,
        16,
        2,
        17,
        7,
        17,
        2,
        18,
        7,
        18,
        1,
        0,
        5,
        0,
        40,
        8,
        0,
        10,
        0,
        12,
        0,
        43,
        9,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        49,
        8,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        5,
        1,
        5,
        1,
        5,
        1,
        5,
        1,
        5,
        1,
        5,
        1,
        6,
        1,
        6,
        1,
        6,
        1,
        6,
        1,
        6,
        1,
        6,
        1,
        6,
        3,
        6,
        80,
        8,
        6,
        1,
        7,
        1,
        7,
        1,
        7,
        1,
        7,
        5,
        7,
        86,
        8,
        7,
        10,
        7,
        12,
        7,
        89,
        9,
        7,
        1,
        7,
        1,
        7,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        8,
        1,
        9,
        1,
        9,
        1,
        9,
        5,
        9,
        104,
        8,
        9,
        10,
        9,
        12,
        9,
        107,
        9,
        9,
        1,
        10,
        1,
        10,
        1,
        10,
        5,
        10,
        112,
        8,
        10,
        10,
        10,
        12,
        10,
        115,
        9,
        10,
        1,
        11,
        1,
        11,
        1,
        11,
        5,
        11,
        120,
        8,
        11,
        10,
        11,
        12,
        11,
        123,
        9,
        11,
        1,
        12,
        1,
        12,
        1,
        12,
        1,
        12,
        1,
        12,
        1,
        12,
        3,
        12,
        131,
        8,
        12,
        1,
        13,
        1,
        13,
        1,
        13,
        1,
        13,
        3,
        13,
        137,
        8,
        13,
        1,
        13,
        1,
        13,
        1,
        14,
        3,
        14,
        142,
        8,
        14,
        1,
        14,
        3,
        14,
        145,
        8,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        3,
        14,
        151,
        8,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        14,
        1,
        15,
        1,
        15,
        1,
        15,
        1,
        15,
        1,
        15,
        1,
        16,
        1,
        16,
        1,
        17,
        1,
        17,
        1,
        18,
        1,
        18,
        1,
        18,
        0,
        0,
        19,
        0,
        2,
        4,
        6,
        8,
        10,
        12,
        14,
        16,
        18,
        20,
        22,
        24,
        26,
        28,
        30,
        32,
        34,
        36,
        0,
        3,
        1,
        0,
        9,
        11,
        1,
        0,
        9,
        10,
        1,
        0,
        24,
        25,
        174,
        0,
        41,
        1,
        0,
        0,
        0,
        2,
        48,
        1,
        0,
        0,
        0,
        4,
        50,
        1,
        0,
        0,
        0,
        6,
        55,
        1,
        0,
        0,
        0,
        8,
        60,
        1,
        0,
        0,
        0,
        10,
        66,
        1,
        0,
        0,
        0,
        12,
        79,
        1,
        0,
        0,
        0,
        14,
        81,
        1,
        0,
        0,
        0,
        16,
        92,
        1,
        0,
        0,
        0,
        18,
        100,
        1,
        0,
        0,
        0,
        20,
        108,
        1,
        0,
        0,
        0,
        22,
        116,
        1,
        0,
        0,
        0,
        24,
        130,
        1,
        0,
        0,
        0,
        26,
        132,
        1,
        0,
        0,
        0,
        28,
        141,
        1,
        0,
        0,
        0,
        30,
        162,
        1,
        0,
        0,
        0,
        32,
        167,
        1,
        0,
        0,
        0,
        34,
        169,
        1,
        0,
        0,
        0,
        36,
        171,
        1,
        0,
        0,
        0,
        38,
        40,
        3,
        2,
        1,
        0,
        39,
        38,
        1,
        0,
        0,
        0,
        40,
        43,
        1,
        0,
        0,
        0,
        41,
        39,
        1,
        0,
        0,
        0,
        41,
        42,
        1,
        0,
        0,
        0,
        42,
        1,
        1,
        0,
        0,
        0,
        43,
        41,
        1,
        0,
        0,
        0,
        44,
        49,
        3,
        6,
        3,
        0,
        45,
        49,
        3,
        10,
        5,
        0,
        46,
        49,
        3,
        8,
        4,
        0,
        47,
        49,
        3,
        4,
        2,
        0,
        48,
        44,
        1,
        0,
        0,
        0,
        48,
        45,
        1,
        0,
        0,
        0,
        48,
        46,
        1,
        0,
        0,
        0,
        48,
        47,
        1,
        0,
        0,
        0,
        49,
        3,
        1,
        0,
        0,
        0,
        50,
        51,
        5,
        1,
        0,
        0,
        51,
        52,
        3,
        36,
        18,
        0,
        52,
        53,
        5,
        2,
        0,
        0,
        53,
        54,
        5,
        3,
        0,
        0,
        54,
        5,
        1,
        0,
        0,
        0,
        55,
        56,
        5,
        1,
        0,
        0,
        56,
        57,
        3,
        36,
        18,
        0,
        57,
        58,
        5,
        17,
        0,
        0,
        58,
        59,
        3,
        12,
        6,
        0,
        59,
        7,
        1,
        0,
        0,
        0,
        60,
        61,
        5,
        4,
        0,
        0,
        61,
        62,
        7,
        0,
        0,
        0,
        62,
        63,
        3,
        12,
        6,
        0,
        63,
        64,
        5,
        12,
        0,
        0,
        64,
        65,
        3,
        36,
        18,
        0,
        65,
        9,
        1,
        0,
        0,
        0,
        66,
        67,
        5,
        13,
        0,
        0,
        67,
        68,
        7,
        1,
        0,
        0,
        68,
        69,
        3,
        12,
        6,
        0,
        69,
        70,
        5,
        14,
        0,
        0,
        70,
        71,
        3,
        36,
        18,
        0,
        71,
        11,
        1,
        0,
        0,
        0,
        72,
        80,
        3,
        32,
        16,
        0,
        73,
        80,
        3,
        34,
        17,
        0,
        74,
        80,
        3,
        36,
        18,
        0,
        75,
        80,
        3,
        16,
        8,
        0,
        76,
        80,
        3,
        14,
        7,
        0,
        77,
        80,
        3,
        18,
        9,
        0,
        78,
        80,
        3,
        28,
        14,
        0,
        79,
        72,
        1,
        0,
        0,
        0,
        79,
        73,
        1,
        0,
        0,
        0,
        79,
        74,
        1,
        0,
        0,
        0,
        79,
        75,
        1,
        0,
        0,
        0,
        79,
        76,
        1,
        0,
        0,
        0,
        79,
        77,
        1,
        0,
        0,
        0,
        79,
        78,
        1,
        0,
        0,
        0,
        80,
        13,
        1,
        0,
        0,
        0,
        81,
        82,
        5,
        18,
        0,
        0,
        82,
        87,
        3,
        12,
        6,
        0,
        83,
        84,
        5,
        22,
        0,
        0,
        84,
        86,
        3,
        12,
        6,
        0,
        85,
        83,
        1,
        0,
        0,
        0,
        86,
        89,
        1,
        0,
        0,
        0,
        87,
        85,
        1,
        0,
        0,
        0,
        87,
        88,
        1,
        0,
        0,
        0,
        88,
        90,
        1,
        0,
        0,
        0,
        89,
        87,
        1,
        0,
        0,
        0,
        90,
        91,
        5,
        20,
        0,
        0,
        91,
        15,
        1,
        0,
        0,
        0,
        92,
        93,
        5,
        19,
        0,
        0,
        93,
        94,
        3,
        12,
        6,
        0,
        94,
        95,
        5,
        22,
        0,
        0,
        95,
        96,
        3,
        12,
        6,
        0,
        96,
        97,
        5,
        22,
        0,
        0,
        97,
        98,
        3,
        12,
        6,
        0,
        98,
        99,
        5,
        21,
        0,
        0,
        99,
        17,
        1,
        0,
        0,
        0,
        100,
        105,
        3,
        20,
        10,
        0,
        101,
        102,
        5,
        27,
        0,
        0,
        102,
        104,
        3,
        20,
        10,
        0,
        103,
        101,
        1,
        0,
        0,
        0,
        104,
        107,
        1,
        0,
        0,
        0,
        105,
        103,
        1,
        0,
        0,
        0,
        105,
        106,
        1,
        0,
        0,
        0,
        106,
        19,
        1,
        0,
        0,
        0,
        107,
        105,
        1,
        0,
        0,
        0,
        108,
        113,
        3,
        22,
        11,
        0,
        109,
        110,
        7,
        2,
        0,
        0,
        110,
        112,
        3,
        22,
        11,
        0,
        111,
        109,
        1,
        0,
        0,
        0,
        112,
        115,
        1,
        0,
        0,
        0,
        113,
        111,
        1,
        0,
        0,
        0,
        113,
        114,
        1,
        0,
        0,
        0,
        114,
        21,
        1,
        0,
        0,
        0,
        115,
        113,
        1,
        0,
        0,
        0,
        116,
        121,
        3,
        24,
        12,
        0,
        117,
        118,
        5,
        23,
        0,
        0,
        118,
        120,
        3,
        26,
        13,
        0,
        119,
        117,
        1,
        0,
        0,
        0,
        120,
        123,
        1,
        0,
        0,
        0,
        121,
        119,
        1,
        0,
        0,
        0,
        121,
        122,
        1,
        0,
        0,
        0,
        122,
        23,
        1,
        0,
        0,
        0,
        123,
        121,
        1,
        0,
        0,
        0,
        124,
        131,
        3,
        34,
        17,
        0,
        125,
        131,
        3,
        36,
        18,
        0,
        126,
        127,
        5,
        19,
        0,
        0,
        127,
        128,
        3,
        18,
        9,
        0,
        128,
        129,
        5,
        21,
        0,
        0,
        129,
        131,
        1,
        0,
        0,
        0,
        130,
        124,
        1,
        0,
        0,
        0,
        130,
        125,
        1,
        0,
        0,
        0,
        130,
        126,
        1,
        0,
        0,
        0,
        131,
        25,
        1,
        0,
        0,
        0,
        132,
        133,
        5,
        18,
        0,
        0,
        133,
        134,
        3,
        32,
        16,
        0,
        134,
        136,
        5,
        26,
        0,
        0,
        135,
        137,
        3,
        32,
        16,
        0,
        136,
        135,
        1,
        0,
        0,
        0,
        136,
        137,
        1,
        0,
        0,
        0,
        137,
        138,
        1,
        0,
        0,
        0,
        138,
        139,
        5,
        20,
        0,
        0,
        139,
        27,
        1,
        0,
        0,
        0,
        140,
        142,
        3,
        30,
        15,
        0,
        141,
        140,
        1,
        0,
        0,
        0,
        141,
        142,
        1,
        0,
        0,
        0,
        142,
        144,
        1,
        0,
        0,
        0,
        143,
        145,
        3,
        30,
        15,
        0,
        144,
        143,
        1,
        0,
        0,
        0,
        144,
        145,
        1,
        0,
        0,
        0,
        145,
        146,
        1,
        0,
        0,
        0,
        146,
        147,
        5,
        7,
        0,
        0,
        147,
        150,
        3,
        36,
        18,
        0,
        148,
        149,
        5,
        22,
        0,
        0,
        149,
        151,
        3,
        36,
        18,
        0,
        150,
        148,
        1,
        0,
        0,
        0,
        150,
        151,
        1,
        0,
        0,
        0,
        151,
        152,
        1,
        0,
        0,
        0,
        152,
        153,
        5,
        5,
        0,
        0,
        153,
        154,
        3,
        36,
        18,
        0,
        154,
        155,
        5,
        6,
        0,
        0,
        155,
        156,
        5,
        12,
        0,
        0,
        156,
        157,
        3,
        36,
        18,
        0,
        157,
        158,
        5,
        16,
        0,
        0,
        158,
        159,
        3,
        36,
        18,
        0,
        159,
        160,
        5,
        8,
        0,
        0,
        160,
        161,
        3,
        12,
        6,
        0,
        161,
        29,
        1,
        0,
        0,
        0,
        162,
        163,
        5,
        15,
        0,
        0,
        163,
        164,
        3,
        36,
        18,
        0,
        164,
        165,
        5,
        16,
        0,
        0,
        165,
        166,
        3,
        12,
        6,
        0,
        166,
        31,
        1,
        0,
        0,
        0,
        167,
        168,
        5,
        29,
        0,
        0,
        168,
        33,
        1,
        0,
        0,
        0,
        169,
        170,
        5,
        30,
        0,
        0,
        170,
        35,
        1,
        0,
        0,
        0,
        171,
        172,
        5,
        28,
        0,
        0,
        172,
        37,
        1,
        0,
        0,
        0,
        12,
        41,
        48,
        79,
        87,
        105,
        113,
        121,
        130,
        136,
        141,
        144,
        150,
    ]


class GraphParser(Parser):
    grammarFileName = "Graph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'let'",
        "'is'",
        "'graph'",
        "'remove'",
        "'where'",
        "'reachable'",
        "'return'",
        "'by'",
        "'vertex'",
        "'edge'",
        "'vertices'",
        "'from'",
        "'add'",
        "'to'",
        "'for'",
        "'in'",
        "'='",
        "'['",
        "'('",
        "']'",
        "')'",
        "','",
        "'^'",
        "'.'",
        "'&'",
        "'..'",
        "'|'",
    ]

    symbolicNames = [
        "<INVALID>",
        "LET",
        "IS",
        "GRAPH",
        "REMOVE",
        "WHERE",
        "REACHABLE",
        "RETURN",
        "BY",
        "VERTEX",
        "EDGE",
        "VERTICES",
        "FROM",
        "ADD",
        "TO",
        "FOR",
        "IN",
        "EQUAL",
        "L_SQ_BRACKET",
        "L_PARENTHESIS",
        "R_SQ_BRACKET",
        "R_PARENTHESIS",
        "COMMA",
        "CIRCUMFLEX",
        "DOT",
        "AMPERSAND",
        "ELLIPSIS",
        "PIPE",
        "VAR_ID",
        "NUM",
        "CHAR",
        "WS",
    ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_declare = 2
    RULE_bind = 3
    RULE_remove = 4
    RULE_add = 5
    RULE_expr = 6
    RULE_set_expr = 7
    RULE_edge_expr = 8
    RULE_regexp = 9
    RULE_term = 10
    RULE_factor = 11
    RULE_primary = 12
    RULE_range = 13
    RULE_select = 14
    RULE_v_filter = 15
    RULE_num = 16
    RULE_char = 17
    RULE_var = 18

    ruleNames = [
        "prog",
        "stmt",
        "declare",
        "bind",
        "remove",
        "add",
        "expr",
        "set_expr",
        "edge_expr",
        "regexp",
        "term",
        "factor",
        "primary",
        "range",
        "select",
        "v_filter",
        "num",
        "char",
        "var",
    ]

    EOF = Token.EOF
    LET = 1
    IS = 2
    GRAPH = 3
    REMOVE = 4
    WHERE = 5
    REACHABLE = 6
    RETURN = 7
    BY = 8
    VERTEX = 9
    EDGE = 10
    VERTICES = 11
    FROM = 12
    ADD = 13
    TO = 14
    FOR = 15
    IN = 16
    EQUAL = 17
    L_SQ_BRACKET = 18
    L_PARENTHESIS = 19
    R_SQ_BRACKET = 20
    R_PARENTHESIS = 21
    COMMA = 22
    CIRCUMFLEX = 23
    DOT = 24
    AMPERSAND = 25
    ELLIPSIS = 26
    PIPE = 27
    VAR_ID = 28
    NUM = 29
    CHAR = 30
    WS = 31

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.StmtContext)
            else:
                return self.getTypedRuleContext(GraphParser.StmtContext, i)

        def getRuleIndex(self):
            return GraphParser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

    def prog(self):
        localctx = GraphParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and ((1 << _la) & 8210) != 0:
                self.state = 38
                self.stmt()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bind(self):
            return self.getTypedRuleContext(GraphParser.BindContext, 0)

        def add(self):
            return self.getTypedRuleContext(GraphParser.AddContext, 0)

        def remove(self):
            return self.getTypedRuleContext(GraphParser.RemoveContext, 0)

        def declare(self):
            return self.getTypedRuleContext(GraphParser.DeclareContext, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

    def stmt(self):
        localctx = GraphParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.bind()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.add()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.remove()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.declare()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclareContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GraphParser.LET, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def IS(self):
            return self.getToken(GraphParser.IS, 0)

        def GRAPH(self):
            return self.getToken(GraphParser.GRAPH, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_declare

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclare"):
                listener.enterDeclare(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclare"):
                listener.exitDeclare(self)

    def declare(self):
        localctx = GraphParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(GraphParser.LET)
            self.state = 51
            self.var()
            self.state = 52
            self.match(GraphParser.IS)
            self.state = 53
            self.match(GraphParser.GRAPH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BindContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GraphParser.LET, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def EQUAL(self):
            return self.getToken(GraphParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphParser.ExprContext, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_bind

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBind"):
                listener.enterBind(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBind"):
                listener.exitBind(self)

    def bind(self):
        localctx = GraphParser.BindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GraphParser.LET)
            self.state = 56
            self.var()
            self.state = 57
            self.match(GraphParser.EQUAL)
            self.state = 58
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RemoveContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(GraphParser.REMOVE, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphParser.ExprContext, 0)

        def FROM(self):
            return self.getToken(GraphParser.FROM, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def VERTEX(self):
            return self.getToken(GraphParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(GraphParser.EDGE, 0)

        def VERTICES(self):
            return self.getToken(GraphParser.VERTICES, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_remove

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRemove"):
                listener.enterRemove(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRemove"):
                listener.exitRemove(self)

    def remove(self):
        localctx = GraphParser.RemoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_remove)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(GraphParser.REMOVE)
            self.state = 61
            _la = self._input.LA(1)
            if not (((_la) & ~0x3F) == 0 and ((1 << _la) & 3584) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.expr()
            self.state = 63
            self.match(GraphParser.FROM)
            self.state = 64
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GraphParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphParser.ExprContext, 0)

        def TO(self):
            return self.getToken(GraphParser.TO, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def VERTEX(self):
            return self.getToken(GraphParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(GraphParser.EDGE, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_add

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAdd"):
                listener.enterAdd(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAdd"):
                listener.exitAdd(self)

    def add(self):
        localctx = GraphParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(GraphParser.ADD)
            self.state = 67
            _la = self._input.LA(1)
            if not (_la == 9 or _la == 10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self.expr()
            self.state = 69
            self.match(GraphParser.TO)
            self.state = 70
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(GraphParser.NumContext, 0)

        def char(self):
            return self.getTypedRuleContext(GraphParser.CharContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def edge_expr(self):
            return self.getTypedRuleContext(GraphParser.Edge_exprContext, 0)

        def set_expr(self):
            return self.getTypedRuleContext(GraphParser.Set_exprContext, 0)

        def regexp(self):
            return self.getTypedRuleContext(GraphParser.RegexpContext, 0)

        def select(self):
            return self.getTypedRuleContext(GraphParser.SelectContext, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

    def expr(self):
        localctx = GraphParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.char()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.var()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.edge_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.set_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.regexp()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.select()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_SQ_BRACKET(self):
            return self.getToken(GraphParser.L_SQ_BRACKET, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphParser.ExprContext, i)

        def R_SQ_BRACKET(self):
            return self.getToken(GraphParser.R_SQ_BRACKET, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.COMMA)
            else:
                return self.getToken(GraphParser.COMMA, i)

        def getRuleIndex(self):
            return GraphParser.RULE_set_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSet_expr"):
                listener.enterSet_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSet_expr"):
                listener.exitSet_expr(self)

    def set_expr(self):
        localctx = GraphParser.Set_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_set_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(GraphParser.L_SQ_BRACKET)
            self.state = 82
            self.expr()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 22:
                self.state = 83
                self.match(GraphParser.COMMA)
                self.state = 84
                self.expr()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(GraphParser.R_SQ_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edge_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENTHESIS(self):
            return self.getToken(GraphParser.L_PARENTHESIS, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphParser.ExprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.COMMA)
            else:
                return self.getToken(GraphParser.COMMA, i)

        def R_PARENTHESIS(self):
            return self.getToken(GraphParser.R_PARENTHESIS, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_edge_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdge_expr"):
                listener.enterEdge_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdge_expr"):
                listener.exitEdge_expr(self)

    def edge_expr(self):
        localctx = GraphParser.Edge_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_edge_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(GraphParser.L_PARENTHESIS)
            self.state = 93
            self.expr()
            self.state = 94
            self.match(GraphParser.COMMA)
            self.state = 95
            self.expr()
            self.state = 96
            self.match(GraphParser.COMMA)
            self.state = 97
            self.expr()
            self.state = 98
            self.match(GraphParser.R_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegexpContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.TermContext)
            else:
                return self.getTypedRuleContext(GraphParser.TermContext, i)

        def PIPE(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.PIPE)
            else:
                return self.getToken(GraphParser.PIPE, i)

        def getRuleIndex(self):
            return GraphParser.RULE_regexp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRegexp"):
                listener.enterRegexp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRegexp"):
                listener.exitRegexp(self)

    def regexp(self):
        localctx = GraphParser.RegexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_regexp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.term()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 27:
                self.state = 101
                self.match(GraphParser.PIPE)
                self.state = 102
                self.term()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.FactorContext)
            else:
                return self.getTypedRuleContext(GraphParser.FactorContext, i)

        def DOT(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.DOT)
            else:
                return self.getToken(GraphParser.DOT, i)

        def AMPERSAND(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.AMPERSAND)
            else:
                return self.getToken(GraphParser.AMPERSAND, i)

        def getRuleIndex(self):
            return GraphParser.RULE_term

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)

    def term(self):
        localctx = GraphParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.factor()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 24 or _la == 25:
                self.state = 109
                _la = self._input.LA(1)
                if not (_la == 24 or _la == 25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.factor()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(GraphParser.PrimaryContext, 0)

        def CIRCUMFLEX(self, i: int = None):
            if i is None:
                return self.getTokens(GraphParser.CIRCUMFLEX)
            else:
                return self.getToken(GraphParser.CIRCUMFLEX, i)

        def range_(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.RangeContext)
            else:
                return self.getTypedRuleContext(GraphParser.RangeContext, i)

        def getRuleIndex(self):
            return GraphParser.RULE_factor

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFactor"):
                listener.enterFactor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFactor"):
                listener.exitFactor(self)

    def factor(self):
        localctx = GraphParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.primary()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 23:
                self.state = 117
                self.match(GraphParser.CIRCUMFLEX)
                self.state = 118
                self.range_()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char(self):
            return self.getTypedRuleContext(GraphParser.CharContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def L_PARENTHESIS(self):
            return self.getToken(GraphParser.L_PARENTHESIS, 0)

        def regexp(self):
            return self.getTypedRuleContext(GraphParser.RegexpContext, 0)

        def R_PARENTHESIS(self):
            return self.getToken(GraphParser.R_PARENTHESIS, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_primary

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrimary"):
                listener.enterPrimary(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrimary"):
                listener.exitPrimary(self)

    def primary(self):
        localctx = GraphParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primary)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.char()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.var()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(GraphParser.L_PARENTHESIS)
                self.state = 127
                self.regexp()
                self.state = 128
                self.match(GraphParser.R_PARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_SQ_BRACKET(self):
            return self.getToken(GraphParser.L_SQ_BRACKET, 0)

        def num(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.NumContext)
            else:
                return self.getTypedRuleContext(GraphParser.NumContext, i)

        def ELLIPSIS(self):
            return self.getToken(GraphParser.ELLIPSIS, 0)

        def R_SQ_BRACKET(self):
            return self.getToken(GraphParser.R_SQ_BRACKET, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_range

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRange"):
                listener.enterRange(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRange"):
                listener.exitRange(self)

    def range_(self):
        localctx = GraphParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_range)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(GraphParser.L_SQ_BRACKET)
            self.state = 133
            self.num()
            self.state = 134
            self.match(GraphParser.ELLIPSIS)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 29:
                self.state = 135
                self.num()

            self.state = 138
            self.match(GraphParser.R_SQ_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GraphParser.RETURN, 0)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphParser.VarContext, i)

        def WHERE(self):
            return self.getToken(GraphParser.WHERE, 0)

        def REACHABLE(self):
            return self.getToken(GraphParser.REACHABLE, 0)

        def FROM(self):
            return self.getToken(GraphParser.FROM, 0)

        def IN(self):
            return self.getToken(GraphParser.IN, 0)

        def BY(self):
            return self.getToken(GraphParser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphParser.ExprContext, 0)

        def v_filter(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.V_filterContext)
            else:
                return self.getTypedRuleContext(GraphParser.V_filterContext, i)

        def COMMA(self):
            return self.getToken(GraphParser.COMMA, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_select

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect"):
                listener.enterSelect(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect"):
                listener.exitSelect(self)

    def select(self):
        localctx = GraphParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_select)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 9, self._ctx)
            if la_ == 1:
                self.state = 140
                self.v_filter()

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 15:
                self.state = 143
                self.v_filter()

            self.state = 146
            self.match(GraphParser.RETURN)
            self.state = 147
            self.var()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 22:
                self.state = 148
                self.match(GraphParser.COMMA)
                self.state = 149
                self.var()

            self.state = 152
            self.match(GraphParser.WHERE)
            self.state = 153
            self.var()
            self.state = 154
            self.match(GraphParser.REACHABLE)
            self.state = 155
            self.match(GraphParser.FROM)
            self.state = 156
            self.var()
            self.state = 157
            self.match(GraphParser.IN)
            self.state = 158
            self.var()
            self.state = 159
            self.match(GraphParser.BY)
            self.state = 160
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_filterContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GraphParser.FOR, 0)

        def var(self):
            return self.getTypedRuleContext(GraphParser.VarContext, 0)

        def IN(self):
            return self.getToken(GraphParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphParser.ExprContext, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_v_filter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterV_filter"):
                listener.enterV_filter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitV_filter"):
                listener.exitV_filter(self)

    def v_filter(self):
        localctx = GraphParser.V_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_v_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GraphParser.FOR)
            self.state = 163
            self.var()
            self.state = 164
            self.match(GraphParser.IN)
            self.state = 165
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(GraphParser.NUM, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_num

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNum"):
                listener.enterNum(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNum"):
                listener.exitNum(self)

    def num(self):
        localctx = GraphParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(GraphParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CharContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(GraphParser.CHAR, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_char

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterChar"):
                listener.enterChar(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitChar"):
                listener.exitChar(self)

    def char(self):
        localctx = GraphParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GraphParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_ID(self):
            return self.getToken(GraphParser.VAR_ID, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_var

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar"):
                listener.enterVar(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar"):
                listener.exitVar(self)

    def var(self):
        localctx = GraphParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(GraphParser.VAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
