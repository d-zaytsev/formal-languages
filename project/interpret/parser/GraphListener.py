# Generated from project/task11/parser/Graph.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser


# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):
    # Enter a parse tree produced by GraphParser#prog.
    def enterProg(self, ctx: GraphParser.ProgContext):
        pass

    # Exit a parse tree produced by GraphParser#prog.
    def exitProg(self, ctx: GraphParser.ProgContext):
        pass

    # Enter a parse tree produced by GraphParser#stmt.
    def enterStmt(self, ctx: GraphParser.StmtContext):
        pass

    # Exit a parse tree produced by GraphParser#stmt.
    def exitStmt(self, ctx: GraphParser.StmtContext):
        pass

    # Enter a parse tree produced by GraphParser#declare.
    def enterDeclare(self, ctx: GraphParser.DeclareContext):
        pass

    # Exit a parse tree produced by GraphParser#declare.
    def exitDeclare(self, ctx: GraphParser.DeclareContext):
        pass

    # Enter a parse tree produced by GraphParser#bind.
    def enterBind(self, ctx: GraphParser.BindContext):
        pass

    # Exit a parse tree produced by GraphParser#bind.
    def exitBind(self, ctx: GraphParser.BindContext):
        pass

    # Enter a parse tree produced by GraphParser#remove.
    def enterRemove(self, ctx: GraphParser.RemoveContext):
        pass

    # Exit a parse tree produced by GraphParser#remove.
    def exitRemove(self, ctx: GraphParser.RemoveContext):
        pass

    # Enter a parse tree produced by GraphParser#add.
    def enterAdd(self, ctx: GraphParser.AddContext):
        pass

    # Exit a parse tree produced by GraphParser#add.
    def exitAdd(self, ctx: GraphParser.AddContext):
        pass

    # Enter a parse tree produced by GraphParser#expr.
    def enterExpr(self, ctx: GraphParser.ExprContext):
        pass

    # Exit a parse tree produced by GraphParser#expr.
    def exitExpr(self, ctx: GraphParser.ExprContext):
        pass

    # Enter a parse tree produced by GraphParser#set_expr.
    def enterSet_expr(self, ctx: GraphParser.Set_exprContext):
        pass

    # Exit a parse tree produced by GraphParser#set_expr.
    def exitSet_expr(self, ctx: GraphParser.Set_exprContext):
        pass

    # Enter a parse tree produced by GraphParser#edge_expr.
    def enterEdge_expr(self, ctx: GraphParser.Edge_exprContext):
        pass

    # Exit a parse tree produced by GraphParser#edge_expr.
    def exitEdge_expr(self, ctx: GraphParser.Edge_exprContext):
        pass

    # Enter a parse tree produced by GraphParser#regexp.
    def enterRegexp(self, ctx: GraphParser.RegexpContext):
        pass

    # Exit a parse tree produced by GraphParser#regexp.
    def exitRegexp(self, ctx: GraphParser.RegexpContext):
        pass

    # Enter a parse tree produced by GraphParser#term.
    def enterTerm(self, ctx: GraphParser.TermContext):
        pass

    # Exit a parse tree produced by GraphParser#term.
    def exitTerm(self, ctx: GraphParser.TermContext):
        pass

    # Enter a parse tree produced by GraphParser#factor.
    def enterFactor(self, ctx: GraphParser.FactorContext):
        pass

    # Exit a parse tree produced by GraphParser#factor.
    def exitFactor(self, ctx: GraphParser.FactorContext):
        pass

    # Enter a parse tree produced by GraphParser#primary.
    def enterPrimary(self, ctx: GraphParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GraphParser#primary.
    def exitPrimary(self, ctx: GraphParser.PrimaryContext):
        pass

    # Enter a parse tree produced by GraphParser#range.
    def enterRange(self, ctx: GraphParser.RangeContext):
        pass

    # Exit a parse tree produced by GraphParser#range.
    def exitRange(self, ctx: GraphParser.RangeContext):
        pass

    # Enter a parse tree produced by GraphParser#select.
    def enterSelect(self, ctx: GraphParser.SelectContext):
        pass

    # Exit a parse tree produced by GraphParser#select.
    def exitSelect(self, ctx: GraphParser.SelectContext):
        pass

    # Enter a parse tree produced by GraphParser#v_filter.
    def enterV_filter(self, ctx: GraphParser.V_filterContext):
        pass

    # Exit a parse tree produced by GraphParser#v_filter.
    def exitV_filter(self, ctx: GraphParser.V_filterContext):
        pass

    # Enter a parse tree produced by GraphParser#num.
    def enterNum(self, ctx: GraphParser.NumContext):
        pass

    # Exit a parse tree produced by GraphParser#num.
    def exitNum(self, ctx: GraphParser.NumContext):
        pass

    # Enter a parse tree produced by GraphParser#char.
    def enterChar(self, ctx: GraphParser.CharContext):
        pass

    # Exit a parse tree produced by GraphParser#char.
    def exitChar(self, ctx: GraphParser.CharContext):
        pass

    # Enter a parse tree produced by GraphParser#var.
    def enterVar(self, ctx: GraphParser.VarContext):
        pass

    # Exit a parse tree produced by GraphParser#var.
    def exitVar(self, ctx: GraphParser.VarContext):
        pass


del GraphParser
