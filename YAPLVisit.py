# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from build.YAPLParser import YAPLParser
else:
    from build.YAPLParser import YAPLParser

from SymbolTable import SymbolTable
from copy import *

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisit(ParseTreeVisitor):

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.actual_class = None
        self.actual_method = None
        self.actual_method_type = None
        self.startType = None
        self.errors = ["inheritProblem","noMain","boolAr","intchar","charAr","assignEr","notequal","noValue","ifError","notLessorequal","notLess","methodError","noMethodAssign"]

    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        print("start visitado")
        
        message = None
        results = []
        tipos = ctx.classDefine()
        for tipo in tipos:
            val = self.visit(tipo)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
            # print("start tipo:", tip)
            # if tip != None:
            #     self.startType = tip
        print(self.symbol_table)
        #realizar ultima revision si existe una clase Main y un metodo main en la clase Main
        MainExist = self.symbol_table.contains_mains()
        # print("MainExist: ",MainExist)
        print("=============================")
        print("visitStart results: ",results)
        for result in results:
            if result in self.errors:
                self.startType = result
        if self.startType == None:
            self.startType = results[0]
        print("self.startType: ",self.startType)
        if self.startType == "Int":
            message = self.startType
        elif self.startType == "Char":
            message = self.startType
        elif self.startType == "Bool":
            message = self.startType
        elif self.startType == "boolAr":
            message = "no se puede operar operaciones aritmetricas entre Bools"
        elif self.startType == "intchar":
            message = "no se puede operar operaciones aritmetricas Int y Char"
        elif self.startType == "charAr":
            message = "no se puede operaciones aritmetricas entre chars"
        elif self.startType == "assignEr":
            message = "no se puede asignar variables ya que no es del mismo tipo"
        elif self.startType == "notequal":
            message = "no se puede asignar variables ya que no es del mismo tipo"
        elif self.startType == "noValue":
            message = "no se puede debido a una variable no existe o no puede ser utilizada en ese entorno"
        elif self.startType == "ifError":
            message = "la funcion de if esta fallando"
        elif self.startType == "notLessorequal":
            message = "No es posible, alguno de los valores al probar <= no es de tipo Int"
        elif self.startType == "notLess":
            message = "No es posible, alguno de los valores al probar < no es de tipo Int"
        elif self.startType == "methodError":
            message = "El metodo tiene un problema"
        elif self.startType == "noMethodAssign":
            message = "El metodo no existe y por ello no se le puede asignar a una variable"
        elif self.startType == "inheritProblem":
            message = "Problema con la herencia (inherits)"
        else:
            message = self.startType
        print("self.startType to send: ",message)
        print("=============================")
        
        if MainExist == False:
            self.startType = "noMain"
            return "Error No existe el Main o main"
        
        return message


    # Visit a parse tree produced by YAPLParser#defClase.
    def visitDefClase(self, ctx:YAPLParser.DefClaseContext):
        print("DefClase visitado")
        defclaseClass = ctx.CLASS()
        # print(defclaseClass)
        
        #definir la clase actual en la que esta
        
        defclaseTypeList = ctx.TYPE()
        classtype = defclaseTypeList[0]
        # print(classtype)
        self.actual_class = classtype
        
        #agregar todos las variables
        variables = ctx.feature()
        variable_array = []
        for variable in variables:
            # print("variable :", variable.ID().getText())
            if variable.ID().getText():
                variable_array.append(variable.ID().getText())
        defclaseInherits = ctx.INHERITS() #revisar si existe la funcion inherits
        # print(defclaseInherits)
        if defclaseInherits:
            inheritPosition = defclaseTypeList[1]
            if len(variable_array) > 0: 
                self.symbol_table.add_symbol(classtype, defclaseClass, inherits=inheritPosition, contains=variable_array)
            else:
                self.symbol_table.add_symbol(classtype, defclaseClass, inherits=inheritPosition)
            # print(inheritPosition)
            if str(inheritPosition) == "IO":
                pass
            else:
                print("inheritPosition: ",inheritPosition)
                if self.symbol_table.contains_symbol(str(inheritPosition)) and str(self.symbol_table.get_symbol_type(str(inheritPosition))) == "class" and str(classtype) != "Main":
                    pass
                else:
                    print("No existe")
                    return "inheritProblem"
                
        else:
            if len(variable_array) > 0:
                self.symbol_table.add_symbol(classtype, defclaseClass,contains=variable_array)
            else:
                self.symbol_table.add_symbol(classtype, defclaseClass)
        
        defclaseType = None
        tipos = ctx.feature()
        results = []
        for tipo in tipos:
            val = self.visit(tipo)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        
        print("DefClase results: ", results)
        
        for result in results:
            if result in self.errors:
                return result
        return results

    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        print("visitMethod")
        method_name = ctx.ID().getText()
        method_type = ctx.TYPE().getText()
        self.symbol_table.add_symbol(method_name, method_type)
        formlExist = ctx.formal()
        self.actual_method = method_name
        self.actual_method_type = method_type
        print('method_name: ', method_name, '\n')
        print('method_type: ', method_type, '\n')
        for form in formlExist:
            print(self.visit(form))
        # Agregar el método a la Tabla de Símbolos
        
        # print("symbol table: ", self.symbol_table)
        # print("++++++++++++++++++++++") 
        # Continuar con el recorrido del árbol sintáctico
        method_expr_type = self.visit(ctx.expr())
        method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
        print("method expr type: ", method_expr_type)
        print("=============================")
        return method_expr_type

    # Visit a parse tree produced by YAPLParser#property.
    def visitProperty(self, ctx:YAPLParser.PropertyContext):
        print("visitProperty")
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        
        var_expr = self.visit(ctx.expr()) if ctx.expr() != None else []
        var_assign = ctx.ASSIGN()
        print("var_expr: ",var_expr)
        print('var_name: ', var_name)
        print('var_type: ', var_type)
        print('var_assign: ', var_assign, '\n')
        #revisar que la variable si no es int, char o bool sea algo que exista en la tabla
        if str(var_type) not in ["Int","Char","Bool"]:
            print("toca buscar")
            if self.symbol_table.contains_symbol(var_type):
                print("Si existe")
                pass
            else:
                return "noMethodAssign"
        
        #asignar el width setun si tipo
        if var_type == "Int":
            self.symbol_table.add_symbol(var_name, var_type,width=8)
        elif var_type == "Char":
            self.symbol_table.add_symbol(var_name, var_type,width=4)
        else:
            self.symbol_table.add_symbol(var_name, var_type)
            
        
        # revisar si es del mismo tipo la asignacion cuando se realice
        if var_assign != None:
            var_expr = self.symbol_table.get_symbol_type(var_expr) if self.symbol_table.get_symbol_type(var_expr) else var_expr
            if var_type not in var_expr:
                print("assignEr")
                return "assignEr"
        
        # print("symbol table: ", self.symbol_table)
        # print("++++++++++++++++++++++") 
        # Continuar con el recorrido del árbol sintáctico
        print("visitProperty var_type: ",var_type)
        print("=============================")
        return var_type

    # Visit a parse tree produced by YAPLParser#forml.
    def visitForml(self, ctx:YAPLParser.FormlContext):
        print("visitForml")
        idtext = ctx.ID().getText()
        tipo = ctx.TYPE().getText()
        print("idtext: ",idtext)
        print("tipo: ",tipo)
        self.symbol_table.add_symbol(idtext,tipo)
        # print("self.actual_method: ",self.actual_method)
        #agregarlo en su contains
        contains = self.symbol_table.get_contains(self.actual_method)
        array = []
        if contains == None:
            array.append(idtext)
        else:
            array.append(idtext)
            for ele in contains:
                array.append(str(ele))
            
        
            
        self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        print("=============================")
        # return self.visitChildren(ctx)
    
    # Visit a parse tree produced by YAPLParser#or.
    def visitOr(self, ctx:YAPLParser.OrContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left_type == "noValue":
            return left_type
        
        if type(left_type) == list:
            left_type = left_type[0]
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        
        if type(right_type) == list:
            right_type = right_type[0]
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Bool" and right_type == "Bool":
            return left_type
        else:
            return None
    
    # Visit a parse tree produced by YAPLParser#and.
    def visitAnd(self, ctx:YAPLParser.AndContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left_type == "noValue":
            return left_type
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
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
        if left_type == "noValue":
            return left_type
        
        if type(left_type) == list:
            left_type = left_type[0]
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        # print('right add:', right)
        # print('right add type:', right_type)
        if right_type == "noValue":
            return right_type
        
        if type(right_type) == list:
            right_type = right_type[0]
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        elif left_type == "Char" and right_type == "Char":
            return left_type
        # errors
        elif left_type == "Int" and right_type == "Char":
            return "intchar"
        elif left_type == "Char" and right_type == "Int":
            return "intchar"
        elif left_type == "Bool" and right_type == "Bool":
            return "boolAr"
        else:
            return None


    # Visit a parse tree produced by YAPLParser#sub.
    def visitSub(self, ctx:YAPLParser.SubContext):
        
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left_type == "noValue":
            return left_type
        
        if type(left_type) == list:
            left_type = left_type[0]
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        
        if type(right_type) == list:
            right_type = right_type[0]
        print("visitSub")
        print("left_type: ",left_type)
        print("right_type: ",right_type )
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        # errors
        elif left_type == "Char" and right_type == "Char":
            return "charAr"
        elif left_type == "Int" and right_type == "Char":
            return "intchar"
        elif left_type == "Char" and right_type == "Int":
            return "intchar"
        elif left_type == "Bool" and right_type == "Bool":
            return "boolAr"
        else:
            return None


    # Visit a parse tree produced by YAPLParser#void.
    def visitVoid(self, ctx:YAPLParser.VoidContext):
        print("visitVoid")
        type = self.visit(ctx.expr())
        print("visitVoid type: ",type)
        print("=============================")
        #comprar si lo que se regreso es de tipo void
        if str(type) == "Void":
            return self.visitTrue(ctx)
        else:
            return self.visitFalse(ctx)


    # Visit a parse tree produced by YAPLParser#invert.
    def visitInvert(self, ctx:YAPLParser.InvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        return "Char"


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        print("Visiting Mul node")
        # print('mul')
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left_type == "noValue":
            return left_type
        
        print("left mul", left)
        print('left mul type: ',left_type)
        if type(left_type) == list:
            left_type = left_type[0]
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        print("right mul: ",right)
        print('right mul type:', right_type)
        if type(right_type) == list:
            right_type = right_type[0]
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        # errors
        elif left_type == "Char" and right_type == "Char":
            return "charAr"
        elif left_type == "Int" and right_type == "Char":
            return "intchar"
        elif left_type == "Char" and right_type == "Int":
            return "intchar"
        elif left_type == "Bool" and right_type == "Bool":
            return "boolAr"
        else:
            return None



    # Visit a parse tree produced by YAPLParser#factExpr.
    def visitFactExpr(self, ctx:YAPLParser.FactExprContext):
        expresion = self.visit(ctx.expr())
        print("FactExpr: ",expresion)
        print("=============================")
        return expresion


    # Visit a parse tree produced by YAPLParser#lteq.
    def visitLteq(self, ctx:YAPLParser.LteqContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        else:
            return "notLessorequal"
        

    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#lt.
    def visitLt(self, ctx:YAPLParser.LtContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        else:
            return "notLess"

    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        print("while visitado")
        expresions = ctx.expr()
        results = []
        for expresion in expresions:
            val = self.visit(expresion)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        print("visitWhile results: ",results)
        print("=============================")
        for result in results:
            if result in self.errors:
                return result
        return results


    # Visit a parse tree produced by YAPLParser#div.
    def visitDiv(self, ctx:YAPLParser.DivContext):
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left_type == "noValue":
            return left_type
        
        if type(left_type) == list:
            left_type = left_type[0]
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        
        if type(right_type) == list:
            right_type = right_type[0]
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        # errors
        elif left_type == "Char" and right_type == "Char":
            return "charAr"
        elif left_type == "Int" and right_type == "Char":
            return "intchar"
        elif left_type == "Char" and right_type == "Int":
            return "intchar"
        elif left_type == "Bool" and right_type == "Bool":
            return "boolAr"
        else:
            return None


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        print("visitando equal")
        left = self.visit(ctx.expr(0)) 
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
       
        if type(left_type) == list:
            left_type = left_type[0]
            
        print("left equal", left)
        print('left equal type: ',left_type)
        print("=============================")
        #si no existe
        if left_type == "noValue":
            return  left_type
        
        
        right = self.visit(ctx.expr(1))
        # print("right equal", right)
        if right in ["Int","Char","Bool"]:
            if left_type == right:
                return left_type
            else:
                return "notequal"
        else:
            return right


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        print("visitNot")
        values = self.visit(ctx.expr())
        
        results = []
        if type(values) == list:
            results.extend(values)
        else:
            results.append(values)
        print("visitNot results: ",results)
        return results


    # Visit a parse tree produced by YAPLParser#newObject.
    def visitNewObject(self, ctx:YAPLParser.NewObjectContext):
        print("visitNewObject")
        print(ctx.TYPE().getText())
        print("=============================")
        return ctx.TYPE().getText()


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        expresions = ctx.expr()
        results = []
        for expresion in expresions:
            val = self.visit(expresion)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        
        print("visitBlock result: ", results)
        print("=============================")
        for result in results:
            if result in self.errors:
                return result
            
        return results


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        print("visitLet")
        result = self.visit(ctx.let_expr())
        print("visitLet result: ",result)
        return result


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        # print("id visitado")
        value = ctx.ID().getText()
        print("id value: ", value)
        #revisar si es de tipo self
        if str(value) == "self":
            self.symbol_table.add_symbol(value, "Void")
            # print("self.actual_method: ",self.actual_method)
            tipo = self.symbol_table.get_symbol_type(self.actual_method)
            # print("tipo: ",tipo)
            contains = self.symbol_table.get_contains(self.actual_method)
            contain = []
            if contains == None:
                contain = [value]
            else:
                contain.append(value)
            self.symbol_table.add_symbol(self.actual_method,tipo,contains=contain)
      
            return "Void"
        else:
            exist = self.symbol_table.variable_class(self.actual_class, value) if self.symbol_table.variable_class(self.actual_class, value) else self.symbol_table.variable_class(self.actual_method, value)
        
        print("existe: ", exist)
        print("=============================")
        if exist:
            return value
        else:
            return "noValue"


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        print("if visitado")
        expresions = ctx.expr()
        results = []
        for expresion in expresions:
            val = self.visit(expresion)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        print("visitIf results: ",results)
        print("=============================")
        #revisar que de los resultados obtenido no haya ninguno que forme parte de algun error
        for result in results:
            if result in self.errors:
                return "ifError"
        return results
        
    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        print("visitOwnMethodCall")
        expresions = ctx.expr()
        results = []
        for expresion in expresions:
            val = self.visit(expresion)
            if type(val)==list:
                results.extend(val)
            else:
                val = self.symbol_table.get_symbol_type(val) if self.symbol_table.get_symbol_type(val) else val
                results.append(val)
            
        print("visitOwnMethodCall results: ", results)
        print("=============================")
        for result in results:
            if result in self.errors:
                return "methodError"
        
        return results


    # Visit a parse tree produced by YAPLParser#INTEGER.
    def visitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        return "Int"


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        print("assign visitado")
        expresion = self.visit(ctx.expr())
        left = ctx.ID().getText()
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.get_symbol_type(left) else "noValue"
        print("expresion: ",expresion)
        # expresion = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        # print("expresion later: ",expresion)
        print("left: ",left)
        print("left_type: ",left_type)
        print("=============================")
        if type(expresion) == list:
            print("es una lista")
            if left_type in expresion:
                return left_type
            return "assignEr"
        else:
            if left_type == expresion:
                return left_type
            else:
                expresion = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
                if left_type == expresion:
                    return left_type
                else:
                    return "assignEr"


    # Visit a parse tree produced by YAPLParser#methodCall.
    def visitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        expresions = ctx.expr()
        results=[] 
        for expreion in expresions:
            # print("visitMethodCall")
            val = self.visit(expreion)
            print("visitMethodCall: ",val)
            if type(val) == list:
                results.extend(val)
            else:
                # print("self.actual_class: ",self.actual_class)
                # print("val: ",val)
                # if self.symbol_table.contains_element(self.actual_class,val):
                #     print("si contiene ")
                val = self.symbol_table.get_symbol_type(val) if (self.symbol_table.get_symbol_type(val) and str(type(self.symbol_table.get_symbol_type(val))) != "<class 'antlr4.tree.Tree.TerminalNodeImpl'>") else val
                print(type(val))
                results.append(val)
        for result in results:
            if result in self.errors:
                return "methodError"
        print("visitMethodCall results: ",results)
        print("=============================")
        return results


    # Visit a parse tree produced by YAPLParser#nestedLet.
    def visitNestedLet(self, ctx:YAPLParser.NestedLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        print("visitLetIn")
        print(ctx.ID().getText())
        print(ctx.TYPE().getText())
        print("=============================")
        if str(ctx.TYPE().getText()) == "Int":
            self.symbol_table.add_symbol(ctx.ID().getText(),ctx.TYPE().getText(),width=8)
        elif  str(ctx.TYPE().getText()) == "Char":
            self.symbol_table.add_symbol(ctx.ID().getText(),ctx.TYPE().getText(),width=4)
        elif str(ctx.TYPE().getText()) == "Bool":
            self.symbol_table.add_symbol(ctx.ID().getText(),ctx.TYPE().getText())
        # print("self.actual_method: ",self.actual_method)
        #agregarlo en su contains
        
        contains = self.symbol_table.get_contains(self.actual_method)
        array = []
        if contains == None:
            array.append(ctx.ID().getText())
        else:
            for contain in contains:
                array.append(contain)
            array.append(ctx.ID().getText())
        
        self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        
        result = self.visit(ctx.expr())
        print("visitLetIn result: ",result)
        return result
        

    # Visit a parse tree produced by YAPLParser#letAssignLet.
    def visitLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letAssignIn.
    def visitLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        return self.visitChildren(ctx)



del YAPLParser