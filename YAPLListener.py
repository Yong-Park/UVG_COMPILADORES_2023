# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#class.
    def enterClass(self, ctx:YAPLParser.ClassContext):
        pass

    # Exit a parse tree produced by YAPLParser#class.
    def exitClass(self, ctx:YAPLParser.ClassContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature.
    def enterFeature(self, ctx:YAPLParser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature.
    def exitFeature(self, ctx:YAPLParser.FeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#formalList.
    def enterFormalList(self, ctx:YAPLParser.FormalListContext):
        pass

    # Exit a parse tree produced by YAPLParser#formalList.
    def exitFormalList(self, ctx:YAPLParser.FormalListContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#expr.
    def enterExpr(self, ctx:YAPLParser.ExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#expr.
    def exitExpr(self, ctx:YAPLParser.ExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#assignExpr.
    def enterAssignExpr(self, ctx:YAPLParser.AssignExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#assignExpr.
    def exitAssignExpr(self, ctx:YAPLParser.AssignExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#condExpr.
    def enterCondExpr(self, ctx:YAPLParser.CondExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#condExpr.
    def exitCondExpr(self, ctx:YAPLParser.CondExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#orExpr.
    def enterOrExpr(self, ctx:YAPLParser.OrExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#orExpr.
    def exitOrExpr(self, ctx:YAPLParser.OrExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#andExpr.
    def enterAndExpr(self, ctx:YAPLParser.AndExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#andExpr.
    def exitAndExpr(self, ctx:YAPLParser.AndExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#relExpr.
    def enterRelExpr(self, ctx:YAPLParser.RelExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#relExpr.
    def exitRelExpr(self, ctx:YAPLParser.RelExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#addExpr.
    def enterAddExpr(self, ctx:YAPLParser.AddExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#addExpr.
    def exitAddExpr(self, ctx:YAPLParser.AddExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#multExpr.
    def enterMultExpr(self, ctx:YAPLParser.MultExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#multExpr.
    def exitMultExpr(self, ctx:YAPLParser.MultExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#unaryExpr.
    def enterUnaryExpr(self, ctx:YAPLParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#unaryExpr.
    def exitUnaryExpr(self, ctx:YAPLParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#atomExpr.
    def enterAtomExpr(self, ctx:YAPLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#atomExpr.
    def exitAtomExpr(self, ctx:YAPLParser.AtomExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#letBindingList.
    def enterLetBindingList(self, ctx:YAPLParser.LetBindingListContext):
        pass

    # Exit a parse tree produced by YAPLParser#letBindingList.
    def exitLetBindingList(self, ctx:YAPLParser.LetBindingListContext):
        pass


    # Enter a parse tree produced by YAPLParser#letBinding.
    def enterLetBinding(self, ctx:YAPLParser.LetBindingContext):
        pass

    # Exit a parse tree produced by YAPLParser#letBinding.
    def exitLetBinding(self, ctx:YAPLParser.LetBindingContext):
        pass


    # Enter a parse tree produced by YAPLParser#exprList.
    def enterExprList(self, ctx:YAPLParser.ExprListContext):
        pass

    # Exit a parse tree produced by YAPLParser#exprList.
    def exitExprList(self, ctx:YAPLParser.ExprListContext):
        pass



del YAPLParser