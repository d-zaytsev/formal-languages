from infer.infer_utils.types import VariableStore, VariablesPrinter, GraphLangType
from parser.GraphParser import GraphParser
from antlr4 import ParserRuleContext


class GraphLangTyper:
    def __init__(self, graph_lang_tree: ParserRuleContext):
        self.__variables = VariableStore()
        self.__infer_result = True
        self.__infer_error_message = None

        try:
            self.__program_infer(graph_lang_tree)
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

    def __program_infer(self, prog: ParserRuleContext):
        # ctx = prog
        statement = prog.children

        for stmt in statement:
            # traversal of all statements

            stmt_child: ParserRuleContext = stmt.getChild(0)
            stmt_child_index: int = stmt_child.getRuleIndex()

            if stmt_child_index == GraphParser.RULE_bind:
                self.__bind_stmt_infer(stmt_child)
            elif stmt_child_index == GraphParser.RULE_declare:
                self.__declare_stmt_infer(stmt_child)
            elif stmt_child_index == GraphParser.RULE_add:
                self.__add_stmt_infer(stmt_child)
            elif stmt_child_index == GraphParser.RULE_remove:
                self.__remove_stmt_infer(stmt_child)
            else:
                raise Exception(f"Can't recognize statement {stmt_child.getText()}")

    def __bind_stmt_infer(self, bind: ParserRuleContext):
        assert (
            bind.getRuleIndex() == GraphParser.RULE_bind
        ), "bind infer accepts only 'bind' rule"

        var_name: str = bind.getChild(1).getText()
        bind_expr = bind.getChild(3)
        bind_expr_type = self.__get_expr_type(bind_expr)

        self.__variables.add_variable(var_name, bind_expr_type)

    def __declare_stmt_infer(self, declare: ParserRuleContext):
        var_name = declare.getChild(1).getText()

        self.__variables.add_variable(var_name, GraphLangType.GRAPH)

    def __add_stmt_infer(self, add: ParserRuleContext):
        assert (
            add.getRuleIndex() == GraphParser.RULE_add
        ), "add infer accepts only 'add' rule"

        add_type_keyword = add.getChild(1).getText()  # 'edge' | 'vertex'
        added_entity = add.getChild(2)
        added_entity_type = self.__get_expr_type(added_entity)
        var_name = add.getChild(4).getText()

        if not self.__check_var_type(var_name, GraphLangType.GRAPH):
            raise Exception(
                f"Variable '{var_name}' have to be GRAPH, not '{self.__variables.get_variable(var_name)}'!"
            )

        if add_type_keyword == "edge":
            if added_entity_type != GraphLangType.EDGE:
                raise Exception(
                    f"Illegal edge construction, it can't be added to '{var_name}'"
                )
        elif add_type_keyword == "vertex":
            if added_entity_type != GraphLangType.NUM:
                raise Exception(
                    f"Illegal vertex construction, it can't be added to '{var_name}'"
                )
        else:
            raise Exception("Can't recognize add keyword (vertex or edge?)")

    def __remove_stmt_infer(self, remove: ParserRuleContext):
        assert (
            remove.getRuleIndex() == GraphParser.RULE_remove
        ), "remove infer accepts only 'remove' rule"

        remove_type_keyword = remove.getChild(
            1
        ).getText()  # 'edge' | 'vertex' | 'vertices'
        removed_entity = remove.getChild(2)
        removed_entity_type = self.__get_expr_type(removed_entity)
        var_name = remove.getChild(4).getText()

        if not self.__check_var_type(var_name, GraphLangType.GRAPH):
            raise Exception(
                f'Variable "{var_name}" have to be GRAPH, not {self.__variables.get_variable(var_name)}!'
            )

        if remove_type_keyword == "edge":
            if removed_entity_type != GraphLangType.EDGE:
                raise Exception(
                    f"Illegal edge construction ({removed_entity.getText()}) , it can't be removed from '{var_name}'"
                )
        elif remove_type_keyword == "vertex":
            if removed_entity_type != GraphLangType.NUM:
                raise Exception(
                    f"Illegal vertex construction ({removed_entity.getText()}), it can't be removed from '{var_name}'"
                )
        elif remove_type_keyword == "vertices":
            if removed_entity_type != GraphLangType.SET:
                raise Exception(
                    f"Illegal vertices construction ({removed_entity.getText()}), it can't be removed from '{var_name}'"
                )
        else:
            raise Exception(f"Can't recognize remove keyword: {remove_type_keyword}")

    def __get_expr_type(self, expr: ParserRuleContext) -> GraphLangType:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), f"get_expr_type accepts only 'expr' rule, not '{expr.getText()}'."

        expr_value = self.__extract_value_from_expr(expr)
        expr_value_index = expr_value.getRuleIndex()

        if expr_value_index == GraphParser.RULE_num:
            return GraphLangType.NUM

        elif expr_value_index == GraphParser.RULE_char:
            return GraphLangType.CHAR

        elif expr_value_index == GraphParser.RULE_var:
            var_name = expr_value.getText()
            return self.__variables.get_variable(var_name)

        elif expr_value_index == GraphParser.RULE_edge_expr:
            edge_check_result = self.__check_edge_type(expr)

            if not edge_check_result:
                raise Exception(f"Incorrect edge construction: {expr_value.getText()}")
            return GraphLangType.EDGE

        elif expr_value_index == GraphParser.RULE_set_expr:
            set_expr_check_result = self.__check_setexpr_type(expr)

            if not set_expr_check_result:
                raise Exception(
                    f"Incorrect set expr construction: {expr_value.getText()}"
                )

            return GraphLangType.SET

        elif expr_value_index == GraphParser.RULE_regexp:
            return self.__get_regexp_type(expr_value)

        else:
            raise f"Can't recognize rule: {expr_value.getText()}"

    def __get_regexp_type(self, regexp: ParserRuleContext) -> GraphLangType:
        assert (
            regexp.getRuleIndex() == GraphParser.RULE_regexp
        ), "get_regexp_type accepts only 'expr' rule"

        child_count = regexp.getChildCount()
        # 🙂🙂🙂
        if child_count == 1:  # CHAR | VAR_ID
            regexp_value = regexp.getChild(0)
            regexp_value_index = regexp.getChild(0).getRuleIndex()

            if regexp_value_index == GraphParser.RULE_char:
                return GraphLangType.FA
            elif regexp_value_index == GraphParser.RULE_var:
                var_name = regexp_value.getText()

                if not self.__variables.contains_variable(var_name):
                    return GraphLangType.RSM
                elif self.__check_var_type(
                    var_name, GraphLangType.CHAR
                ) or self.__check_var_type(var_name, GraphLangType.FA):
                    return GraphLangType.FA
                elif self.__check_var_type(var_name, GraphLangType.RSM):
                    return GraphLangType.RSM
                else:
                    raise Exception(
                        f"Illegal variable's type occured in regexp: '{var_name}'"
                    )
            else:
                raise Exception(f"Can't recognize regexp: '{regexp_value.getText()}'")

        elif (
            child_count == 3
            and regexp.getChild(0).getText() == "("
            and regexp.getChild(2).getText() == ")"
        ):
            regexp_in_brackets = regexp.getChild(1)
            return self.__get_regexp_type(regexp_in_brackets)

        elif child_count == 3:
            operator: str = regexp.getChild(1).getText()

            if operator == "^":
                left_regexp, right_range_exp = regexp.getChild(0), regexp.getChild(2)

                left_regexp_type = self.__get_regexp_type(left_regexp)

                if right_range_exp.getRuleIndex() != GraphParser.RULE_range:
                    raise f"Type with {right_range_exp} index can't be used in Repeat (^) operation."

                if left_regexp_type == GraphLangType.FA:
                    return GraphLangType.FA
                elif left_regexp_type == GraphLangType.RSM:
                    return GraphLangType.RSM
                else:
                    raise f"Type {left_regexp_type} can't be in Repeat (^) operation."

            else:
                left_regexp, right_regexp = regexp.getChild(0), regexp.getChild(2)

                left_regexp_type, right_regexp_type = (
                    self.__get_regexp_type(left_regexp),
                    self.__get_regexp_type(right_regexp),
                )

                if operator in ["|", "."]:
                    return (
                        GraphLangType.RSM
                        if left_regexp_type == GraphLangType.RSM
                        or right_regexp_type == GraphLangType.RSM
                        else GraphLangType.FA
                    )
                elif operator == "&":
                    if (
                        left_regexp_type == GraphLangType.RSM
                        and right_regexp_type == GraphLangType.RSM
                    ):
                        raise Exception(
                            f'Can\'t intersect two RSMs: "{regexp.getText()}".'
                        )

                    return (
                        GraphLangType.RSM
                        if left_regexp_type == GraphLangType.RSM
                        or right_regexp_type == GraphLangType.RSM
                        else GraphLangType.FA
                    )

        else:
            raise Exception("Can't recognize regexp type")

        return GraphLangType.UNKNOWN

    def __check_setexpr_type(self, expr: ParserRuleContext) -> bool:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "check_set_expr_type accepts only 'expr' rule"

        # 🐈🐈🐈
        set_expr = self.__extract_value_from_expr(expr)
        rule_index = set_expr.getRuleIndex()

        if rule_index == GraphParser.RULE_set_expr:
            first_num_id = 1
            last_num_id = set_expr.getChildCount() - 1

            for child_id in range(first_num_id, last_num_id):
                child = set_expr.getChild(child_id)

                if child.getText() == ",":
                    continue

                if self.__get_expr_type(child) != GraphLangType.NUM:
                    return False

            return True
        else:
            return False

    def __check_edge_type(self, expr: ParserRuleContext) -> bool:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "check_edge_type accepts only 'expr' rule"

        # 🐈🐈🐈
        edge_expr = self.__extract_value_from_expr(expr)
        rule_index = edge_expr.getRuleIndex()

        if rule_index == GraphParser.RULE_edge_expr:
            left_num = self.__get_expr_type(edge_expr.getChild(1))
            char = self.__get_expr_type(edge_expr.getChild(3))
            right_num = self.__get_expr_type(edge_expr.getChild(5))

            edge_check_result = (
                left_num == GraphLangType.NUM
                and char == GraphLangType.CHAR
                and right_num == GraphLangType.NUM
            )

            return edge_check_result
        else:
            return False

    def __check_var_type(self, var_name: str, var_correct_type: GraphLangType) -> bool:
        """Check if variable exists in environment and if it has correct type."""
        if not self.__variables.contains_variable(var_name):
            raise Exception(f'Variable "{var_name}" doesn\'t exist')

        return self.__variables.get_variable(var_name) == var_correct_type

    def __extract_value_from_expr(self, expr: ParserRuleContext) -> ParserRuleContext:
        assert (
            expr.getRuleIndex() == GraphParser.RULE_expr
        ), "__extract_value_from_expr got something different from 'expr' type"

        return expr.getChild(0)
