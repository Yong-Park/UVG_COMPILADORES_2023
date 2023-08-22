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
        self.actualAmbit = "Global"
        self.errors = ["whileError","DobleMain","newError","invertNotInt","inheritProblem","noMain","boolAr","intchar","charAr","assignEr","notequal","noValue","ifError","notLessorequal","notLess","methodError","noMethodAssign"]

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
        elif self.startType == "invertNotInt":
            message = "No es posible realizar la inversa ya que no es un tipo Int"
        elif self.startType == "newError":
            message = "No es posible debido a que el type para el new no existe"
        elif self.startType == "DobleMain":
            message = "No es posible que hayan mas de 1 Main y main"
        elif self.startType == "whileError":
            message = "No es posible, error en el while"
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
        print("\nDefClase visitado")
        defclaseClass = ctx.CLASS()
        # print(defclaseClass)
        
        #definir la clase actual en la que esta
        
        defclaseTypeList = ctx.TYPE()
        classtype = defclaseTypeList[0].getText()
        # print(classtype)
        print("classtype type: ", classtype)
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
            
            #revisar que no sea recursivo
            if inheritPosition == classtype:
                return "methodError"
            
            #revisar si Main ya existe
            existMain = self.symbol_table.contains_symbol("Main")
            existmain = self.symbol_table.contains_symbol("main")
            if not existMain and not existmain: 
                if len(variable_array) > 0: 
                    self.symbol_table.add_symbol(classtype, defclaseClass, inherits=inheritPosition, contains=variable_array, ambit="Global")
                else:
                    self.symbol_table.add_symbol(classtype, defclaseClass, inherits=inheritPosition)
                # print(inheritPosition)
                if str(inheritPosition) == "IO":
                    pass
                else:
                    print("inheritPosition: ",inheritPosition)
                    if self.symbol_table.contains_symbol(str(inheritPosition)) and str(self.symbol_table.get_symbol_type(str(inheritPosition))) == "class" and str(classtype) != "Main":
                        print("inheritPosition si existe")
                        typeContains = self.symbol_table.get_contains(self.actual_class)
                        typeInheritContains = self.symbol_table.get_contains(inheritPosition)
                        print("visitDefClase typeContains: ",typeContains)
                        print("visitDefClase typeInheritContains: ",typeInheritContains)
                        array = []
                        if typeContains == None:
                            array.extend(typeInheritContains)
                        else:
                            array.extend(typeContains)
                            array.extend(typeInheritContains)
                            
                        self.symbol_table.add_symbol(classtype,defclaseClass,contains=array)
                        
                        
                        pass
                    else:
                        print("inheritPosition No existe")
                        return "inheritProblem"
            else:
                return "DobleMain"
                
        else:
            if len(variable_array) > 0:
                self.symbol_table.add_symbol(classtype, defclaseClass,contains=variable_array,ambit="Global")
            else:
                self.symbol_table.add_symbol(classtype, defclaseClass,ambit="Global")
        
        defclaseType = None
        tipos = ctx.feature()
        results = []
        for tipo in tipos:
            self.actualAmbit = "Global"
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
        print("\nvisitMethod")
        self.actualAmbit = "Local"
        self.forml_type = False
        method_name = ctx.ID().getText()
        method_type = ctx.TYPE().getText()
        self.symbol_table.add_symbol(method_name, method_type,ambit="Local")
        formlExist = ctx.formal()
        # print("method_name type: ", type(method_name))
        # print("method_type type: ", type(method_type))
        
        self.actual_method = method_name
        self.actual_method_type = method_type
        print('method_name: ', method_name, '\n')
        print('method_type: ', method_type, '\n')
        
        self.methodRecieves = []
        for form in formlExist:
            res= self.visit(form)
            if res in self.errors:
                print("visitMethod found error: ",res)
                return res
            
        if len(self.methodRecieves) > 0:
            #revisar si el metodo existe pero tiene que el recieves es falso o none
            methodHasRecieve = self.symbol_table.get_recieves(method_name)
            if methodHasRecieve == False:
                self.symbol_table.add_symbol(method_name,method_type,recieves=self.methodRecieves)
            #revisar si el class es un inhertis
            classIsInhertis = self.symbol_table.get_inherits(self.actual_class)
            if classIsInhertis: 
                classInheritContains = self.symbol_table.get_contains(classIsInhertis)
                if classInheritContains:
                    if method_name in classInheritContains:
                        #revisar que el forml sea del mismo tipo que el que tiene adentro y el tipo de valor de regreso
                        classInhertisMethodRecieves = self.symbol_table.get_recieves(method_name)
                        print("visitMethod classInhertisMethodRecieves: ",classInhertisMethodRecieves)
                        print("visitMethod self.methodRecieves: ",self.methodRecieves)
                        if classInhertisMethodRecieves != self.methodRecieves:
                            return "methodError"
                        #revisar si regresan el mismo tipo de valor
                        inhertisMethodType = self.symbol_table.get_symbol_type(method_name)
                        if inhertisMethodType != method_type:
                            return "methodError"
        
        # contains = self.symbol_table.get_contains(self.actual_method)
        # recieve = self.symbol_table.get_recieves(self.actual_method)
        # print("visitMethod contains: ",contains)
        # print("visitMethod recieve: ",recieve)    
        
        # self.symbol_table.add_symbol(self.actual_method,self.actual_method_type)
        
        # Agregar el método a la Tabla de Símbolos
        
        # print("symbol table: ", self.symbol_table)
        # print("++++++++++++++++++++++") 
        # Continuar con el recorrido del árbol sintáctico
        method_expr_type = self.visit(ctx.expr())
        # method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
        print("method expr type: ", method_expr_type)
        print("=============================")
        # voidBasicType = ["Void","Int","Char","Bool"]
        #revisar si tiene un valor igual al tipo del metodo 
        if type(method_expr_type) == list:
            
            if self.actual_method_type in method_expr_type:
                return self.actual_method_type
            else:
                # #revisar si su tipo es SELF_TYPE
                # if self.actual_method_type == "SELF_TYPE":
                #     # return method_expr_type
                #     for types in voidBasicType:
                #         if types in method_expr_type:
                #             return types
                return "methodError"
        else:
            if method_expr_type in self.errors:
                return method_expr_type
            
            if self.actual_method_type == method_expr_type:
                return self.actual_method_type
            else:
                method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
                if self.actual_method_type == method_expr_type:
                    return self.actual_method_type
                else:
                    return "methodError"
       
    # Visit a parse tree produced by YAPLParser#property.
    def visitProperty(self, ctx:YAPLParser.PropertyContext):
        print("\nvisitProperty")
        self.actualAmbit = "Local"
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        
        var_expr = self.visit(ctx.expr()) if ctx.expr() != None else []
        var_assign = ctx.ASSIGN()
        print("var_expr: ",var_expr)
        print('var_name: ', var_name)
        print('var_type: ', var_type)
        print('var_assign: ', var_assign, '\n')
        #revisar que la variable si no es int, char o bool sea algo que exista en la tabla
        if str(var_type) not in ["Int","Char","Bool","String"]:
            print("toca buscar")
            if self.symbol_table.contains_symbol(var_type):
                print("Si existe")
                pass
            else:
                return "noMethodAssign"
        
        #asignar el width setun si tipo
        if var_type == "Int":
            self.symbol_table.add_symbol(var_name, var_type,width=8, ambit="Local")
        elif var_type == "Char":
            self.symbol_table.add_symbol(var_name, var_type,width=4, ambit="Local")
        elif var_type == "String":
            self.symbol_table.add_symbol(var_name, var_type,width=2, ambit="Local")
        else:
            self.symbol_table.add_symbol(var_name, var_type, ambit="Local")
            
        
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
        print("\nvisitForml")
        idtext = ctx.ID().getText()
        tipo = ctx.TYPE().getText()
        print("idtext: ",idtext)
        print("tipo: ",tipo)
        self.symbol_table.add_symbol(idtext,tipo,ambit="Local")
        if tipo not in ["Int","Char","Bool","Object"]:
            print("buscar si el tipo existe")
            tipoExiste = self.symbol_table.contains_symbol(tipo)
            print("tipoExiste: ",tipoExiste)
            if tipoExiste:
                classContains = self.symbol_table.get_contains(tipo)
                formContains = self.symbol_table.get_contains(idtext)
                formArray = []
                if formContains == None:
                    formArray.extend(classContains)
                else:
                    formArray.extend(formContains)
                    formArray.extend(classContains)
                self.symbol_table.add_symbol(idtext,tipo,contains=formArray)
            else:
                print("visitForml found: methodError")
                return "methodError"
        
        print("self.actual_method: ",self.actual_method)
        # print("self.actual_method Type: ",type(self.actual_method))
        print("self.actual_method_type: ",self.actual_method_type)
        
        #agregarlo en su contains
        contains = self.symbol_table.get_contains(self.actual_method)
        array = []
        if contains == None:
            array.append(idtext)
        else:
            array.append(idtext)
            for ele in contains:
                array.append(str(ele))
        
        self.methodRecieves.append(tipo)
        
        print("visitForml array: ",array)
        print("visitForml self.methodRecieves: ",self.methodRecieves)
        self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        print("=============================")
        
        
    
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
        print("\nvisitSub")
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
        print("\nvisitVoid")
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
        print("\nvisitInvert")
        value = self.visit(ctx.expr())
        value = self.symbol_table.get_symbol_type(value) if self.symbol_table.get_symbol_type(value) else value
        print("visitInvert value: ",value)
        if value == "Int":
            return "Int"
        else:
            return "invertNotInt"
        
        


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        return "Char"


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        print("\nVisiting Mul node")
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
        print("\nFactExpr: ",expresion)
        print("=============================")
        return expresion


    # Visit a parse tree produced by YAPLParser#lteq.
    def visitLteq(self, ctx:YAPLParser.LteqContext):
        left = self.visit(ctx.expr(0))
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        if left_type == "Int" and right_type == "Int":
            return "Bool"
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
            return "Bool"
        else:
            return "notLess"

    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        print("\nwhile visitado")
        whileIsBool = False
        
        expresions = ctx.expr()
        if len(expresions) != 2:
            return "whileError"
        
        whilestate = expresions[0] #esto es lo del while que tiene que ser bool
        print("corriendo while")
        whileResult = self.visit(whilestate)
        print("while result: ",whileResult)
        
        if type(whileResult) == list:
            if "Bool" not in whileResult:
                return "whileError"
            else:
                whileIsBool = True
        else:
            if whileResult != "Bool":
                return "whileError"
            else:
                whileIsBool = True
                
        loopstate = expresions[1] #esto es el contenido del loop
        print("corriendo loop")
        loopResult = self.visit(loopstate)
        
        
        print("visitWhile results (loop): ",loopResult)
        print("=============================")
        
        if whileIsBool:
            return "Object"
        else:
            return "whileError"


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
        print("\nvisitando equal")
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
        right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.get_symbol_type(right) else right
        # print("right equal", right)
        if right_type in ["Int","Char","Bool"]:
            if left_type == right_type:
                return "Bool"
            else:
                return "notequal"
        else:
            return "Bool"


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        print("\nvisitNot")
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
        print("\nvisitNewObject")
        value = ctx.TYPE().getText()
        print(value)
        #revisar que si existe en new type
        if value not in ["Object"]:
            existNew = self.symbol_table.contains_symbol(value)
            print("existNew: ",existNew)
        else:
            existNew = True
        print("=============================")
        if existNew:
            return value
        else:
            return "newError"


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
        
        print("\nvisitBlock result: ", results)
        print("=============================")
        for result in results:
            if result in self.errors:
                return result
            
        return results


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        print("\nvisitLet")
        result = self.visit(ctx.let_expr())
        print("visitLet result: ",result)
        return result


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        # print("id visitado")
        value = ctx.ID().getText()
        print("\nid value: ", value)
        #revisar si es de tipo self
        if str(value) == "self":
            print("self.actual_method: ",self.actual_method)
            print("self.actual_method_type: ",self.actual_method_type)
            self.symbol_table.add_symbol(value, self.actual_method_type,ambit=self.actualAmbit)
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
      
            return str(self.actual_method_type)
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
        print("\nif visitado")
        expresions = ctx.expr()
        
        #if there are not three expresion return error
        if len(expresions) != 3:
            return "ifError"
        
        ifstate = expresions[0] #if
        print("corriendo el if")
        ifResult = self.visit(ifstate)
        
        if type(ifResult) == list:
            if "Bool" not in ifResult:
                return "ifError"
        else:
            if ifResult != "Bool":
                return "ifError"
            
        print("ifResult: ",ifResult)
            
        #obtener los resultados de elstate y thenstate
        thenstate = expresions[1] #then
        print("Corriendo el then")
        thenResult = self.visit(thenstate)
        
        elsestate = expresions[2] #else
        print("Corriendo el else")
        elseResult = self.visit(elsestate)
        
        #agregar los resultados en el results
        results = []
        
        if type(thenResult) == list:
            results.extend(thenResult)
        else:
            results.append(thenResult)
            
        if type(elseResult) == list:
            results.extend(elseResult)
        else:
            results.append(elseResult)
        
        # for expresion in expresions:
        #     val = self.visit(expresion)
        #     if type(val) == list:
        #         results.extend(val)
        #     else:
        #         results.append(val)
        print("visitIf results: ",results)
        print("=============================")
        #revisar que de los resultados obtenido no haya ninguno que forme parte de algun error
        for result in results:
            if result in self.errors:
                return "ifError"
            
        return results
        
    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        print("\nvisitOwnMethodCall")
        message = "methodError"
        expresions = ctx.expr()
        
        inherist = self.symbol_table.get_inherits(self.actual_class)
        print("visitOwnMethodCall inherist: ",inherist)
        
        id = ctx.ID().getText() 
        print("visitOwnMethodCall id: ",id)
        # print("visitOwnMethodCall id Type: ",type(id))

        #tiene el io inheritado
        if str(inherist) == "IO":
            if id == "out_string":
                first = expresions.pop(0)
                firstType = self.visit(first)
                if firstType == "Char":
                    message = "SELF_TYPE"
                
            elif id == "out_int":
                first = expresions.pop(0)
                firstType = self.visit(first)
                if firstType == "Int":
                    message = "SELF_TYPE"
                else:
                    firstType = self.symbol_table.get_symbol_type(firstType) if self.symbol_table.get_symbol_type(firstType) else firstType
                    if firstType == "Int":
                        message = "SELF_TYPE"
                    
            elif id == "in_string":
                message = "String"
            elif id == "in_int":
                message = "Int"
                    
        #cumple con alguno de los string o object
        if id == "abort":
            message = "Object"
        elif id == "type_name":
            message = "Char"
        elif id == "copy":
            message = "SELF_TYPE"
        elif id == "length":
            message = "Int"
        elif id == "concat":
            second = expresions.pop(0)
            secondType = self.visit(second)
            if secondType == "Char":
                message = "Char"
        elif id == "substr":
            second = expresions.pop(0)
            secondType = self.visit(second)
            third = expresions.pop(0)
            thirdType = self.visit(third)
            
            if secondType == "Int" and thirdType == "Int":
                message = "Char"
                
        #el id es un metodo que se esta volviendo a llamar?
        actualClassContains = self.symbol_table.get_contains(self.actual_class)
        if actualClassContains != None:
            if id in actualClassContains:
                first = expresions.pop(0) if len(expresions) > 0 else False
                if first != False:
                    firstType = self.visit(first)
                    print("visitOwnMethodCall firstType: ",firstType)
                    print("visitOwnMethodCall id: ",id , " :", type(id))
                    recieveMethod = self.symbol_table.get_recieves(id)
                    print("visitOwnMethodCall recieveMethod: ",recieveMethod)

                    if type(firstType) != list:
                        firstType = [firstType]
                    
                    if len(firstType) == len(recieveMethod):
                        for ft in firstType:
                            if ft in recieveMethod:
                                message = str(self.symbol_table.get_symbol_type(id))
                            else:
                                ft = self.symbol_table.get_symbol_type(ft) if self.symbol_table.get_symbol_type(ft) else ft
                                if ft in recieveMethod:
                                    message = str(self.symbol_table.get_symbol_type(id))
                                else:
                                    message = "methodError"
                                    break
                
        print("visitOwnMethodCall message: ",message)
        
        
        return message


    # Visit a parse tree produced by YAPLParser#INTEGER.
    def visitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        return "Int"


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        print("\nassign visitado")
        expresion = self.visit(ctx.expr())
        expresionType = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        left = ctx.ID().getText()
        left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.get_symbol_type(left) else "noValue"
        print("expresion: ",expresion)
        print("expresionType: ",expresionType)
        # expresion = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        # print("expresion later: ",expresion)
        print("left: ",left)
        print("left_type: ",left_type)
        
        if expresionType in self.errors:
            return expresionType
        
        if expresionType not in ["Int","Char","Bool","Void","Object"]:
            #obtener los contains
            array = []
            expresionContains = self.symbol_table.get_contains(expresion)
            leftContains = self.symbol_table.get_contains(left)

            if leftContains == None:
                if expresionContains != None:
                    array.extend(expresionContains)
            else:
                array.extend(leftContains)
                array.extend(expresionContains)

            self.symbol_table.add_symbol(left,left_type,contains=array)
            
        #revisar si expresion inhertis de algun otro y si es asi convertirlo en lista lo de expresion
        exprInhertis = self.symbol_table.get_inherits(expresion)
        print("expresion type: ",type(expresion))
        if exprInhertis !=False:
            print("exprInhertis: ",exprInhertis)
            expresion = [expresion]
            expresion.append(str(exprInhertis))
        while exprInhertis != False:
            expr = expresion[len(expresion)-1]
            print("expr: ",expr)
            print("expr type: ",type(expr))
            exprInhertis = self.symbol_table.get_inherits(expr)
            print("exprInhertis: ",exprInhertis)
            if exprInhertis != False:
                if str(exprInhertis) not in expresion:
                    expresion.append(str(exprInhertis))
                else:
                    exprInhertis = False
            
        
        print("=============================")
        if type(expresion) == list:
            print("es una lista")
            print("left_type: ",left_type)
            print("expresion: ",expresion)
            if left_type in expresion:
                return left_type
            return "assignEr"
        else:
            print("No es una lista")
            if str(left_type) == str(expresion):
                print("Se esta regresando este: ",left_type)
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
        
        inherist = self.symbol_table.get_inherits(self.actual_class)
        print("visitMethodCall inherist: ",inherist)
        
        #obtener el primer tipo y segun ello trabajarlo
        first = expresions.pop(0)
        firstType = self.visit(first)
        
        print("\nvisitMethodCall")
        message = "methodError"
        # results=[] 
        
        id = ctx.ID().getText()
        print("visitMethodCall id: ",id)
        print("visitMethodCall firstType",firstType)
        if firstType in self.errors:
            return firstType
        
        if id == "abort":
            message = "Object"
        elif id == "type_name":
            message = "Char"
        elif id == "copy":
            message = "SELF_TYPE"
        elif id == "length":
            message = "Int"
        elif id == "concat":
            second = expresions.pop(0)
            secondType = self.visit(second)
            if secondType == "Char":
                message = "Char"
        elif id == "substr":
            second = expresions.pop(0)
            secondType = self.visit(second)
            third = expresions.pop(0)
            thirdType = self.visit(third)
            # print("substr secondType: ",secondType)
            # print("substr thirdType: ",thirdType)
            if secondType == "Int" and thirdType == "Int":
                message = "Char"
        elif id == "isNil":
            message = "Bool"
        
        if str(inherist) == "IO":
            if id == "out_string":
                first = expresions.pop(0)
                firstType = self.visit(first)
                
                if firstType == "Char":
                    message = "SELF_TYPE"
            elif id == "out_int":
                first = expresions.pop(0)
                firstType = self.visit(first)
                
                if firstType == "Int":
                    message = "SELF_TYPE"
            elif id == "in_string":
                message = "Char"
            elif id == "in_int":
                message = "Int"
             
        #revisar si el id es un metodo llamda utuilziando la primera expresion   
        firstContains = self.symbol_table.get_contains(firstType)
        print("visitMethodCall firstContains: ", firstContains)
        if firstContains != None:
            if id in firstContains:
                nextArray = []
                while(len(expresions) > 0):
                    next = expresions.pop(0) if len(expresions) > 0 else False
                    if next != False:
                        nextType = self.visit(next)
                        print("visitMethodCall nextType: ",nextType)
                        nextType = self.symbol_table.get_symbol_type(nextType) if self.symbol_table.get_symbol_type(nextType) else nextType
                        print("visitMethodCall nextType after: ",nextType)
                        
                        if type(nextType) != list:
                            nextArray.append(nextType)
                        else:
                            nextArray.extend(nextType)
                            
                idRecieves = self.symbol_table.get_recieves(id)
                print("visitMethodCall idRecieves: ",idRecieves)
                if idRecieves != False:
                    print("visitMethodCall nextArray: ",nextArray)
                    if len(nextArray) == len(idRecieves):
                        for nt in nextArray:
                            if nt in idRecieves:
                                message = str(self.symbol_table.get_symbol_type(id))
                            else:
                                message = "methodError"
                                break
                else:
                    message = str(self.symbol_table.get_symbol_type(id))
        print("visitMethodCall message original: ",message)
        if message == "SELF_TYPE":
            message = firstType
        
        print("visitMethodCall message if SELF_TYPE: ",message)
        return message

        
        # for expreion in expresions:
        #     # print("visitMethodCall")
        #     val = self.visit(expreion)
        #     print("visitMethodCall: ",val)
        #     if type(val) == list:
        #         results.extend(val)
        #     else:
        #         # print("self.actual_class: ",self.actual_class)
        #         # print("val: ",val)
        #         # if self.symbol_table.contains_element(self.actual_class,val):
        #         #     print("si contiene ")
        #         val = self.symbol_table.get_symbol_type(val) if (self.symbol_table.get_symbol_type(val) and str(type(self.symbol_table.get_symbol_type(val))) != "<class 'antlr4.tree.Tree.TerminalNodeImpl'>") else val
        #         print(type(val))
        #         results.append(val)
        # for result in results:
        #     if result in self.errors:
        #         return "methodError"
        # print("visitMethodCall results: ",results)
        # print("=============================")
        # return results


    # Visit a parse tree produced by YAPLParser#nestedLet.
    def visitNestedLet(self, ctx:YAPLParser.NestedLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        print("\nvisitLetIn")
        id = ctx.ID().getText()
        letinType = ctx.TYPE().getText()
        print("id: ",id)
        print("letinType: ",letinType)
        print("=============================")
        if str(letinType) == "Int":
            self.symbol_table.add_symbol(id,letinType,width=8,ambit="Local")
        elif  str(letinType) == "Char":
            self.symbol_table.add_symbol(id,letinType,width=4,ambit="Local")
        elif str(letinType) == "Bool":
            self.symbol_table.add_symbol(id,letinType,ambit="Local")
        # print("self.actual_method: ",self.actual_method)
        #agregarlo en su contains
        
        contains = self.symbol_table.get_contains(self.actual_method)
        # recieve = self.symbol_table.get_recieves(self.actual_method)
        # print("visitLetIn recieves: ",recieve)
        array = []
        if contains == None:
            array.append(id)
        else:
            array.extend(contains)
            array.append(id)
        
        self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        
        result = self.visit(ctx.expr())
        print("visitLetIn result: ",result)
        return result
        

    # Visit a parse tree produced by YAPLParser#letAssignLet.
    def visitLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        print("\nvisitLetAssignLet")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letAssignIn.
    def visitLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        print("\nvisitLetAssignIn")
        id = ctx.ID().getText()
        typevisit = ctx.TYPE().getText()
        print("visitLetAssignIn typevisit: ",typevisit)
        
        resutls = []
        
        self.symbol_table.add_symbol(id,typevisit,ambit="Local")
        
        print("self.actual_method: ", self.actual_method)
        
        #agregar el nuevo simbolo en contians del metodo
        contains = self.symbol_table.get_contains(self.actual_method)
        print("contains: ",contains)
        array = []
        if contains == None:
            array.append(id)
        else:
            array.append(id)
            for contain in contains:
                array.append(str(contain))
        
        self.symbol_table.add_symbol(self.actual_method, self.actual_method_type, contains=array)
        
        #realizar la asignacion
        expresions = ctx.expr()
        assignExpresion = expresions[0]
        
        assignValue = self.visit(assignExpresion)
        print("visitLetAssignIn assignValue: ",assignValue)
        
        if type(assignValue) ==  list:
            if typevisit in assignValue:
                resutls.extend(assignValue)
                resutls.append(typevisit)
            else:
                resutls.append("assignEr")
        else:
            assignValue = self.symbol_table.get_symbol_type(assignValue) if self.symbol_table.get_symbol_type(assignValue) else assignValue
        
            if assignValue == typevisit:
                resutls.append(typevisit)
            else:
                resutls.append("assignEr")
                
        #obtener la otra expr
        exprResult = expresions[1]
        exprValue = self.visit(exprResult)
        
        if type(exprValue) == list:
            resutls.extend(exprValue)
        else:
            exprValue = self.symbol_table.get_symbol_type(exprValue) if self.symbol_table.get_symbol_type(exprValue) else exprValue
            resutls.append(exprValue)
        
        print("visitLetAssignIn results: ",resutls)
        return resutls



del YAPLParser