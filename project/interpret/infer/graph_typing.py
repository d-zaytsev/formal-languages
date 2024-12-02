from antlr4 import ParserRuleContext, TerminalNode
from parser.GraphParser import GraphParser
from collections import namedtuple


Char = namedtuple("Char", ["value"])
Num = namedtuple("Num", ["value"])
Var = namedtuple("Var", ["value"])

BasicType = namedtuple("BasicType", ["basic_type"])
Expr = namedtuple("Expr", ["expr_type"])
EdgeExpr = namedtuple("EdgeExpr", ["edge1", "label", "edge2"])

GraphType = "Graph"


class GraphTyping:
    def __init__(self, tree: ParserRuleContext):
        if tree.getRuleIndex() != GraphParser.RULE_prog or tree.getChildCount() == 0:
            raise Exception("Can't infer types for an empty program")

        self.__vars: dict[str, dict] = {}
        statements = tree.children

        for stmt in statements:
            # traversal of all statements

            if (
                isinstance(stmt, ParserRuleContext)
                and stmt.getRuleIndex() == GraphParser.RULE_stmt
            ):
                stmt_value: ParserRuleContext = stmt.getChild(0)
                rule_index = stmt_value.getRuleIndex()

                if rule_index == GraphParser.RULE_bind:
                    # bind rule
                    var = stmt_value.getChild(1).getText()
                    expr = stmt_value.getChild(3)

                    expr_type = self.__infer_expr(expr)
                    self.__vars[var] = expr_type

                elif rule_index == GraphParser.RULE_declare:
                    var = stmt_value.getChild(1)
                    self.__vars[var] = GraphType

            else:
                raise Exception(
                    "Can't find statement in the position where it should be"
                )

            print()
            for key in self.__vars.keys():
                print(f"{key} => {self.__vars[key]}")

    def __infer_expr(self, expr: ParserRuleContext):
        # expr : num | char | var | edge_expr | set_expr | regexp | select
        expr_value: ParserRuleContext = expr.getChild(0)

        rule_index = expr_value.getRuleIndex()

        if rule_index in [GraphParser.RULE_num, GraphParser.RULE_char]:
            return Expr(self.__infer_basic_types(expr_value))

        elif rule_index == GraphParser.RULE_var:
            return self.__infer_var_type(expr_value)

        elif rule_index == GraphParser.RULE_edge_expr:
            return Expr(self.__infer_edge_expr(expr_value))

        else:
            raise Exception(f'Unrecognized expr type "{expr_value.getText()}"')

    def __infer_edge_expr(self, edge_expr: ParserRuleContext):
        edge1_expr: ParserRuleContext = edge_expr.getChild(1)
        label_expr: ParserRuleContext = edge_expr.getChild(3)
        edge2_expr: ParserRuleContext = edge_expr.getChild(5)

        edge1 = self.__edge_to_int(edge1_expr.getChild(0))
        edge2 = self.__edge_to_int(edge2_expr.getChild(0))

        return EdgeExpr(edge1, label_expr, edge2)

    def __edge_to_int(self, edge: ParserRuleContext) -> bool:
        ruleIndex = edge.getRuleIndex()

        if ruleIndex == GraphParser.RULE_num:
            return int(edge.getText())
        elif ruleIndex == GraphParser.RULE_var:
            var = edge.getText()

            if var in self.__vars:
                return int(self.__vars[var].expr_type.basic_type.value)
            else:
                raise Exception(f'Can\'f find variable "{var}" during edge checking')
        else:
            raise Exception(f'Incorrect edge "{edge.getText()}"')

    def __infer_var_type(self, value: ParserRuleContext) -> BasicType:
        var: str = value.getText()

        if var in self.__vars:
            return self.__vars[var]
        else:
            raise Exception(f'Unknown variable "{var}"')

    def __infer_basic_types(self, value: ParserRuleContext) -> BasicType:
        rule = value.getRuleIndex()
        child = value.children[0]

        if not isinstance(child, TerminalNode):
            raise Exception(
                f'Incorrect basic type: "{value.getText()}" (can\'t find terminal node)'
            )

        text = child.getText()

        if rule == GraphParser.RULE_char:
            return BasicType(Char(text))
        elif rule == GraphParser.RULE_num:
            return BasicType(Num(int(text)))
        else:
            raise Exception(f'Unrecognized basic type: "{value.getText()}"')
