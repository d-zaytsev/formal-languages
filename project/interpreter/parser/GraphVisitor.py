# Generated from project/interpret/parser/Graph.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.


class GraphVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by GraphParser#prog.
    def visitProg(self, ctx: GraphParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#stmt.
    def visitStmt(self, ctx: GraphParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#declare.
    def visitDeclare(self, ctx: GraphParser.DeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#bind.
    def visitBind(self, ctx: GraphParser.BindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#remove.
    def visitRemove(self, ctx: GraphParser.RemoveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#add.
    def visitAdd(self, ctx: GraphParser.AddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#expr.
    def visitExpr(self, ctx: GraphParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#set_expr.
    def visitSet_expr(self, ctx: GraphParser.Set_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#edge_expr.
    def visitEdge_expr(self, ctx: GraphParser.Edge_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#regexp.
    def visitRegexp(self, ctx: GraphParser.RegexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#range.
    def visitRange(self, ctx: GraphParser.RangeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#select.
    def visitSelect(self, ctx: GraphParser.SelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#v_filter.
    def visitV_filter(self, ctx: GraphParser.V_filterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#num.
    def visitNum(self, ctx: GraphParser.NumContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#char.
    def visitChar(self, ctx: GraphParser.CharContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GraphParser#var.
    def visitVar(self, ctx: GraphParser.VarContext):
        return self.visitChildren(ctx)


del GraphParser
