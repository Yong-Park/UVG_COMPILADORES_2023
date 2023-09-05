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
        self.bytesSize = 0
        self.startType = None
        self.actual_method = None
        self.actual_class = None
        self.actual_method_type = None
        self.actualAmbit = None
        self.errors = ["ArithError","BothNotBool","RepeatedValue","assignError","methodValuesNotSame","NotSameLenght","TypeNotExist","notContainsType","diferentMethodType","diferentRecievers","recursiveInherit","whileError","DobleMain","newError","invertNotInt","inheritProblem","noMain","boolAr","intchar","charAr","assignEr","notequal","noValue","ifError","notLessorequal","notLess","methodError","noMethodAssign"]
            
    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        print("start visitado")
        
        message = []
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
        # print(self.symbol_table)
        #realizar ultima revision si existe una clase Main y un metodo main en la clase Main
        MainExist = self.symbol_table.contains_mains()

        # print("MainExist: ",MainExist)
        print("=============================")
        print("visitStart results: ",results)
        for result in results:
            if result in self.errors:
                self.startType = result
            else:
                self.startType = "Int"
                
            # if self.startType == None:
            #     self.startType = results[0]
            print("self.startType: ",self.startType)
            if self.startType == "Int":
                pass
            elif self.startType == "String":
                pass
            elif self.startType == "Bool":
                pass
            elif self.startType == "boolAr":
                message.append("no se puede operar operaciones aritmetricas entre Bools\n")
            elif self.startType == "intchar":
                message.append("no se puede operar operaciones aritmetricas Int y String\n")
            elif self.startType == "charAr":
                message.append("no se puede operaciones aritmetricas entre Strings\n")
            elif self.startType == "assignEr":
                message.append("no se puede asignar variables ya que no es del mismo tipo\n")
            elif self.startType == "notequal":
                message.append("no se puede asignar variables ya que no es del mismo tipo\n")
            elif self.startType == "noValue":
                message.append("no se puede debido a una variable no existe o no puede ser utilizada en ese entorno\n")
            elif self.startType == "ifError":
                message.append("la funcion de if esta fallando\n")
            elif self.startType == "notLessorequal":
                message.append("No es posible, alguno de los valores al probar <= no es de tipo Int\n")
            elif self.startType == "notLess":
                message.append("No es posible, alguno de los valores al probar < no es de tipo Int\n")
            elif self.startType == "methodError":
                message.append("El metodo no esta creado o no existe en este ambiente que esta\n")
            elif self.startType == "noMethodAssign":
                message.append("El metodo no existe y por ello no se le puede asignar a una variable\n")
            elif self.startType == "inheritProblem":
                message.append("Problema con la herencia, no existe esta clase para heredar\n")
            elif self.startType == "invertNotInt":
                message.append("No es posible realizar la inversa ya que no es un tipo Int\n")
            elif self.startType == "newError":
                message.append("No es posible debido a que el type para el new no existe\n")
            elif self.startType == "DobleMain":
                message.append("No es posible que hayan mas de 1 Main y main\n")
            elif self.startType == "whileError":
                message.append("No es posible, error en el while\n")
            elif self.startType == "recursiveInherit":
                message.append("No es posible que la clase herede de la misma, esto causa recurrencia\n")
            elif self.startType == "diferentRecievers":
                message.append("No es posible sobre escribir el metodo debido a que el tipo de asignacion (reciever) no es el mismo\n")
            elif self.startType == "diferentMethodType":
                message.append("No es posible sobre escribir este metodo debido a que son del distintos tipos\n")
            elif self.startType == "notContainsType":
                message.append("No es posible debido a que no regresa el tipo que fue definido en el metodo\n")
            elif self.startType == "TypeNotExist":
                message.append("No es posible dar este valor al la variable debido a que este tipo no existe\n")
            elif self.startType == "NotSameLenght":
                message.append("No es posible debido a que la cantidad de valores que se esta ingresando en el metodo llamado supera o es menor al lo que se pide\n")
            elif self.startType == "methodValuesNotSame":
                message.append("No es posible debido a que las variables que se estan utilizando son distintos al del metodo\n")
            elif self.startType == "assignError":
                message.append("No es posible debido a que el tipo que esta utilizando no existe\n")
            elif self.startType == "RepeatedValue":
                message.append("No es posible ya que esta variable ya esta definida anteriormente\n")
            elif self.startType == "BothNotBool":
                message.append("Ambos deben de ser de tipo bool")
            elif self.startType == "ArithError":
                message.append("No es posible realizar esta operacion aritmetica")
        if MainExist == False:
            message.append("Error No existe el Main o main\n")
        print("self.startType to send: ",message)
        print("=============================")

        return message


    # Visit a parse tree produced by YAPLParser#defClase.
    def visitDefClase(self, ctx:YAPLParser.DefClaseContext):
        print("\nDefClase visitado")
        defclaseClass = ctx.CLASS()
        print("defclaseClass: ",defclaseClass)
        
        #definir la clase actual en la que esta
        
        defclaseTypeList = ctx.TYPE()
        classtype = defclaseTypeList[0].getText()
        # print(classtype)
        print("classtype type: ", classtype)
        self.actual_class = classtype
        #guardar el tipo de ambiente en el que esta
        self.actualAmbit = classtype
        
        defclaseInherits = ctx.INHERITS() #revisar si existe la funcion inherits
        # print(defclaseInherits)
        if defclaseInherits:
            inheritPosition = defclaseTypeList[1]
            
            #revisar que no sea recursivo
            if inheritPosition == classtype:
                return "recursiveInherit"
            
            #revisar si Main ya existe
            existMain = self.symbol_table.contains_symbol("Main","Main")
            existmain = self.symbol_table.contains_symbol("main","Main")
            
            # aqui se revisa si no existe ya definido el Main y su main de ello porque si existe significa que anteriormente ya se definio y por ello se esta repetiendo Mains
            if not existMain and not existmain: 
                #agregarlo en la tabla la clase que tiene una heredacion
                if str(inheritPosition) == "IO":
                    self.symbol_table.add_symbol(classtype, type=defclaseClass, inherits=inheritPosition, ambit=self.actualAmbit)
                else:
                    print("inheritPosition: ",inheritPosition)
                    #se revisa en este caso que si no es IO sea una clase que existe en la tabla de simbolos y que el classtype no sea Main ya que main solo puede heredar de IO
                    if self.symbol_table.contains_class(str(inheritPosition)) and str(classtype) != "Main":
                        print("inheritPosition si existe")
                        self.symbol_table.add_symbol(classtype, type=defclaseClass, inherits=inheritPosition, ambit=self.actualAmbit)
                        #añadir el valor de inherti position a su respectiva clase
                        # self.symbol_table.change_symbol_value(classtype,self.actual_class,"inherits",inheritPosition)

                    else:
                        print("inheritPosition No existe")
                        return "inheritProblem"
            else:
                return "DobleMain"
                
        else:
            self.symbol_table.add_symbol(classtype, type=defclaseClass,ambit=self.actual_class)
        
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
        print("\nvisitMethod")
        
        size_method = 0
        self.forml_type = False
        
        method_name = ctx.ID().getText()
        method_type = ctx.TYPE().getText()
        
        self.actual_method = method_name
        self.actual_method_type = method_type

        #revisar si el method_type existe si no es tipo Int, Char, Bool, Object, Void, SELF_TYPE
        if method_type not in ["Int","String","Bool","Object","Void","SELF_TYPE"]:
            #revisar si existe
            method_type_Exist = self.symbol_table.contains_class(method_type)
            print("visitMethod method_type_Exist: ",method_type_Exist)
            #si existe es porque se encontro y es de tipo class
            if method_type_Exist:
                pass
            else:
                return "assignError"
        else:
            if method_type == "Int":
                size_method += 4

        #agregar el metodo
        self.symbol_table.add_symbol(method_name, method_type,ambit=self.actual_class)
        
        #actualizar el ambito que seria la clase mas el nombre del metodo
        self.actualAmbit = self.actual_class + "." + method_name
        
        #revisar si el metodo recibe parametros
        formlExist = ctx.formal()

        print('method_name: ', method_name, '\n')
        print('method_type: ', method_type, '\n')
        
        # en este se guardara los parametros que recibe el metodo
        self.methodRecieves = []
        for form in formlExist:
            res= self.visit(form)
            if res in self.errors:
                print("visitMethod found error: ",res)
                return res
        print("visitMethod self.methodRecieves: ",self.methodRecieves)
        if len(self.methodRecieves) > 0:
            print("el len de self.methodrecieves si es mas de 1")
            #agregar el recieves los parametros que tendria ese metodo
            self.symbol_table.change_symbol_value(method_name,self.actual_class,"recieves",self.methodRecieves)
            
        # visitar el expr de la funcion
        method_expr_type = self.visit(ctx.expr())
        
        # method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
        print("method expr type: ", method_expr_type)
        print("self.actualAmbit: ",self.actualAmbit)
        print("=============================")
        
        #revisar si tiene un valor igual al tipo del metodo 
        if type(method_expr_type) == list:
            #revisar si en los returns tiene un error
            for mey in method_expr_type:
                if mey in self.errors:
                    return mey
            
            print("visitMethod es un tipo de lista")
            if str(method_type) in method_expr_type:
                return method_type
            else:
                print("no fue igual")
                #revisar si el self.actual_method_type es tipo Bool o Int y si es asi revisar si en las respuestas ahi un Int O Bool
                if str(method_type) == "Int":
                    if "Bool" in method_expr_type:
                        return method_type
                    else:
                        return "notContainsType"
                elif str(method_type) == "Bool":
                    if "Int" in method_expr_type:
                        return method_type
                    else:
                        return "notContainsType"
                else:
                    return "notContainsType"
        else:
            print("visitMethod no es un tipo de lista")
            if method_expr_type in self.errors:
                return method_expr_type
            
            if method_type == method_expr_type:
                return method_type
            else:
                if str(method_type) == "Int" and str(method_expr_type) == "Bool":
                    return method_type
                elif str(method_type) == "Bool" and str(method_expr_type) == "Int":
                    return method_type
                else:
                    return "notContainsType"
       
    # Visit a parse tree produced by YAPLParser#property.
    def visitProperty(self, ctx:YAPLParser.PropertyContext):
        print("\nvisitProperty")
        var_name = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        
        self.actual_method = var_name
        self.actual_method_type = var_type
        
        self.symbol_table.add_symbol(var_name, type=var_type, ambit=self.actual_class)
        #cambiar el tipo de ambiente para que ya sea del clase mas metodo
        self.actualAmbit = self.actual_class + "." + var_name
        
        var_expr = self.visit(ctx.expr()) if ctx.expr() != None else []
        var_assign = ctx.ASSIGN()
        print("var_expr: ",var_expr)
        print('var_name: ', var_name)
        print('var_type: ', var_type)
        print('var_assign: ', var_assign, '\n')
        
        
        #revisar si el var_expr es un tipo de lista
        if type(var_expr) == list:
            #revisar que el var_expr no este en errores
            for ve in var_expr:
                if ve in self.errors:
                    return ve

        else:
            #revisar que el var_expr no sea un tipo de error
            if var_expr in self.errors:
                return var_expr
        #revisar que la variable si no es int, char o bool sea algo que exista en la tabla
        if str(var_type) not in ["Int","String","Bool","Object","Void","SELF_TYPE"]:
            print("toca buscar")
            if self.symbol_table.contains_class(var_type):
                print("Si existe")
                pass
            else:
                print("no existe")
                return "noMethodAssign"
            
        #asignar el width setun si tipo
        if var_type == "Int":
            width = 4
        elif var_type == "String":
            width = 2
        elif var_type == "Bool":
            width = 2
        else:
            width = 2
        
        # revisar si es del mismo tipo la asignacion cuando se realice
        if var_assign != None:
            #revisar si var_expr es un tipo de lista
            if type(var_expr) == list:
                if var_type not in var_expr:
                    print("visitProperty assignEr")
                    return "assignEr"
            else:            
                #si var_expr no es un tipo de int o algo asi revisa para conseguirlo de lo contrario permanece
                var_expr = self.symbol_table.get_symbol_value(var_expr,self.actual_class,"type") if self.symbol_table.get_symbol_value(var_expr,self.actual_class,"type")  else var_expr
                if var_type != var_expr:
                    print("visitProperty assignEr")
                    return "assignEr"

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
        self.symbol_table.add_symbol(idtext,tipo,ambit=self.actualAmbit)
        if tipo not in ["Int","String","Bool","Object"]:
            print("buscar si el tipo existe")
            tipoExiste = self.symbol_table.contains_class(tipo)
            print("tipoExiste: ",tipoExiste)
            if tipoExiste:
                pass
            else:
                print("visitForml found: TypeNotExist")
                return "TypeNotExist"
        
        #agregarlo en el method recieves para tener un control de cuales son los parametros que este recibe
        self.methodRecieves.append([idtext,tipo])
        
        print("visitForml self.methodRecieves: ",self.methodRecieves)
        print("=============================")
        
        
    
    # Visit a parse tree produced by YAPLParser#or.
    def visitOr(self, ctx:YAPLParser.OrContext):
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
       
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left
        if right in self.errors:
            return right
        
        if left == "Bool" and right == "Bool":
            return left
        else:
            return "BothNotBool"
    
    # Visit a parse tree produced by YAPLParser#and.
    def visitAnd(self, ctx:YAPLParser.AndContext):
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left
        if right in self.errors:
            return right
        
        if left == "Bool" and right == "Bool":
            return left
        else:
            return "BothNotBool"

    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        print("Visiting Add node")
        
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print('left add: ',left)
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print('right add:', right)


        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left
        if right in self.errors:
            return right
        
        if left == "Int" and right == "Int":
            return left
        elif left == "String" and right == "String":
            return left
        elif left == "Bool" and right == "Int":
            return left
        elif left == "Int" and right == "Bool":
            return left
        elif left == "Bool" and right == "Bool":
            return left
        # errors
        elif left == "Int" and right == "String":
            return "intchar"
        elif left == "String" and right == "Int":
            return "intchar"
        else:
            return "ArithError"


    # Visit a parse tree produced by YAPLParser#sub.
    def visitSub(self, ctx:YAPLParser.SubContext):
        
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))

        print("\nvisitSub")
        print("left: ",left)
        print("right: ",right )
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left
        if right in self.errors:
            return right
        
        if left == "Int" and right == "Int":
            return left
        elif left == "Bool" and right == "Int":
            return left
        elif left == "Int" and right == "Bool":
            return left
        elif left == "Bool" and right == "Bool":
            return left
        # errors
        elif left == "String" and right == "String":
            return "charAr"
        elif left == "Int" and right == "String":
            return "intchar"
        elif left == "String" and right == "Int":
            return "intchar"
        else:
            return "ArithError"


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
        
        # value = self.symbol_table.get_symbol_type(value) if self.symbol_table.get_symbol_type(value) else value
        print("visitInvert value: ",value)
        if str(value) == "Int":
            return "Int"
        else:
            return "invertNotInt"
        
        
    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        print("visitString")
        text = ctx.STRING().getText()
        text = text[1:-1]
        lenText = len(text)
        print("visitString text: ",text)
        self.bytesSize = lenText * 2
        return "String"


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        print("\nVisiting Mul node")
    
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left mul", left)

        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right mul: ",right)
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left
        if right in self.errors:
            return right
        
        if left == "Int" and right == "Int":
            return left
        elif left == "Bool" and right == "Int":
            return right
        elif left == "Int" and right == "Bool":
            return left
        elif left == "Bool" and right == "Bool":
            return left
        # errors
        elif left == "String" and right == "String":
            return "charAr"
        elif left == "Int" and right == "String":
            return "intchar"
        elif left == "String" and right == "Int":
            return "intchar"
        else:
            return "ArithError"



    # Visit a parse tree produced by YAPLParser#factExpr.
    def visitFactExpr(self, ctx:YAPLParser.FactExprContext):
        expresion = self.visit(ctx.expr())
        print("\nFactExpr: ",expresion)
        print("=============================")
        return expresion


    # Visit a parse tree produced by YAPLParser#lteq.
    def visitLteq(self, ctx:YAPLParser.LteqContext):
        print("visitLteq")
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left: ",left)
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right: ",right)
        
        if left == "Int" and right == "Int":
            return "Bool"
        if left == "Int" and right == "Bool":
            return "Bool"
        if left == "Bool" and right == "Int":
            return "Bool"
        if left == "Bool" and right == "Bool":
            return "Bool"
        else:
            return "notLessorequal"
        

    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#lt.
    def visitLt(self, ctx:YAPLParser.LtContext):
        print("visitLt")
        
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left: ",left)
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right: ",right)
        
        if left == "Int" and right == "Int":
            return "Bool"
        if left == "Int" and right == "Bool":
            return "Bool"
        if left == "Bool" and right == "Int":
            return "Bool"
        if left == "Bool" and right == "Bool":
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
        if type(loopResult) == list:
            for x in loopResult:
                if x in self.errors:
                    return x
        else:
            if loopResult in self.errors:
                return loopResult
        
        if whileIsBool:
            return "Object"
        else:
            return "whileError"


    # Visit a parse tree produced by YAPLParser#div.
    def visitDiv(self, ctx:YAPLParser.DivContext):
        print("visitDiv")
        
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left: ",left )
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right: ",right )
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return right
        if left in self.errors:
            return right
        
        if left == "Int" and right == "Int":
            return left
        elif left == "Bool" and right == "Int":
            return left
        elif left == "Int" and right == "Bool":
            return left
        elif left == "Bool" and right == "Bool":
            return left
        # errors
        elif left == "String" and right == "String":
            return "charAr"
        elif left == "Int" and right == "String":
            return "intchar"
        elif left == "String" and right == "Int":
            return "intchar"
        else:
            return "ArithError"


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        print("\nvisitando equal")
        
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
            
        print("left equal", left)
        
        if left in self.errors:
            return  left
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.get_symbol_type(right) else right
        print("right equal", right)
        
        if right in self.errors:
            return  right
        
        print("=============================")
        if right in ["Int","String","Bool"]:
            if left == right:
                return "Bool"
            else:
                return "notequal"
        else:
            if left == "Int" and right == "Bool":
                return "Bool"
            elif left == "Bool" and right == "Int":
                return "Bool"
            else:
                return "notequal"


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
            existNew = self.symbol_table.contains_class(value)
            print("visitNewObject existNew: ",existNew)
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
        value = ctx.ID().getText()
        print("\nid value: ", value)
        #revisar si es de tipo self
        if str(value) == "self":
            print("self.actual_method: ",self.actual_method)
            print("self.actual_method_type: ",self.actual_method_type)
            #agregar el self y asi segun lo que es en la tabla
            self.symbol_table.add_symbol(value, type=self.actual_method_type,ambit=self.actualAmbit)
            # print("self.actual_method: ",self.actual_method)
      
            return str(self.actual_method_type)
        else:
            exist = self.symbol_table.contains_symbol(value,self.actual_class) if self.symbol_table.contains_symbol(value,self.actual_class) else self.symbol_table.contains_symbol(value,self.actualAmbit)
    
        print("existe: ", exist)
        print("=============================")
        if exist:
            if self.symbol_table.get_symbol_value(value,self.actualAmbit,"type"):
                return self.symbol_table.get_symbol_value(value,self.actualAmbit,"type")
            
            elif self.symbol_table.get_symbol_value(value,self.actual_class,"type"):
                return self.symbol_table.get_symbol_value(value,self.actual_class,"type")
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
        
        print("visitIf results: ",results)
        print("=============================")
        #revisar que de los resultados obtenido no haya ninguno que forme parte de algun error
        for result in results:
            if result in self.errors:
                return result
            
        return results
        
    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        print("\nvisitOwnMethodCall")
        message = "methodError"
        expresions = ctx.expr()
        
        inherist = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
        print("visitOwnMethodCall inherist: ",inherist)
        
        id = ctx.ID().getText() 
        print("visitOwnMethodCall id: ",id)

        #tiene el io inheritado
        if str(inherist) == "IO":
            if id == "out_string":
                first = expresions.pop(0)
                firstType = self.visit(first)
    
                if firstType == "String":
                    # self.symbol_table.add_symbol(id,type="SELF_TYPE",recieves=firstType,ambit=self.actualAmbit)
                    message = "SELF_TYPE"
                
            elif id == "out_int":
                first = expresions.pop(0)
                firstType = self.visit(first)
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
            message = "String"
            
        elif id == "copy":
            message = "SELF_TYPE"
            
        elif id == "length":
            message = "Int"
            
        elif id == "concat":
            second = expresions.pop(0)
            secondType = self.visit(second)
            if secondType == "String":
                message = "String"
                
        elif id == "substr":
            second = expresions.pop(0)
            secondType = self.visit(second)
            
            third = expresions.pop(0)
            thirdType = self.visit(third)
            
            if secondType == "Int" and thirdType == "Int":
                message = "String"
                
        #revisar si el id es un metodo que se esta llamando que es del mismo metodo
        if self.symbol_table.contains_symbol(id,self.actual_class):
            print("visitOwnMethodCall si es un metodo de la misma clase")
            #revisar si este recibe parametros
            params = self.symbol_table.get_symbol_value(id,self.actual_class,"recieves")
            if params != None:
                newparams = []
                for p in params:
                    newparams.append(p[1])
                
                recievedParams = []
                for exp in expresions:
                    val = self.visit(exp)
                    recievedParams.append(val)
                #revisar ahora los parametros si son del mismo largo 
                print("visitOwnMethodCall params: ",params)
                print("visitOwnMethodCall newparams: ",newparams)
                print("visitOwnMethodCall recievedParams: ",recievedParams)
                if len(newparams) == len(recievedParams):
                    for i in range(len(newparams)):
                        if newparams[i] == recievedParams[i]:
                            message = self.symbol_table.get_symbol_value(id,self.actual_class,"type")
                        elif newparams[i] == "Bool" and recievedParams[i] == "Int":
                            message = self.symbol_table.get_symbol_value(id,self.actual_class,"type")
                        elif newparams[i] == "Int" and recievedParams[i] == "Bool":
                            message = self.symbol_table.get_symbol_value(id,self.actual_class,"type")
                        else:
                            message = "methodValuesNotSame"
                            break
                else:
                    message = "NotSameLenght"
            else:
                message = self.symbol_table.get_symbol_value(id,self.actual_class,"type")
        else:
            #revisar si es de un inhertis desde el cual se esta llamando
            #primero obtener si existe un inhertis de la clase
            inhertisExist = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
            while inhertisExist:
                if self.symbol_table.contains_symbol(id, inhertisExist):
                    #revisar si recibe parametros este
                    params = self.symbol_table.get_symbol_value(id,inhertisExist,"recieves")
                    if params != None:
                        newparams = []
                        for p in params:
                            newparams.append(p[1])
                        #revisar ahora los parametros si son del mismo largo 
                        recievedParams = []
                        for exp in expresions:
                            val = self.visit(exp)
                            recievedParams.append(val)
                        print("visitOwnMethodCall params: ",params)
                        print("visitOwnMethodCall newparams: ",newparams)
                        print("visitOwnMethodCall recievedParams: ",recievedParams)
                        #comparar ahora los parametros que tengan el mismo largo y si sean del mismo tipo
                        if len(newparams) == len(recievedParams):
                            for i in range(len(newparams)):
                                if newparams[i] == recievedParams[i]:
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                elif newparams[i] == "Bool" and recievedParams[i] == "Int":
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                elif newparams[i] == "Int" and recievedParams[i] == "Bool":
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                else:
                                    message = "methodValuesNotSame"
                                    break
                        else:
                            message = "NotSameLenght"
                        
                    else:
                        message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                    inhertisExist = False
                else:
                    inhertisExist = self.symbol_table.get_symbol_value(inhertisExist,inhertisExist,"inherits")
        
        if str(message) == "SELF_TYPE":
            message = self.actual_method_type
                
        print("visitOwnMethodCall message: ",message)
        
        return message


    # Visit a parse tree produced by YAPLParser#INTEGER.
    def visitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        return "Int"


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        print("\nassign visitado")
        expresion = self.visit(ctx.expr())
        # expresionType = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        left = ctx.ID().getText()
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.get_symbol_type(left) else "noValue"
        print("expresion: ",expresion)
        
        # expresion = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        # print("expresion later: ",expresion)
        print("left: ",left)
        left = self.symbol_table.get_symbol_value(left,self.actualAmbit,"type") if self.symbol_table.get_symbol_value(left,self.actualAmbit,"type") else left
        print("left after search: ",left)
        
        if expresion in self.errors:
            return expresion
        if left in self.errors:
            return left

        #si no esta significa que es una clase
        if expresion not in ["Int","String","Bool","Void","Object"]:
            #primero buscar si es una clase que si existe en la tabla
            if self.symbol_table.contains_class(expresion):
                pass
                # self.symbol_table.change_symbol_value(left,self.actualAmbit,"inherits",expresion)
        
        print("=============================")
        print("left: ",left)
        print("expresion: ",expresion)
        if str(left) == str(expresion):
            print("Se esta regresando este: ",left)
    
            return left
        elif str(left) == "Bool" and str(expresion) == "Int":
            return left
        elif str(left) == "Int" and str(expresion) == "Bool":
            return left
        else:
            #revisar si es una variable que se definio afuera del metodo que esta
            left = self.symbol_table.get_symbol_value(left,self.actual_class,"type") if self.symbol_table.get_symbol_value(left,self.actual_class,"type") else left
            print("left after search of newest: ",left)
            if str(left) == str(expresion):
                print("Se esta regresando este: ",left)
                return left
            elif str(left) == "Bool" and str(expresion) == "Int":
                return left
            elif str(left) == "Int" and str(expresion) == "Bool":
                return left
            return "assignEr"


    # Visit a parse tree produced by YAPLParser#methodCall.
    def visitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        expresions = ctx.expr()
        
        inherits = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
        print("visitMethodCall inherits: ",inherits)
        
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
            message = "String"
        elif id == "copy":
            message = "SELF_TYPE"
        elif id == "length":
            message = "Int"
        elif id == "concat":
            second = expresions.pop(0)
            secondType = self.visit(second)
            if secondType == "String":
                message = "String"
        elif id == "substr":
            second = expresions.pop(0)
            secondType = self.visit(second)
            third = expresions.pop(0)
            thirdType = self.visit(third)
            if secondType == "Int" and thirdType == "Int":
                message = "String"
        elif id == "isNil":
            message = "Bool"
        
        if str(inherits) == "IO":
            if id == "out_string":
                first = expresions.pop(0)
                firstType = self.visit(first)
                
                if firstType == "String":
                    message = "SELF_TYPE"
            elif id == "out_int":
                first = expresions.pop(0)
                firstType = self.visit(first)
                
                if firstType == "Int":
                    message = "SELF_TYPE"
            elif id == "in_string":
                message = "String"
            elif id == "in_int":
                message = "Int"
    
        #revisar si el id es un metodo que se esta llamando que es del mismo metodo
        if self.symbol_table.contains_symbol(id,firstType):
            print("visitmethodcall este metodo existe")
            #revisar si este recibe parametros
            params = self.symbol_table.get_symbol_value(id,firstType,"recieves")
            newparams = []
            if params != None:
                for p in params:
                    newparams.append(p[1])
                recievedParams = []
                for exp in expresions:
                    val = self.visit(exp)
                    recievedParams.append(val)
                print("visitmethodcall params: ",params)
                print("visitmethodcall newparams: ",newparams)
                print("visitmethodcall recievedParams: ",recievedParams)   
                #revisar ahora los parametros si son del mismo largo 
                if len(newparams) == len(recievedParams):
                    for i in range(len(newparams)):
                        if newparams[i] == recievedParams[i]:
                            message = self.symbol_table.get_symbol_value(id,firstType,"type")
                        elif newparams[i] == "Bool" and recievedParams[i] == "Int":
                            message = self.symbol_table.get_symbol_value(id,firstType,"type")
                        elif newparams[i] == "Int" and recievedParams[i] == "Bool":
                            message = self.symbol_table.get_symbol_value(id,firstType,"type")
                        else:
                            message = "methodValuesNotSame"
                            break
                else:
                    message = "NotSameLenght"
            else:
                message = self.symbol_table.get_symbol_value(id,firstType,"type")
        else:
            print("no es de la clase revisar si hereda y si es asi encontrar si es una de las funciones por la cual se hereda")
            #revisar si es de un inhertis desde el cual se esta llamando
            #primero obtener si existe un inhertis de la clase
            inhertisExist = self.symbol_table.get_symbol_value(firstType,firstType,"inherits")
            print("visitmethodcall inhertisExist: ",inhertisExist)
            print("========================")
            while inhertisExist:
                print("visitmethodcall id: ",id)
                print("visitmethodcall inhertisExist: ",inhertisExist)
                if self.symbol_table.contains_symbol(id, inhertisExist):
                    #revisar si recibe parametros este
                    params = self.symbol_table.get_symbol_value(id,inhertisExist,"recieves")
                    newparams = []
                    if params != None:
                        #revisar ahora los parametros si son del mismo largo 
                        for p in params:
                            newparams.append(p[1])
                        recievedParams = []
                        for exp in expresions:
                            val = self.visit(exp)
                            recievedParams.append(val)
                        print("visitmethodcall params: ",params)
                        print("visitmethodcall newparams: ",newparams)
                        print("visitmethodcall recievedParams: ",recievedParams)  
                        #comparar ahora los parametros que tengan el mismo largo y si sean del mismo tipo
                        if len(newparams) == len(recievedParams):
                            for i in range(len(newparams)):
                                if newparams[i] == recievedParams[i]:
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                elif newparams[i] == "Bool" and recievedParams[i] == "Int":
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                elif newparams[i] == "Int" and recievedParams[i] == "Bool":
                                    message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                                else:
                                    message = "methodValuesNotSame"
                                    break
                        else:
                            message = "NotSameLenght"
                        
                    else:
                        message = self.symbol_table.get_symbol_value(id,inhertisExist,"type")
                    inhertisExist = False
                else:
                    inhertisExist = self.symbol_table.get_symbol_value(inhertisExist,inhertisExist,"inherits")
                    print("visitmethodcall new inhertisExist: ",inhertisExist)
             
                    
        print("visitMethodCall message original: ",message)
        if message == "SELF_TYPE":
            message = firstType
        
        print("visitMethodCall message if SELF_TYPE: ",message)
        return message


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
        
        #logica para agregar el peso 
        
        # if str(letinType) == "Int":
        #     width=4
        # elif  str(letinType) == "String":
        #     width=2
        # elif str(letinType) == "Bool":
        #     width=2
        # else: 
        #     print("No existe este tipo por lo tanto toca buscar en la tabla")
        #     symbolExist = self.symbol_table.contains_symbol(letinType)
        #     if symbolExist:
        #         symbolType = self.symbol_table.get_symbol_type(letinType)
        #         if symbolType != False:
        #             if str(symbolType) == "class":
        #                 width=4
        #         else:
        #             return "assignError"
        #     else:
        #         return "assignError"
        
        #agregarlo a la tabla el nuevo valor del id
        self.symbol_table.add_symbol(id,type=letinType,ambit=self.actualAmbit)
        
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
        
        #agregar el id de este a la tabla
        self.symbol_table.add_symbol(id,type=typevisit,ambit=self.actualAmbit)
        
        #realizar la asignacion
        expresions = ctx.expr()
        assignExpresion = expresions[0]
        
        assignValue = self.visit(assignExpresion)
        print("visitLetAssignIn assignValue: ",assignValue)
        resutls = []
        if type(assignValue) ==  list:
            if typevisit in assignValue:
                resutls.extend(assignValue)
                resutls.append(typevisit)
            else:
                resutls.append("assignEr")
        else:
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
            resutls.append(exprValue)
        
        print("visitLetAssignIn results: ",resutls)
        return resutls



del YAPLParser