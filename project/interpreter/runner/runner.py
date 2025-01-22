from parser.GraphParser import GraphParser
from parser.GraphVisitor import GraphVisitor
from typing import Tuple, Set
from networkx import MultiDiGraph


class GraphLangRunner(GraphVisitor):
    def __init__(self):
        super(GraphVisitor, self).__init__()
        self.__variables = {}
        self.__select_results = {}

    def printVariables(self):
        if not self.__variables:
            print("* No variables *")
            return

        for var_name, var_type in self.__variables.items():
            print(f"    {var_name} ~> {var_type}")

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

    def visitExpr(self, ctx: GraphParser.ExprContext):
        return self.visitChildren(ctx)

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

    def visitNum(self, ctx: GraphParser.NumContext):
        return int(ctx.NUM().getText())

    def visitChar(self, ctx: GraphParser.CharContext):
        return str(ctx.CHAR().getText())

    def __get_var_name(self, ctx: GraphParser.VarContext) -> str:
        return str(ctx.VAR_ID().getText())

    def visitVar(self, ctx: GraphParser.VarContext):
        var_name = self.__get_var_name(ctx)
        if var_name not in self.__variables:
            raise Exception(f"Variable '{var_name}' doesn't exist.")

        return self.__variables[var_name]
