# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from build.YAPLParser import YAPLParser
else:
    from build.YAPLParser import YAPLParser

from SymbolTable import SymbolTable

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisit(ParseTreeVisitor):

    def __init__(self):
        self.symbol_table = SymbolTable()

    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        # print("start visitado")
        startType = None
        tipos = ctx.classDefine()
        for tipo in tipos:
            tip = self.visit(tipo)
            # print("start tipo:", tip)
            if tip != None:
                startType = tip
        return startType


    # Visit a parse tree produced by YAPLParser#defClase.
    def visitDefClase(self, ctx:YAPLParser.DefClaseContext):
        # print("DefClase visitado")
        defclaseType = None
        tipos = ctx.feature()
        for tipo in tipos:
            tip = self.visit(tipo)
            # print("DefClase tipo:", tip)
            if tip == "Int":
                defclaseType = tip
            elif tip == "Char":
                defclaseType = tip
            elif tip == "Bool":
                defclaseType = tip
        return defclaseType


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        # print("method call")
        method_name = ctx.ID().getText()
        method_type = ctx.TYPE().getText()
        # print('method_name: ', method_name, '\n')
        # print('method_type: ', method_type, '\n')

        # Agregar el método a la Tabla de Símbolos
        self.symbol_table.add_symbol(method_name, method_type)
        # print("symbol table: ", self.symbol_table)
        # print("++++++++++++++++++++++") 
        # Continuar con el recorrido del árbol sintáctico
        method_expr_type = self.visit(ctx.expr())
        # print("method expr type: ", method_expr_type)
        return method_expr_type

    # Visit a parse tree produced by YAPLParser#property.
    def visitProperty(self, ctx:YAPLParser.PropertyContext):
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        self.symbol_table.add_symbol(var_name, var_type)
        var_expr = self.visit(ctx.expr()) if ctx.expr() != None else None
        var_assign = ctx.ASSIGN()
        # print("var_expr: ",var_expr)
        # print('var_name: ', var_name)
        # print('var_type: ', var_type)
        # print('var_assign: ', var_assign, '\n')
        # revisar si es del mismo tipo la asignacion cuando se realice
        if var_assign != None:
            if var_type != var_expr:
                return None
        
        # if ctx.expr():
        #     # Si hay una expresión de asignación, verificar su tipo
        #     initial_value_type = self.visit(ctx.expr())
        #     if initial_value_type != var_type:
        #         return None
        #         # Manejar el error de tipos para la asignación inicial
        #         raise TypeError(f"Error de tipos en la asignación inicial de '{var_name}': "
        #                         f"se esperaba '{var_type}', pero se obtuvo '{initial_value_type}'")
            
        #     # Agregar la variable a la Tabla de Símbolos con su tipo y valor inicial
        #     print('var_name: ', var_name, '\n')
        #     print('var_type: ', var_type, '\n')
        #     print('initial_value_type: ', initial_value_type, '\n')
        #     self.symbol_table.add_symbol(var_name, var_type, initial_value_type)
        # else:
            # Si no hay asignación inicial, agregar la variable a la Tabla de Símbolos solo con su tipo
        
        # print("symbol table: ", self.symbol_table)
        # print("++++++++++++++++++++++") 
        # Continuar con el recorrido del árbol sintáctico
        return var_expr

    # Visit a parse tree produced by YAPLParser#forml.
    def visitForml(self, ctx:YAPLParser.FormlContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by YAPLParser#or.
    def visitOr(self, ctx:YAPLParser.OrContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if left_type == "Bool" and right_type == "Bool":
            return left_type
        else:
            return None
    
    # Visit a parse tree produced by YAPLParser#and.
    def visitAnd(self, ctx:YAPLParser.AndContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if left_type == "Bool" and right_type == "Bool":
            return left_type
        else:
            return None

    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        # print("Visiting Add node")
        # print('add')
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        # print('left add: ',left)
        # print('left add type: ',left_type)
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        # print('right add:', right)
        # print('right add type:', right_type)
        if left_type == "Int" and right_type == "Int":
            return left_type
        elif left_type == "Char" and right_type == "Char":
            return left_type
        else:
            return None
            # Manejar el error de tipos para la operación de suma
            raise TypeError("Error de tipos: la suma solo está definida para enteros")


    # Visit a parse tree produced by YAPLParser#sub.
    def visitSub(self, ctx:YAPLParser.SubContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if left_type == "Int" and right_type == "Int":
            return left_type
        else:
            return None
            # Manejar el error de tipos para la operación de resta
            raise TypeError("Error de tipos: la resta solo está definida para enteros")


    # Visit a parse tree produced by YAPLParser#void.
    def visitVoid(self, ctx:YAPLParser.VoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#invert.
    def visitInvert(self, ctx:YAPLParser.InvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        # print("Visiting Mul node")
        # print('mul')
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        # print("left mul", left)
        # print('left mul type: ',left_type)
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        # print("right mul: ",right)
        # print('right mul type:', right_type)
        if left_type == "Int" and right_type == "Int":
            return left_type
        else:
            return None
            # Manejar el error de tipos para la operación de multiplicación
            raise TypeError("Error de tipos: la multiplicación solo está definida para enteros")



    # Visit a parse tree produced by YAPLParser#factExpr.
    def visitFactExpr(self, ctx:YAPLParser.FactExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lteq.
    def visitLteq(self, ctx:YAPLParser.LteqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lt.
    def visitLt(self, ctx:YAPLParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#div.
    def visitDiv(self, ctx:YAPLParser.DivContext):
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if left_type == "Int" and right_type == "Int":
            return left_type
        else:
            return None
            # Manejar el error de tipos para la operación de división
            raise TypeError("Error de tipos: la división solo está definida para enteros")


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        # print("visitando equal")
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        # print("left equal", left)
        # print('left equal type: ',left_type)
        right = self.visit(ctx.expr(1))
        # print("right equal", right)
        if left_type == right:
            return left_type
        else:
            return None
            # Manejar el error de tipos para la operación de división
            raise TypeError("Error de tipos: la igualdad solo se puede en variables del mismo tipo")


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#newObject.
    def visitNewObject(self, ctx:YAPLParser.NewObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        value = ctx.ID().getText()
        # print("id value: ", value)
        return value


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#INTEGER.
    def visitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        print("Visiting Assign node")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#methodCall.
    def visitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#nestedLet.
    def visitNestedLet(self, ctx:YAPLParser.NestedLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letAssignLet.
    def visitLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letAssignIn.
    def visitLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        return self.visitChildren(ctx)



del YAPLParser