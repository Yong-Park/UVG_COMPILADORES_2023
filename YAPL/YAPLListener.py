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


    # Enter a parse tree produced by YAPLParser#class_list.
    def enterClass_list(self, ctx:YAPLParser.Class_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#class_list.
    def exitClass_list(self, ctx:YAPLParser.Class_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#class_def.
    def enterClass_def(self, ctx:YAPLParser.Class_defContext):
        pass

    # Exit a parse tree produced by YAPLParser#class_def.
    def exitClass_def(self, ctx:YAPLParser.Class_defContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature_list.
    def enterFeature_list(self, ctx:YAPLParser.Feature_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature_list.
    def exitFeature_list(self, ctx:YAPLParser.Feature_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature_def.
    def enterFeature_def(self, ctx:YAPLParser.Feature_defContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature_def.
    def exitFeature_def(self, ctx:YAPLParser.Feature_defContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature_body.
    def enterFeature_body(self, ctx:YAPLParser.Feature_bodyContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature_body.
    def exitFeature_body(self, ctx:YAPLParser.Feature_bodyContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal_list.
    def enterFormal_list(self, ctx:YAPLParser.Formal_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal_list.
    def exitFormal_list(self, ctx:YAPLParser.Formal_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal_param.
    def enterFormal_param(self, ctx:YAPLParser.Formal_paramContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal_param.
    def exitFormal_param(self, ctx:YAPLParser.Formal_paramContext):
        pass


    # Enter a parse tree produced by YAPLParser#expr_list.
    def enterExpr_list(self, ctx:YAPLParser.Expr_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#expr_list.
    def exitExpr_list(self, ctx:YAPLParser.Expr_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#expr.
    def enterExpr(self, ctx:YAPLParser.ExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#expr.
    def exitExpr(self, ctx:YAPLParser.ExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#case_list.
    def enterCase_list(self, ctx:YAPLParser.Case_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#case_list.
    def exitCase_list(self, ctx:YAPLParser.Case_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#case_def.
    def enterCase_def(self, ctx:YAPLParser.Case_defContext):
        pass

    # Exit a parse tree produced by YAPLParser#case_def.
    def exitCase_def(self, ctx:YAPLParser.Case_defContext):
        pass



del YAPLParser