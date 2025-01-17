from infer.infer_utils.types import VariableStore, VariablesPrinter, GraphLangType
from parser.GraphParser import GraphParser
from antlr4 import ParserRuleContext


class GraphLangTyper:
    def __init__(self, graph_lang_tree: ParserRuleContext):
        self.__variables = VariableStore()
        self.__infer_result = True
        self.__infer_error_message = None

        try:
            self.__prog_infer(graph_lang_tree)
        except Exception as ex:
            self.__infer_result = False
            self.__infer_error_message = str(ex)

    def check_result(self) -> bool:
        return self.__infer_result

    def get_error_message(self) -> str:
        if not self.__infer_error_message:
            raise ValueError("Try to get error message when there is no error")

        return self.__infer_error_message

    def print_variables(self):
        VariablesPrinter(self.__variables).print()

    def __prog_infer(self, prog: ParserRuleContext):
        # ctx = prog
        statement = prog.children

        for stmt in statement:
            # traversal of all statements

            stmt_child: ParserRuleContext = stmt.getChild(0)
            stmt_child_index: int = stmt_child.getRuleIndex()

            if stmt_child_index == GraphParser.RULE_bind:
                pass
            elif stmt_child_index == GraphParser.RULE_declare:
                self.__declare_infer(stmt_child)
            elif stmt_child_index == GraphParser.RULE_add:
                self.__add_infer(stmt_child)
            elif stmt_child_index == GraphParser.RULE_remove:
                self.__remove_infer(stmt_child)
            else:
                raise Exception("Can't recognize statement")

    def __bind_infer(self, bind: ParserRuleContext):
        pass

    def __declare_infer(self, declare: ParserRuleContext):
        var_name = declare.getChild(1).getText()
        self.__variables.add_variable(var_name, GraphLangType.GRAPH)

    def __add_infer(self, add: ParserRuleContext):
        assert (
            add.getRuleIndex() == GraphParser.RULE_add
        ), "__add_infer accepts only 'add' type"

        add_type_keyword = add.getChild(1).getText()  # 'edge' | 'vertex'
        added_entity = add.getChild(2)
        var_name = add.getChild(4).getText()

        if not self.__check_var_type(var_name, GraphLangType.GRAPH):
            raise Exception(
                f"Variable {var_name} have to be GRAPH, not {self.__variables.get_variable(var_name)}!"
            )

        if add_type_keyword == "edge":
            if not self.__check_edge_type(added_entity):
                raise Exception(
                    f"Illegal edge construction, it can't be added to {var_name}"
                )
        elif add_type_keyword == "vertex":
            if not self.__check_vertex_type(added_entity):
                raise Exception(
                    f"Illegal vertex construction, it can't be added to {var_name}"
                )
        else:
            raise Exception("Can't recognize add keyword (vertex or edge?)")

    def __remove_infer(self, remove: ParserRuleContext):
        assert (
            remove.getRuleIndex() == GraphParser.RULE_remove
        ), "__add_infer accepts only 'remove' type"

        remove_type_keyword = remove.getChild(1).getText()  # 'edge' | 'vertex'
        removed_entity = remove.getChild(2)
        var_name = remove.getChild(4).getText()

        if not self.__check_var_type(var_name, GraphLangType.GRAPH):
            raise Exception(
                f'Variable "{var_name}" have to be GRAPH, not {self.__variables.get_variable(var_name)}!'
            )

        if remove_type_keyword == "edge":
            if not self.__check_edge_type(removed_entity):
                raise Exception(
                    f"Illegal edge construction, it can't be removed from {var_name}"
                )
        elif remove_type_keyword == "vertex":
            if not self.__check_vertex_type(removed_entity):
                raise Exception(
                    f"Illegal vertex construction, it can't be removed from {var_name}"
                )
        else:
            raise Exception("Can't recognize remove keyword (vertex or edge?)")

    def __check_vertex_type(self, expr: ParserRuleContext) -> bool:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "__check_edge_type accepts only 'expr' type"

        vertex = self.__extract_value_from_expr(expr)

        return self.__check_num_type(vertex)

    def __check_edge_type(self, expr: ParserRuleContext) -> bool:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "__check_edge_type accepts only 'expr' type"

        # (expr (edge_expr ...))
        edge_expr = self.__extract_value_from_expr(expr)
        rule_index = edge_expr.getRuleIndex()

        if rule_index == GraphParser.RULE_edge_expr:
            left_num = self.__extract_value_from_expr(
                edge_expr.getChild(1)
            )  # (expr (num ...))
            char = self.__extract_value_from_expr(edge_expr.getChild(3))
            right_num = self.__extract_value_from_expr(edge_expr.getChild(5))

            edge_check_result = (
                self.__check_num_type(left_num)
                and self.__check_char_type(char)
                and self.__check_num_type(right_num)
            )

            return edge_check_result
        elif rule_index == GraphParser.RULE_var:
            return self.__check_var_type(edge_expr.getText(), GraphLangType.EDGE)
        else:
            return False

    def __check_var_type(self, var_name: str, var_correct_type: GraphLangType) -> bool:
        """Check if variable exists in environment and if it has correct type."""
        if not self.__variables.contains_variable(var_name):
            raise Exception(f'Variable "{var_name}" doesn\'t exist')

        return self.__variables.get_variable(var_name) == var_correct_type

    def __check_num_type(self, num: ParserRuleContext) -> bool:
        rule_index = num.getRuleIndex()

        if rule_index == GraphParser.RULE_num:
            return True
        elif rule_index == GraphParser.RULE_var:
            return self.__check_var_type(num.getText(), GraphLangType.NUM)
        else:
            return False

    def __check_char_type(self, char: ParserRuleContext) -> bool:
        rule_index = char.getRuleIndex()

        if rule_index == GraphParser.RULE_char:
            return True
        elif rule_index == GraphParser.RULE_var:
            return self.__check_var_type(char.getText(), GraphLangType.CHAR)
        else:
            return False

    def __extract_value_from_expr(self, expr: ParserRuleContext) -> ParserRuleContext:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "__extract_value_from_expr got something different from 'expr' type"

        return expr.getChild(0)
