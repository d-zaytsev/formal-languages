from typechecker.utils.types import (
    VariableStore,
    VariablesPrinter,
    GraphLangType,
)
from parser.GraphParser import GraphParser
from parser.GraphVisitor import GraphVisitor


class GraphLangTyper(GraphVisitor):
    def __init__(self):
        super(GraphVisitor, self).__init__()
        self.__variables = VariableStore()
        self.__local_variables = VariableStore()

    def printVariables(self):
        VariablesPrinter(self.__variables).print()

    def visitProg(self, ctx: GraphParser.ProgContext):
        self.visitChildren(ctx)

    def visitStmt(self, ctx: GraphParser.StmtContext):
        self.visitChildren(ctx)

    def visitDeclare(self, ctx: GraphParser.DeclareContext):
        var_name = self.__get_var_name(ctx.var())

        self.__variables.add_variable(var_name, GraphLangType.GRAPH)

    def visitAdd(self, ctx: GraphParser.AddContext):
        # Check variable type
        var_name = self.__get_var_name(ctx.var())

        if self.visitVar(ctx.var()) != GraphLangType.GRAPH:
            raise Exception(
                f"Variable '{var_name}' have to be GRAPH, not '{self.__variables.get_variable(var_name)}'!"
            )

        # Check expr type
        added_entity_type = self.visitExpr(ctx.expr())

        if ctx.EDGE() and added_entity_type != GraphLangType.EDGE:
            raise Exception(
                f"Illegal edge construction, it can't be added to '{var_name}'."
            )
        elif ctx.VERTEX() and added_entity_type != GraphLangType.NUM:
            raise Exception(
                f"Illegal vertex construction, it can't be added to '{var_name}'."
            )
        else:
            return

    def visitRemove(self, ctx: GraphParser.RemoveContext):
        # Check variable type
        var_name = self.__get_var_name(ctx.var())
        var_type = self.visitVar(ctx.var())

        if var_type != GraphLangType.GRAPH:
            raise Exception(
                f"Variable '{var_name}' have to be GRAPH, not '{self.__variables.get_variable(var_name)}'!"
            )

        # Check expr type
        removed_entity_type = self.visitExpr(ctx.expr())

        if ctx.EDGE() and removed_entity_type != GraphLangType.EDGE:
            raise Exception(
                f"Illegal edge construction, it can't be removed from '{var_name}'."
            )
        elif ctx.VERTEX() and removed_entity_type != GraphLangType.NUM:
            raise Exception(
                f"Illegal vertex construction, it can't be removed from '{var_name}'."
            )
        elif ctx.VERTICES() and removed_entity_type != GraphLangType.SET:
            raise Exception(
                f"Illegal vertices construction, it can't be removed from '{var_name}'"
            )
        else:
            return

    def visitBind(self, ctx: GraphParser.BindContext):
        var_name: str = self.__get_var_name(ctx.var())
        bind_expr_type = self.visitExpr(ctx.expr())

        self.__variables.add_variable(var_name, bind_expr_type)

    def visitExpr(self, ctx: GraphParser.ExprContext):
        return self.visitChildren(ctx)

    def visitRegexp(self, ctx: GraphParser.RegexpContext) -> GraphLangType:
        regexpInBrackets = ctx.L_PARENTHESIS() and ctx.R_PARENTHESIS()

        if ctx.char():
            return GraphLangType.FA
        elif ctx.var():
            var_name = self.__get_var_name(ctx.var())

            if not self.__variables.contain_variable(var_name):
                return GraphLangType.RSM
            else:
                var_type = self.visitVar(ctx.var())

                if var_type in [GraphLangType.FA, GraphLangType.CHAR]:
                    return GraphLangType.FA

                elif var_type == GraphLangType.RSM:
                    return GraphLangType.RSM

                else:
                    raise Exception(
                        f"Illegal variable type '{var_type}' occured in regexp: '{var_name}'"
                    )

        elif regexpInBrackets:
            return self.visitRegexp(ctx.regexp(0))
        else:
            if ctx.CIRCUMFLEX():
                left_regexp, range = ctx.regexp(0), ctx.range_()

                left_regexp_type = self.visitRegexp(left_regexp)
                range_type = self.visitRange(range)

                if range_type != GraphLangType.RANGE:
                    raise Exception(
                        f"Illegal type in regexp: '{range_type}' instead of '{GraphLangType.RANGE}"
                    )

                if left_regexp_type == GraphLangType.FA:
                    return GraphLangType.FA
                elif left_regexp_type == GraphLangType.RSM:
                    return GraphLangType.RSM
                else:
                    raise Exception(
                        f"Type '{left_regexp_type}' can't be in Repeat (^) operation."
                    )

            else:
                left_regexp, right_regexp = ctx.regexp(0), ctx.regexp(1)

                left_regexp_type, right_regexp_type = (
                    self.visitRegexp(left_regexp),
                    self.visitRegexp(right_regexp),
                )

                if ctx.PIPE() or ctx.DOT():
                    return (
                        GraphLangType.RSM
                        if left_regexp_type == GraphLangType.RSM
                        or right_regexp_type == GraphLangType.RSM
                        else GraphLangType.FA
                    )
                elif ctx.AMPERSAND():
                    if (
                        left_regexp_type == GraphLangType.RSM
                        and right_regexp_type == GraphLangType.RSM
                    ):
                        raise Exception(
                            f'Can\'t intersect two RSMs: "{ctx.getText()}".'
                        )

                    return (
                        GraphLangType.RSM
                        if left_regexp_type == GraphLangType.RSM
                        or right_regexp_type == GraphLangType.RSM
                        else GraphLangType.FA
                    )

        return GraphLangType.UNKNOWN

    def visitSelect(self, ctx: GraphParser.SelectContext):
        # Check v_filters
        v_filter_1, v_filter_2 = ctx.v_filter(0), ctx.v_filter(1)

        if v_filter_1 and self.visitV_filter(v_filter_1) != GraphLangType.SET:
            raise Exception(f"Incorrect type for: '{v_filter_1.getText()}'")
        if v_filter_2 and self.visitV_filter(v_filter_2) != GraphLangType.SET:
            raise Exception(f"Incorrect type for: '{v_filter_2.getText()}'")

        # Check vars
        var_list: list = ctx.var()

        in_var = self.__get_var_name(var_list[-1])
        from_var = self.__get_var_name(var_list[-2])
        where_var = self.__get_var_name(var_list[-3])

        if self.__variables.get_variable(in_var) != GraphLangType.GRAPH:
            raise Exception(
                f"Incorrect type of variable '{in_var}', it should be '{GraphLangType.GRAPH}'."
            )

        if self.__local_variables.contain_variable(from_var):
            if self.__local_variables.get_variable(from_var) != GraphLangType.SET:
                raise Exception(
                    f"Incorrect type of variable '{from_var}', it should be '{GraphLangType.GRAPH}'."
                )
        else:
            self.__local_variables.add_variable(from_var, GraphLangType.SET)

        if self.__local_variables.contain_variable(where_var):
            raise Exception(f"Variable '{where_var}' already exists.")
        else:
            self.__local_variables.add_variable(where_var, GraphLangType.SET)

        # Check result vars
        result_var_1 = self.__get_var_name(var_list[0])
        result_var_2 = self.__get_var_name(var_list[1]) if ctx.COMMA() else None

        if (
            not self.__local_variables.contain_variable(result_var_1)
        ) or self.__local_variables.get_variable(result_var_1) != GraphLangType.SET:
            raise Exception(f"Inappropriate variable '{result_var_1}'.")

        if result_var_2 and (
            not self.__local_variables.contain_variable(result_var_2)
            or self.__local_variables.get_variable(result_var_2) != GraphLangType.SET
        ):
            raise Exception(f"Inappropriate variable '{result_var_2}'.")

        # check expr
        expr_type = self.visitExpr(ctx.expr())

        if expr_type not in [GraphLangType.FA, GraphLangType.RSM]:
            raise Exception(f"Illegal expression in SELECT with type '{expr_type}'.")

        self.__local_variables.clear()
        return GraphLangType.SET if not result_var_2 else GraphLangType.PAIR_SET

    def visitV_filter(self, ctx: GraphParser.V_filterContext):
        var_name = self.__get_var_name(ctx.var())

        # Create new SET variable
        if not self.__variables.contain_variable(var_name):
            self.__local_variables.add_variable(var_name, GraphLangType.SET)
        else:
            raise Exception(f"Variable '{var_name}' already exists.")

        expr_type = self.visitExpr(ctx.expr())

        if expr_type == GraphLangType.SET:
            return GraphLangType.SET
        else:
            raise Exception(
                f"Illegal filter expression of type '{expr_type}': '{ctx.getText()}'."
            )

    def visitSet_expr(self, ctx: GraphParser.Set_exprContext) -> GraphLangType:
        exprs = ctx.expr()

        for expr in exprs:
            if self.visitExpr(expr) != GraphLangType.NUM:
                raise Exception(f"Illegal construction in RANGE: '{expr.getText()}'")

        return GraphLangType.SET

    def visitEdge_expr(self, ctx: GraphParser.Edge_exprContext):
        edge_exprs = ctx.expr()

        left_num_check = self.visitExpr(edge_exprs[0]) == GraphLangType.NUM
        char_check = self.visitExpr(edge_exprs[1]) == GraphLangType.CHAR
        right_num_check = self.visitExpr(edge_exprs[2]) == GraphLangType.NUM

        edge_check = left_num_check and char_check and right_num_check

        if edge_check:
            return GraphLangType.EDGE
        else:
            raise Exception(f"Illegal EDGE construction: '{ctx.getText()}'")

    def __get_var_name(self, ctx: GraphParser.VarContext) -> str:
        return str(ctx.VAR_ID().getText())

    def visitRange(self, ctx: GraphParser.RangeContext) -> GraphLangType:
        return GraphLangType.RANGE

    def visitNum(self, ctx: GraphParser.NumContext) -> GraphLangType:
        return GraphLangType.NUM

    def visitChar(self, ctx: GraphParser.CharContext) -> GraphLangType:
        return GraphLangType.CHAR

    def visitVar(self, ctx: GraphParser.VarContext) -> GraphLangType:
        var_name = self.__get_var_name(ctx)
        if not self.__variables.contain_variable(var_name):
            raise Exception(f"Variable '{var_name}' doesn't exist.")

        return self.__variables.get_variable(var_name)
