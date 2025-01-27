from parser.GraphParser import GraphParser
from parser.GraphVisitor import GraphVisitor
from typing import Tuple, Set, Optional
from networkx import MultiDiGraph
from pyformlang.finite_automaton import EpsilonNFA
from runner.regexp import (
    nfa_from_char,
    nfa_from_var,
    group,
    intersect,
    concatenate,
    union,
    repeat_range,
    build_rsm,
)
from project.task8 import tensor_based_cfpq


class GraphLangRunner(GraphVisitor):
    def __init__(self):
        super(GraphVisitor, self).__init__()
        self.__variables = {}
        self.__query_results = {}
        # Special for adding new query results
        self.__query_was_completed = False

    def printVariables(self):
        if not self.__variables:
            print("* No variables *")
            return

        for var_name, var_type in self.__variables.items():
            print(f"    {var_name} ~> {var_type}")

        for var_name, var_type in self.__query_results.items():
            print(f"    {var_name}:")
            for set_item in var_type:
                print(f"        {set_item}")

    def visitProg(self, ctx: GraphParser.ProgContext):
        self.visitChildren(ctx)

    def visitStmt(self, ctx: GraphParser.StmtContext):
        self.visitChildren(ctx)

    def visitDeclare(self, ctx: GraphParser.DeclareContext):
        var_name = self.__get_var_name(ctx.var())

        self.__variables[var_name] = MultiDiGraph()

    def visitBind(self, ctx: GraphParser.BindContext):
        var_name: str = self.__get_var_name(ctx.var())
        expr_value = self.visitExpr(ctx.expr())

        self.__variables[var_name] = expr_value

        # for SELECT
        if self.__query_was_completed:
            self.__query_was_completed = False

            self.__query_results[var_name] = expr_value

    def visitExpr(self, ctx: GraphParser.ExprContext):
        return self.visitChildren(ctx)

    def visitRegexp(self, ctx: GraphParser.RegexpContext):
        regexpInBrackets = ctx.L_PARENTHESIS() and ctx.R_PARENTHESIS()

        if ctx.char():
            return nfa_from_char(self.visitChar(ctx.char()))
        elif ctx.var():
            return nfa_from_var(ctx.var().getText())
        elif regexpInBrackets:
            return group(self.visitRegexp(ctx.regexp(0)))
        else:
            if ctx.CIRCUMFLEX():
                left_regexp, range = (
                    self.visitRegexp(ctx.regexp(0)),
                    self.visitRange(ctx.range_()),
                )

                return repeat_range(left_regexp, range[0], range[1])
            else:
                left_regexp, right_regexp = (
                    self.visitRegexp(ctx.regexp(0)),
                    self.visitRegexp(ctx.regexp(1)),
                )

                if ctx.PIPE():
                    return union(left_regexp, right_regexp)
                elif ctx.DOT():
                    return concatenate(left_regexp, right_regexp)
                elif ctx.AMPERSAND():
                    return intersect(left_regexp, right_regexp)

    def visitSelect(self, ctx: GraphParser.SelectContext):
        # for v in [start_set_expr]
        start_nodes_name, start_nodes_set = self.visitV_filter(ctx.v_filter(0))
        # for u in [final_set_expr]
        final_nodes_name, final_nodes_set = self.visitV_filter(ctx.v_filter(1))

        # ... IN <graph> ...
        graph: MultiDiGraph = self.visitVar(ctx.var()[-1])

        nfa_subs_dict: dict[str, EpsilonNFA] = {
            key: value
            for key, value in self.__variables.items()
            if isinstance(value, EpsilonNFA)
        }

        query = build_rsm(self.__expr_to_nfa(ctx.expr()), nfa_subs_dict)

        cfpq_result = tensor_based_cfpq(query, graph, start_nodes_set, final_nodes_set)
        select_result = set()

        # return frv, srv
        frv = ctx.var(0).getText()
        srv = ctx.var(1).getText()

        # return <start>, <final> where <final> reachable from <start>
        start_var_name = ctx.var()[-2].getText()
        final_var_name = ctx.var()[-3].getText()

        # return v
        if frv in [start_nodes_name, start_var_name] and not srv:
            for res in cfpq_result:
                select_result.add(res[0])
        # return u
        elif frv in [final_nodes_name, final_var_name] and not srv:
            for res in cfpq_result:
                select_result.add(res[1])
        # return u, v
        elif frv in [start_nodes_name, start_var_name] and srv in [
            final_nodes_name,
            final_var_name,
        ]:
            select_result = cfpq_result
        # return v, u
        elif frv in [final_nodes_name, final_var_name] and srv in [
            start_nodes_name,
            start_var_name,
        ]:
            for res in cfpq_result:
                select_result.add((res[1], res[0]))
        else:
            raise Exception("O_O")

        # Mark that for BIND
        self.__query_was_completed = True

        return select_result

    def visitV_filter(self, ctx: GraphParser.V_filterContext) -> Tuple[str, Set[int]]:
        if not ctx:
            return (None, None)

        var_name = ctx.var().getText()
        set_expr = self.visitExpr(ctx.expr())

        return (var_name, set_expr)

    def visitAdd(self, ctx: GraphParser.AddContext):
        graph: MultiDiGraph = self.visitVar(ctx.var())

        if ctx.EDGE():
            edge: Tuple[int, str, int] = self.visitExpr(ctx.expr())

            graph.add_edge(edge[0], edge[2], label=edge[1])
        else:
            vertex: int = self.visitExpr(ctx.expr())

            graph.add_node(vertex)

    def visitRemove(self, ctx: GraphParser.RemoveContext):
        # Check variable type
        graph: MultiDiGraph = self.visitVar(ctx.var())

        if ctx.EDGE():
            edge: Tuple[int, str, int] = self.visitExpr(ctx.expr())

            graph.remove_edge(edge[0], edge[2])
        elif ctx.VERTEX():
            vertex: int = self.visitExpr(ctx.expr())

            graph.remove_node(vertex)
        else:
            vertices: set[int] = self.visitExpr(ctx.expr())

            for vertex in vertices:
                graph.remove_node(vertex)

    def visitSet_expr(self, ctx: GraphParser.Set_exprContext) -> Set:
        exprs = ctx.expr()

        result_set: Set[int] = set()

        for expr in exprs:
            num = self.visitExpr(expr)
            result_set.add(num)

        return result_set

    def visitEdge_expr(self, ctx: GraphParser.Edge_exprContext) -> Tuple[int, str, int]:
        edge_exprs = ctx.expr()

        left_num = self.visitExpr(edge_exprs[0])
        char = self.visitExpr(edge_exprs[1])
        right_num = self.visitExpr(edge_exprs[2])

        edge = (left_num, char, right_num)

        return edge

    def visitRange(self, ctx: GraphParser.RangeContext) -> Tuple[int, Optional[int]]:
        return (ctx.num(0), ctx.num(1))

    def visitNum(self, ctx: GraphParser.NumContext):
        return int(ctx.NUM().getText())

    def visitChar(self, ctx: GraphParser.CharContext):
        return str(ctx.CHAR().getText()[1])
    
    def __expr_to_nfa(self, ctx: GraphParser.ExprContext) -> EpsilonNFA:
        expr_value = self.visitExpr(ctx)

        if isinstance(expr_value, EpsilonNFA):
            return expr_value
        elif isinstance(expr_value, str):
            return nfa_from_char(expr_value)
        else:
            raise Exception(f"illegal type '{expr_value}', it can't be coverted to EpsilonNFA.")

    def __get_var_name(self, ctx: GraphParser.VarContext) -> str:
        return str(ctx.VAR_ID().getText())

    def visitVar(self, ctx: GraphParser.VarContext):
        var_name = self.__get_var_name(ctx)
        if var_name not in self.__variables:
            raise Exception(f"Variable '{var_name}' doesn't exist.")

        return self.__variables[var_name]
