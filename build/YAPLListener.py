# Generated from YAPL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#start.
    def enterStart(self, ctx:YAPLParser.StartContext):
        pass

    # Exit a parse tree produced by YAPLParser#start.
    def exitStart(self, ctx:YAPLParser.StartContext):
        pass


    # Enter a parse tree produced by YAPLParser#defClase.
    def enterDefClase(self, ctx:YAPLParser.DefClaseContext):
        pass

    # Exit a parse tree produced by YAPLParser#defClase.
    def exitDefClase(self, ctx:YAPLParser.DefClaseContext):
        pass


    # Enter a parse tree produced by YAPLParser#method.
    def enterMethod(self, ctx:YAPLParser.MethodContext):
        pass

    # Exit a parse tree produced by YAPLParser#method.
    def exitMethod(self, ctx:YAPLParser.MethodContext):
        pass


    # Enter a parse tree produced by YAPLParser#property.
    def enterProperty(self, ctx:YAPLParser.PropertyContext):
        pass

    # Exit a parse tree produced by YAPLParser#property.
    def exitProperty(self, ctx:YAPLParser.PropertyContext):
        pass


    # Enter a parse tree produced by YAPLParser#forml.
    def enterForml(self, ctx:YAPLParser.FormlContext):
        pass

    # Exit a parse tree produced by YAPLParser#forml.
    def exitForml(self, ctx:YAPLParser.FormlContext):
        pass


    # Enter a parse tree produced by YAPLParser#sub.
    def enterSub(self, ctx:YAPLParser.SubContext):
        pass

    # Exit a parse tree produced by YAPLParser#sub.
    def exitSub(self, ctx:YAPLParser.SubContext):
        pass


    # Enter a parse tree produced by YAPLParser#string.
    def enterString(self, ctx:YAPLParser.StringContext):
        pass

    # Exit a parse tree produced by YAPLParser#string.
    def exitString(self, ctx:YAPLParser.StringContext):
        pass


    # Enter a parse tree produced by YAPLParser#mul.
    def enterMul(self, ctx:YAPLParser.MulContext):
        pass

    # Exit a parse tree produced by YAPLParser#mul.
    def exitMul(self, ctx:YAPLParser.MulContext):
        pass


    # Enter a parse tree produced by YAPLParser#lteq.
    def enterLteq(self, ctx:YAPLParser.LteqContext):
        pass

    # Exit a parse tree produced by YAPLParser#lteq.
    def exitLteq(self, ctx:YAPLParser.LteqContext):
        pass


    # Enter a parse tree produced by YAPLParser#lt.
    def enterLt(self, ctx:YAPLParser.LtContext):
        pass

    # Exit a parse tree produced by YAPLParser#lt.
    def exitLt(self, ctx:YAPLParser.LtContext):
        pass


    # Enter a parse tree produced by YAPLParser#while.
    def enterWhile(self, ctx:YAPLParser.WhileContext):
        pass

    # Exit a parse tree produced by YAPLParser#while.
    def exitWhile(self, ctx:YAPLParser.WhileContext):
        pass


    # Enter a parse tree produced by YAPLParser#div.
    def enterDiv(self, ctx:YAPLParser.DivContext):
        pass

    # Exit a parse tree produced by YAPLParser#div.
    def exitDiv(self, ctx:YAPLParser.DivContext):
        pass


    # Enter a parse tree produced by YAPLParser#not.
    def enterNot(self, ctx:YAPLParser.NotContext):
        pass

    # Exit a parse tree produced by YAPLParser#not.
    def exitNot(self, ctx:YAPLParser.NotContext):
        pass


    # Enter a parse tree produced by YAPLParser#newObject.
    def enterNewObject(self, ctx:YAPLParser.NewObjectContext):
        pass

    # Exit a parse tree produced by YAPLParser#newObject.
    def exitNewObject(self, ctx:YAPLParser.NewObjectContext):
        pass


    # Enter a parse tree produced by YAPLParser#and.
    def enterAnd(self, ctx:YAPLParser.AndContext):
        pass

    # Exit a parse tree produced by YAPLParser#and.
    def exitAnd(self, ctx:YAPLParser.AndContext):
        pass


    # Enter a parse tree produced by YAPLParser#block.
    def enterBlock(self, ctx:YAPLParser.BlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#block.
    def exitBlock(self, ctx:YAPLParser.BlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#let.
    def enterLet(self, ctx:YAPLParser.LetContext):
        pass

    # Exit a parse tree produced by YAPLParser#let.
    def exitLet(self, ctx:YAPLParser.LetContext):
        pass


    # Enter a parse tree produced by YAPLParser#id.
    def enterId(self, ctx:YAPLParser.IdContext):
        pass

    # Exit a parse tree produced by YAPLParser#id.
    def exitId(self, ctx:YAPLParser.IdContext):
        pass


    # Enter a parse tree produced by YAPLParser#if.
    def enterIf(self, ctx:YAPLParser.IfContext):
        pass

    # Exit a parse tree produced by YAPLParser#if.
    def exitIf(self, ctx:YAPLParser.IfContext):
        pass


    # Enter a parse tree produced by YAPLParser#ownMethodCall.
    def enterOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        pass

    # Exit a parse tree produced by YAPLParser#ownMethodCall.
    def exitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        pass


    # Enter a parse tree produced by YAPLParser#INTEGER.
    def enterINTEGER(self, ctx:YAPLParser.INTEGERContext):
        pass

    # Exit a parse tree produced by YAPLParser#INTEGER.
    def exitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        pass


    # Enter a parse tree produced by YAPLParser#add.
    def enterAdd(self, ctx:YAPLParser.AddContext):
        pass

    # Exit a parse tree produced by YAPLParser#add.
    def exitAdd(self, ctx:YAPLParser.AddContext):
        pass


    # Enter a parse tree produced by YAPLParser#void.
    def enterVoid(self, ctx:YAPLParser.VoidContext):
        pass

    # Exit a parse tree produced by YAPLParser#void.
    def exitVoid(self, ctx:YAPLParser.VoidContext):
        pass


    # Enter a parse tree produced by YAPLParser#or.
    def enterOr(self, ctx:YAPLParser.OrContext):
        pass

    # Exit a parse tree produced by YAPLParser#or.
    def exitOr(self, ctx:YAPLParser.OrContext):
        pass


    # Enter a parse tree produced by YAPLParser#invert.
    def enterInvert(self, ctx:YAPLParser.InvertContext):
        pass

    # Exit a parse tree produced by YAPLParser#invert.
    def exitInvert(self, ctx:YAPLParser.InvertContext):
        pass


    # Enter a parse tree produced by YAPLParser#factExpr.
    def enterFactExpr(self, ctx:YAPLParser.FactExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#factExpr.
    def exitFactExpr(self, ctx:YAPLParser.FactExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#false.
    def enterFalse(self, ctx:YAPLParser.FalseContext):
        pass

    # Exit a parse tree produced by YAPLParser#false.
    def exitFalse(self, ctx:YAPLParser.FalseContext):
        pass


    # Enter a parse tree produced by YAPLParser#equal.
    def enterEqual(self, ctx:YAPLParser.EqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#equal.
    def exitEqual(self, ctx:YAPLParser.EqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#true.
    def enterTrue(self, ctx:YAPLParser.TrueContext):
        pass

    # Exit a parse tree produced by YAPLParser#true.
    def exitTrue(self, ctx:YAPLParser.TrueContext):
        pass


    # Enter a parse tree produced by YAPLParser#assign.
    def enterAssign(self, ctx:YAPLParser.AssignContext):
        pass

    # Exit a parse tree produced by YAPLParser#assign.
    def exitAssign(self, ctx:YAPLParser.AssignContext):
        pass


    # Enter a parse tree produced by YAPLParser#methodCall.
    def enterMethodCall(self, ctx:YAPLParser.MethodCallContext):
        pass

    # Exit a parse tree produced by YAPLParser#methodCall.
    def exitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        pass


    # Enter a parse tree produced by YAPLParser#nestedLet.
    def enterNestedLet(self, ctx:YAPLParser.NestedLetContext):
        pass

    # Exit a parse tree produced by YAPLParser#nestedLet.
    def exitNestedLet(self, ctx:YAPLParser.NestedLetContext):
        pass


    # Enter a parse tree produced by YAPLParser#letIn.
    def enterLetIn(self, ctx:YAPLParser.LetInContext):
        pass

    # Exit a parse tree produced by YAPLParser#letIn.
    def exitLetIn(self, ctx:YAPLParser.LetInContext):
        pass


    # Enter a parse tree produced by YAPLParser#letAssignLet.
    def enterLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        pass

    # Exit a parse tree produced by YAPLParser#letAssignLet.
    def exitLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        pass


    # Enter a parse tree produced by YAPLParser#letAssignIn.
    def enterLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        pass

    # Exit a parse tree produced by YAPLParser#letAssignIn.
    def exitLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        pass



del YAPLParser