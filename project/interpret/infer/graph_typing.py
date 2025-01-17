from antlr4 import ParserRuleContext, TerminalNode
from parser.GraphParser import GraphParser


# BasicType = namedtuple("BasicType", ["basic_type"])
# Expr = namedtuple("Expr", ["expr_type"])

EDGE = "Edge"
NUM = "Num"
CHAR = "Char"
GRAPH = "Graph"
FA = "FA"
RSM = "RSM"
SET = "SET"


class GraphTyping:
    def __init__(self, tree: ParserRuleContext):
        if tree.getRuleIndex() != GraphParser.RULE_prog or tree.getChildCount() == 0:
            raise Exception("Can't infer types for an empty program")

        self.__vars: dict[str, dict] = {}
        statements = tree.children

        for stmt in statements:
            # traversal of all statements

            stmt_value: ParserRuleContext = stmt.getChild(0)
            rule_index: int = stmt_value.getRuleIndex()

            if rule_index == GraphParser.RULE_bind:
                # bind rule
                var = stmt_value.getChild(1).getText()
                expr = stmt_value.getChild(3)

                expr_type = self.__infer_expr(expr)
                self.__vars[var] = expr_type

            elif rule_index == GraphParser.RULE_declare:
                # declare rule
                var = stmt_value.getChild(1).getText()
                self.__vars[var] = GRAPH

            # TODO add
            # TODO remove

            else:
                raise Exception("Can't recognize statement")

    def __infer_expr(self, expr: ParserRuleContext):
        # expr : num | char | var | edge_expr | set_expr | regexp | select
        expr_value: ParserRuleContext = expr.getChild(0)

        rule_index = expr_value.getRuleIndex()

        if rule_index in [GraphParser.RULE_num, GraphParser.RULE_char]:
            return self.__infer_basic_type(expr_value)

        elif rule_index == GraphParser.RULE_var:
            return self.__pull_variable(expr_value)

        elif rule_index == GraphParser.RULE_edge_expr:
            return self.__infer_edge_expr(expr_value)

        elif rule_index == GraphParser.RULE_regexp:
            return self.__infer_regexp(expr_value)

        elif rule_index == GraphParser.RULE_set_expr:
            return self.__infer_set_expr(expr_value)

        # TODO select

        else:
            raise Exception(f'Unrecognized expr type "{expr_value.getText()}"')

    def __infer_regexp(self, regexpr: ParserRuleContext):
        # CHAR | VAR | '(' regexp ')' | (regexp '|' regexp) | (regexp '^' range) | (regexp '.' regexp) | (regexp '&' regexp)
        term_recursion = []  # is term RSM or not

        for term_i in range(regexpr.getChildCount()):
            term = regexpr.getChild(term_i)

            factor_recursion = []
            current_op = None
            for factor in term.children:
                if isinstance(factor, TerminalNode):
                    current_op = factor.getText()
                    continue

                primary_recursion = False
                for primary_i in range(factor.getChildCount()):
                    primary = factor.getChild(primary_i)

                    if isinstance(primary, ParserRuleContext):
                        primary_value = primary.getChild(0)
                        rule = primary_value.getRuleIndex()

                        if rule == GraphParser.RULE_var:
                            var = primary_value

                            if var not in self.__vars:
                                primary_recursion = True
                            else:
                                var_type = self.__pull_variable(var)
                                if var_type != CHAR:
                                    raise Exception(
                                        f'Incorrect variable usage in regexpr: "{var}"'
                                    )

                factor_recursion.append(primary_recursion)

                # if we determine second argument
                if current_op:
                    if current_op == "&":
                        # intersection
                        if all(factor_recursion):
                            raise Exception("You can't intersect two RSMs :((")
                        term_recursion.append(any(factor_recursion))
                    elif current_op == ".":
                        # concat
                        term_recursion.append(any(factor_recursion))
                    else:
                        raise Exception(f'Illegal regexpr operation: "{current_op}"')

        if any(term_recursion):
            return RSM
        else:
            return FA

    def __infer_set_expr(self, set_expr: ParserRuleContext):
        element_id = 1
        child_count = set_expr.getChildCount()

        while element_id < child_count:
            el = set_expr.getChild(element_id)
            el_type = self.__infer_basic_type(el.getChild(0))

            if el_type != NUM:
                raise Exception(
                    f'Set element can\'t be "{el_type}", it should be "{NUM}"'
                )

            element_id += 2

        return SET

    def __infer_edge_expr(self, edge_expr: ParserRuleContext):
        edge1_expr: ParserRuleContext = edge_expr.getChild(1)
        label_expr: ParserRuleContext = edge_expr.getChild(3)
        edge2_expr: ParserRuleContext = edge_expr.getChild(5)

        # get types
        edge1 = self.__infer_basic_type(edge1_expr.getChild(0))
        label = self.__infer_basic_type(label_expr.getChild(0))
        edge2 = self.__infer_basic_type(edge2_expr.getChild(0))

        # check types
        if edge1 != NUM:
            raise Exception(
                f'Can\'t use type "{edge1}" as first node in "{edge_expr.getText()}"'
            )
        if label != CHAR:
            raise Exception(
                f'Can\'t use type "{label}" as label in "{edge_expr.getText()}"'
            )
        if edge2 != NUM:
            raise Exception(
                f'Can\'t use type "{edge2}" as second node in "{edge_expr.getText()}"'
            )

        return EDGE

    def __pull_variable(self, value: ParserRuleContext):
        """Find and return variable from dict"""
        var: str = value.getText()

        if var in self.__vars:
            return self.__vars[var]
        else:
            raise Exception(f'Unknown variable "{var}"')

    def __infer_basic_type(self, value: ParserRuleContext):
        """Convert CHAR|NUM|VAR to types Char|Num|<Var type>"""
        rule = value.getRuleIndex()
        child = value.children[0]

        if not isinstance(child, TerminalNode):
            raise Exception(
                f'Incorrect basic type: "{value.getText()}" (can\'t find terminal node)'
            )

        if rule == GraphParser.RULE_char:
            return CHAR
        elif rule == GraphParser.RULE_num:
            return NUM
        elif rule == GraphParser.RULE_var:
            return self.__pull_variable(value)
        else:
            raise Exception(f'Unrecognized basic type: "{value.getText()}"')
