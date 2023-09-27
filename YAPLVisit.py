# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from build.YAPLParser import YAPLParser
else:
    from build.YAPLParser import YAPLParser
from MipsThreeCode import ThreeAddressCode
from SymbolTable import SymbolTable
from copy import *
import re

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisit(ParseTreeVisitor):

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.startType = None
        self.bytesSize_string = 0
        self.temp_size_class = 0
        self.actual_method = None
        self.actual_class = None
        self.actual_method_type = None
        self.actualAmbit = None
        # Codigo de tres direcciones
        self.tac = ThreeAddressCode()
        self.errors = ["ArithError","BothNotBool","RepeatedValue","assignError","methodValuesNotSame","NotSameLenght","TypeNotExist","notContainsType","diferentMethodType","diferentRecievers","recursiveInherit","whileError","DobleMain","newError","invertNotInt","inheritProblem","noMain","boolAr","intchar","charAr","assignEr","notequal","noValue","ifError","notLessorequal","notLess","methodError","noMethodAssign"]
        
    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        print("start visitado")
        
        message = []
        results = []
        tipos = ctx.classDefine()
        for tipo in tipos:
            # realizar limpieza de los s0,s1 y temporales 
            self.tac.clearClassElements()
            self.tac.clearTemporals
            val = self.visit(tipo)
            #add the label of end of the label
            self.tac.add(l=str(self.tac.returnSpecificLabelInCopy(self.actual_class,self.actual_class)) +"_EndTask")
            #delete the actual class of the copy of self.tac
            self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy(self.actual_class,self.actual_class))
            #clear all the labelscopy 
            self.tac.clearLabels()
            
            print("self.tac.classElements: ", self.tac.classElements)
            print("self.tac.temporals: ", self.tac.temporals)
            print("self.tac.labels: ",self.tac.labels)
            print("self.tac.labelsCopy: ",self.tac.labelsCopy)
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
        #para hacer print el tac
        self.tac.printTac()
        self.tac.printTacLabel()
        return message


    # Visit a parse tree produced by YAPLParser#defClase.
    def visitDefClase(self, ctx:YAPLParser.DefClaseContext):
        print("\nDefClase visitado")
        defclaseClass = ctx.CLASS()
        print("defclaseClass: ",defclaseClass)
        self.class_size = 0
        
        #definir la clase actual en la que esta
        
        defclaseTypeList = ctx.TYPE()
        classtype = defclaseTypeList[0].getText()
        # print(classtype)
        print("classtype type: ", classtype)
        self.actual_class = classtype
        #guardar el tipo de ambiente en el que esta
        self.actualAmbit = classtype
        
        #agregar el label del metodo en tac
        self.tac.addLables(classtype,self.actualAmbit)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy(classtype,self.actualAmbit))
        
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
            self.tac.clearTemporals()
            #delete the actual feature of the copy of self.tac
            if self.tac.returnSpecificLabelInCopy(self.actual_method,self.actualAmbit) != None:
                print(self.actualAmbit)
                self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy(self.actual_method,self.actualAmbit))
            
            print("visitDefClase val ver: ", val)
            
            #Acá detectamos los tipos de las variables que esto contiene
            if val == "Int":
                self.class_size += 4
            elif val == "String":
                print("Soy el otro valor cuando se detectan los tipos")
                self.class_size += 2
            elif val == "Bool":
                self.class_size += 2
            elif val == "Object":
                self.class_size += 2
            elif val == "SELF_TYPE":
                self.class_size += 2
            elif val == classtype: 
                print("SOY EL CLASSTYPE EN ESTAS  INSTANCIAS: ", classtype)
                print("TAMAÑO DE LA CLASE EN ESTOS MOMENTOS: ", self.class_size)
                self.class_size += self.class_size
            self.temp_size_class = self.class_size
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        
        #Actualizamos el valor del peso de la clase
        self.symbol_table.change_symbol_value(classtype,self.actual_class,"width",self.class_size)
        
        print("DefClase results: ", results)
        
        for result in results:
            if result in self.errors:
                return result
        return results

    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        print("\nvisitMethod")
        
        self.size_method = 0
        self.method_recieves_size = 0
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
                self.size_method += 4
            elif method_type == "String":
                print("Valor del ")
                self.size_method += 2
            elif method_type == "Bool":
                self.size_method += 2
            elif method_type == self.actual_class: 
                print("visitMethod ActualClass viendo: ", self.actual_class)

        #agregar el metodo
        self.symbol_table.add_symbol(method_name, method_type,ambit=self.actual_class)
        
        #actualizar el ambito que seria la clase mas el nombre del metodo
        self.actualAmbit = self.actual_class + "." + method_name
        
        #revisar si el metodo recibe parametros
        formlExist = ctx.formal()
        
        #agregar el label del metodo en tac
        self.tac.addLables(method_name,self.actual_class)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy(method_name,self.actual_class))

        print('method_name: ', method_name, '\n')
        print('method_type: ', method_type, '\n')
        
        # en este se guardara los parametros que recibe el metodo
        self.methodRecieves = []
        for form in formlExist:
            res= self.visit(form)
            print("VisitMethod recieves result: ", res)
            if res in self.errors:
                print("visitMethod found error: ",res)
                return res
        print("visitMethod self.methodRecieves: ",self.methodRecieves)
        if len(self.methodRecieves) > 0:
            print("el len de self.methodrecieves si es mas de 1")
            #agregar el recieves los parametros que tendria ese metodo junto con el nuevo peso calculado
            self.symbol_table.change_symbol_value(method_name,self.actual_class,"recieves",self.methodRecieves)
        
        
        # visitar el expr de la funcion
        method_expr_type, _ = self.visit(ctx.expr())
        
        print("VisitMethod tamaño de cadena actual: ", self.bytesSize_string)
        
        self.size_method = self.bytesSize_string + 2
        
        #Actualizamos el peso del método en la tabla
        self.symbol_table.change_symbol_value(method_name,self.actual_class,"width",self.size_method)
        
        # method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
        print("method expr type: ", method_expr_type)
        print("self.actualAmbit: ",self.actualAmbit)
        print("=============================")
        
        #agregar el fin del metodo del metodo en tac
        
        self.tac.add(l=str(self.tac.returnSpecificLabelInCopy(method_name,self.actual_class)) + "_EndTask")
        
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
        self.size_val = 0
        
        self.actual_method = var_name
        self.actual_method_type = var_type
        
        self.symbol_table.add_symbol(var_name, type=var_type, ambit=self.actual_class)
        #cambiar el tipo de ambiente para que ya sea del clase mas metodo
        self.actualAmbit = self.actual_class + "." + var_name
        
        var_expr, var_expr_value = self.visit(ctx.expr()) if ctx.expr() != None else ([], None)
        var_assign = ctx.ASSIGN()
        print("var_expr: ",var_expr)
        print('var_name: ', var_name)
        print('var_type: ', var_type)
        print('var_assign: ', var_assign, '\n')
        
        #definir que este sera un tipo S0 donde luego se revisara si este ya esta definido
        self.tac.addClassElements(var_name, "S")
        
        #agregar el label del metodo en tac
        self.tac.addLables(var_name,self.actual_class)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy(var_name,self.actual_class))
        
        #agregar al tac, la asignacion de elemtno al classelement
        self.tac.add("create",var_name,self.tac.returnSpecificRegistro(var_name))

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
            self.size_val = 4
        elif var_type == "String":
            self.size_val = self.bytesSize_string
        elif var_type == "Bool":
            self.size_val = 2
        else:
            self.size_val = 2
            
        #Actualizamos el peso de la tabla
        self.symbol_table.change_symbol_value(var_name,self.actual_class,"width",self.size_val)
        
        # revisar si es del mismo tipo la asignacion cuando se realice
        if var_assign != None:
            #buscar el registro de la variable
            registro = self.tac.returnSpecificRegistro(var_name)
            #agregar la agregacion 
            # self.tac.add("declare",registro,var_name)
            self.tac.add("<-",registro,var_expr_value)
            
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
        # else:
        #     registro = self.tac.returnSpecificRegistro(var_name)
            # self.tac.add("declare",registro,var_name)
            
        #agregar el fin del metodo del metodo en tac
        self.tac.add(l=str(self.tac.returnSpecificLabelInCopy(var_name,self.actual_class)) +"_EndTask")

        print("visitProperty var_type: ",var_type)
        print("=============================")
        return var_type

    # Visit a parse tree produced by YAPLParser#forml.
    def visitForml(self, ctx:YAPLParser.FormlContext):
        print("\nvisitForml")
        idtext = ctx.ID().getText()
        tipo = ctx.TYPE().getText()
        self.forml_size = 0
        print("idtext: ",idtext)
        print("tipo: ",tipo)
        if tipo not in ["Int","String","Bool","Object"]:
            print("buscar si el tipo existe")
            tipoExiste = self.symbol_table.contains_class(tipo)
            print("tipoExiste: ",tipoExiste)
            if tipoExiste:
                pass
            else:
                print("visitForml found: TypeNotExist")
                return "TypeNotExist"
        
        #asignar el width setun su tipo
        if tipo == "Int":
            self.forml_size = 4
        elif tipo == "String":
            self.forml_size = 2
        elif tipo == "Bool":
            self.forml_size = 2
        else:
            self.forml_size = 2
            
        #add the value of receving parameter in the self.tac
        
        recivingElements = []
        for ce in self.tac.classElements:
            recivingElements.append(str(ce[0]))
        if str(idtext) not in recivingElements:
            self.tac.addClassElements(idtext,"a")
        
        #actualizar el peso de la tabla
        self.symbol_table.add_symbol(idtext,tipo, width= self.forml_size,ambit=self.actualAmbit)
                      
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
        
        left, left_value = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print('left add: ',left)
        print('left_value add: ',left_value)
        
        right, right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print('right add:', right)
        print('right_value add:', right_value)
        
        #revisar si el left_value o el right_value es una temporal
        temporalExist = False
        if left_value.startswith("t"):
            temporalToAdd = left_value
            temporalExist = True
        if right_value.startswith("t"):
            temporalToAdd = right_value
            temporalExist = True
            
        #revisar en caso que ambos lados regresen una temporal
        if left_value.startswith("t") and right_value.startswith("t"):
            #realiazar una comparacion para ver cual de los dos es el menor ya que ese es el que se usara para guardar o asignar el temporal
            left_temporal = int(left_value[1:])
            right_temporal = int(right_value[1:])
            
            if left_temporal < right_temporal:
                temporalToAdd = left_value
            else:
                temporalToAdd = right_value
            
        #en caso que siga false crear una temporal para guardar la operacion en ella
        if temporalExist == False:
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("add",temporalToAdd,left_value,right_value)
        else:
            self.tac.add("add",temporalToAdd,left_value,right_value)

        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left,None
        if right in self.errors:
            return right,None
        
        if left == "Int" and right == "Int":
            return left,temporalToAdd
        elif left == "String" and right == "String":
            return left,temporalToAdd
        elif left == "Bool" and right == "Int":
            return left,temporalToAdd
        elif left == "Int" and right == "Bool":
            return left,temporalToAdd
        elif left == "Bool" and right == "Bool":
            return left,temporalToAdd
        # errors
        elif left == "Int" and right == "String":
            return "intchar",None
        elif left == "String" and right == "Int":
            return "intchar",None
        else:
            return "ArithError",None


    # Visit a parse tree produced by YAPLParser#sub.
    def visitSub(self, ctx:YAPLParser.SubContext):
        
        left, left_value = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right, right_value = self.visit(ctx.expr(1))

        print("\nvisitSub")
        print("left: ",left)
        print("left_value: ",left_value)
        print("right: ",right )
        print("right_value: ",right_value )
        
        #revisar si el left_value o el right_value es una temporal
        temporalExist = False
        if left_value.startswith("t"):
            temporalToAdd = left_value
            temporalExist = True
        if right_value.startswith("t"):
            temporalToAdd = right_value
            temporalExist = True
            
        #revisar en caso que ambos lados regresen una temporal
        if left_value.startswith("t") and right_value.startswith("t"):
            #realiazar una comparacion para ver cual de los dos es el menor ya que ese es el que se usara para guardar o asignar el temporal
            left_temporal = int(left_value[1:])
            right_temporal = int(right_value[1:])
            
            if left_temporal < right_temporal:
                temporalToAdd = left_value
            else:
                temporalToAdd = right_value
            
        #en caso que siga false crear una temporal para guardar la operacion en ella
        if temporalExist == False:
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("sub",temporalToAdd,left_value,right_value)
        else:
            self.tac.add("sub",temporalToAdd,left_value,right_value)
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left,None
        if right in self.errors:
            return right,None
        
        if left == "Int" and right == "Int":
            return left,temporalToAdd
        elif left == "Bool" and right == "Int":
            return left,temporalToAdd
        elif left == "Int" and right == "Bool":
            return left,temporalToAdd
        elif left == "Bool" and right == "Bool":
            return left,temporalToAdd
        # errors
        elif left == "String" and right == "String":
            return "charAr",None
        elif left == "Int" and right == "String":
            return "intchar",None
        elif left == "String" and right == "Int":
            return "intchar",None
        else:
            return "ArithError",None


    # Visit a parse tree produced by YAPLParser#void.
    def visitVoid(self, ctx:YAPLParser.VoidContext):
        print("\nvisitVoid")
        type,typeValue = self.visit(ctx.expr())
        print("visitVoid type: ",type)
        print("visitVoid typeValue: ",typeValue)
        print("=============================")
        #comprar si lo que se regreso es de tipo void
        if str(type) == "Void":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("isvoid",temporalToAdd,typeValue)
            return "bool",temporalToAdd
        else:
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("isvoid",temporalToAdd,typeValue)
            return "bool",temporalToAdd

    # Visit a parse tree produced by YAPLParser#invert.
    def visitInvert(self, ctx:YAPLParser.InvertContext):
        print("\nvisitInvert")
        
        value,valurFeature = self.visit(ctx.expr())
        
        # value = self.symbol_table.get_symbol_type(value) if self.symbol_table.get_symbol_type(value) else value
        print("visitInvert value: ",value)
        if str(value) == "Int":
            return "Int",valurFeature
        else:
            return "invertNotInt",None
        
        
    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        print("visitString")
        text = ctx.STRING().getText()
        text = text[1:-1]
        lenText = len(text)
        print("visitString text: ",text)
        self.bytesSize_string = lenText * 2
        print("VISIT STRING Peso de la cadena: ", self.bytesSize_string)
        return "String", text


    # Visit a parse tree produced by YAPLParser#mul.
    def visitMul(self, ctx:YAPLParser.MulContext):
        print("\nVisiting Mul node")
    
        left, left_value = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left mul: ", left)
        print("left_value mul: ", left_value)

        right, right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right mul: ",right)
        print("right_value mul: ",right_value)
        
        #revisar si el left_value o el right_value es una temporal
        temporalExist = False
        if left_value.startswith("t"):
            temporalToAdd = left_value
            temporalExist = True
        if right_value.startswith("t"):
            temporalToAdd = right_value
            temporalExist = True
            
        #revisar en caso que ambos lados regresen una temporal
        if left_value.startswith("t") and right_value.startswith("t"):
            #realiazar una comparacion para ver cual de los dos es el menor ya que ese es el que se usara para guardar o asignar el temporal
            left_temporal = int(left_value[1:])
            right_temporal = int(right_value[1:])
            
            if left_temporal < right_temporal:
                temporalToAdd = left_value
            else:
                temporalToAdd = right_value
        
        #en caso que siga false crear una temporal para guardar la operacion en ella
        if temporalExist == False:
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("mul",temporalToAdd,left_value,right_value)

        else:
            self.tac.add("mul",temporalToAdd,left_value,right_value)
            
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return left,None
        if right in self.errors:
            return right,None
        
        if left == "Int" and right == "Int":
            return left,temporalToAdd
        elif left == "Bool" and right == "Int":
            return right,temporalToAdd
        elif left == "Int" and right == "Bool":
            return left,temporalToAdd
        elif left == "Bool" and right == "Bool":
            return left,temporalToAdd
        # errors
        elif left == "String" and right == "String":
            return "charAr",None
        elif left == "Int" and right == "String":
            return "intchar",None
        elif left == "String" and right == "Int":
            return "intchar",None
        else:
            return "ArithError",None



    # Visit a parse tree produced by YAPLParser#factExpr.
    def visitFactExpr(self, ctx:YAPLParser.FactExprContext):
        expresion, expresion_value = self.visit(ctx.expr())
        print("\nFactExpr expresion: ",expresion)
        print("FactExpr expresion_value: ",expresion_value)
        print("=============================")
        return expresion, expresion_value



    # Visit a parse tree produced by YAPLParser#lteq.
    def visitLteq(self, ctx:YAPLParser.LteqContext):
        print("visitLteq")
        left,left_value = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left: ",left)
        
        right,right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right: ",right)
        
        #agregar la asigancion de la condicion segun el tipo del self.actual_conditional (if, while)
        self.actual_conditional = "lteq"
        # if self.actual_conditional == "if":
        #     tercetoResult = self.tac.add("ble",s="then",x=left_value,y=right_value)
        
        if left == "Int" and right == "Int":
            return "Bool",[left_value,right_value]
        if left == "Int" and right == "Bool":
            return "Bool",[left_value,right_value]
        if left == "Bool" and right == "Int":
            return "Bool",[left_value,right_value]
        if left == "Bool" and right == "Bool":
            return "Bool",[left_value,right_value]
        else:
            return "notLessorequal",None
        

    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        temporalToAdd = self.tac.newTemporal()
        self.tac.add("<-",temporalToAdd,0)
        return "Bool", temporalToAdd


    # Visit a parse tree produced by YAPLParser#lt.
    def visitLt(self, ctx:YAPLParser.LtContext):
        print("visitLt")
        
        left,left_value = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left: ",left)
        
        right,right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right: ",right)
        
        #agregar la asigancion de la condicion segun el tipo del self.actual_conditional (if, while)
        self.actual_conditional = "lt"
        # if self.actual_conditional == "if":
        #     tercetoResult = self.tac.add("blt",s="then",x=left_value,y=right_value)
        
        if left == "Int" and right == "Int":
            return "Bool",[left_value,right_value]
        if left == "Int" and right == "Bool":
            return "Bool",[left_value,right_value]
        if left == "Bool" and right == "Int":
            return "Bool",[left_value,right_value]
        if left == "Bool" and right == "Bool":
            return "Bool",[left_value,right_value]
        else:
            return "notLess",None

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
        
        left, left_value = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        print("left div: ",left )
        print("left_value div: ",left_value )
        
        right, right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        print("right div: ",right )
        print("right_value div: ",right_value )
        
        #revisar si el left_value o el right_value es una temporal
        temporalExist = False
        if left_value.startswith("t"):
            temporalToAdd = left_value
            temporalExist = True
        if right_value.startswith("t"):
            temporalToAdd = right_value
            temporalExist = True
            
        #revisar en caso que ambos lados regresen una temporal
        if left_value.startswith("t") and right_value.startswith("t"):
            #realiazar una comparacion para ver cual de los dos es el menor ya que ese es el que se usara para guardar o asignar el temporal
            left_temporal = int(left_value[1:])
            right_temporal = int(right_value[1:])
            
            if left_temporal < right_temporal:
                temporalToAdd = left_value
            else:
                temporalToAdd = right_value
        
        #en caso que siga false crear una temporal para guardar la operacion en ella
        if temporalExist == False:
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("div",temporalToAdd,left_value,right_value)
                    
        else:
            self.tac.add("div",temporalToAdd,left_value,right_value)
        
        #revisar que no sean parte del algun del los errors
        if left in self.errors:
            return right,None
        if left in self.errors:
            return right,None
        
        if left == "Int" and right == "Int":
            return left,temporalToAdd
        elif left == "Bool" and right == "Int":
            return left,temporalToAdd
        elif left == "Int" and right == "Bool":
            return left,temporalToAdd
        elif left == "Bool" and right == "Bool":
            return left,temporalToAdd
        # errors
        elif left == "String" and right == "String":
            return "charAr",None
        elif left == "Int" and right == "String":
            return "intchar",None
        elif left == "String" and right == "Int":
            return "intchar",None
        else:
            return "ArithError",None


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        print("\nvisitando equal")
        
        left, left_value = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
            
        print("left equal", left)
        print("left_value equal", left_value)
        
        if left in self.errors:
            return  left,None
        
        right, right_value = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.get_symbol_type(right) else right
        print("right equal", right)
        print("right_value equal", right_value)
        
        if right in self.errors:
            return  right,None
        
        #agregar la asigancion de la condicion segun el tipo del self.actual_conditional (if, while)
        self.actual_conditional = "equal"
        # if self.actual_conditional == "if":
        #     tercetoResult = self.tac.add("beq",s="then",x=left_value,y=right_value)
            
        
        print("=============================")
        if right in ["Int","String","Bool"]:
            if left == right:
                return "Bool",[left_value,right_value]
            else:
                return "notequal",None
        else:
            if left == "Int" and right == "Bool":
                return "Bool",[left_value,right_value]
            elif left == "Bool" and right == "Int":
                return "Bool",[left_value,right_value]
            else:
                return "notequal",None


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        print("\nvisitNot")
        values,valuesFeature = self.visit(ctx.expr())
        self.tac.add("not",valuesFeature,valuesFeature)
        
        # results = []
        # if type(values) == list:
        #     results.extend(values)
        # else:
        #     results.append(values)
        print("visitNot results: ",values)
        return values,valuesFeature


    # Visit a parse tree produced by YAPLParser#newObject.
    def visitNewObject(self, ctx:YAPLParser.NewObjectContext):
        print("\nvisitNewObject")
        # print(self.tac.labels)
        value = ctx.TYPE().getText()
        print(value)
        #revisar que si existe en new type
        if value not in ["Object"]:
            existNew = self.symbol_table.contains_class(value)
            print("visitNewObject existNew: ",existNew)
        else:
            existNew = True
        print("=============================")
        print("visitNewObject self.actualAmbit: ",self.actualAmbit)
        
        #obtener todos los que son del ambiente
        newObjectLists = self.symbol_table.get_ambit_symbols(self.actualAmbit)
        print("newObjectLists: ",newObjectLists)
        #filtrarlos para que solo esten los que comienzen con t
        newObjectLists = {k: v for k, v in newObjectLists.items() if re.match(r't\d+', k)}
        print("newObjectLists after filtering: ",newObjectLists)
        #guardar ya solo los nombres
        newObjectNames = list(newObjectLists.keys())
        print("newObjectNames: ",newObjectNames)
        # #comenzar a agregarle una temporal por cada uno
        # temporal_idx = 1
        # temporal = f"t{temporal_idx}"

        # while temporal in newObjectNames:
        #     temporal_idx += 1
        #     temporal = f"t{temporal_idx}"

        # self.symbol_table.add_symbol(temporal,value, width=self.temp_size_class,ambit=self.actualAmbit)
            
        # classLabel = self.tac.returnSpecificLabel(value,value)
        
        #agregar temporal de la asigacion de este
        temporalToAdd = self.tac.newTemporal()
        self.tac.add("<-",temporalToAdd,value)
        
        print("visitNewObject temporalToAdd: ",temporalToAdd)
        if existNew:
            return value,temporalToAdd
        else:
            return "newError",None


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        temporalToAdd = self.tac.newTemporal()
        self.tac.add("<-",temporalToAdd,1)
        return "Bool", temporalToAdd


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        expresions = ctx.expr()
        results = []
        for expresion in expresions:
            val,_ = self.visit(expresion)
            if type(val) == list:
                results.extend(val)
            else:
                results.append(val)
        
        print("\nvisitBlock result: ", results)
        print("=============================")
        for result in results:
            if result in self.errors:
                return result,None
            
        return results,None


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        print("\nvisitLet")
        result,_ = self.visit(ctx.let_expr())
        print("visitLet result: ",result)
        return result,None


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        value = ctx.ID().getText()
        print("\nid value: ", value)
        #revisar si es de tipo self
        if str(value) == "self":
            print("self.actual_method: ",self.actual_method)
            print("self.actual_method_type: ",self.actual_method_type)
            #agregar el self y asi segun lo que es en la tabla
            self.symbol_table.add_symbol(value, type=self.actual_method_type, width= self.size_method,ambit=self.actualAmbit)
            # print("self.actual_method: ",self.actual_method)
            
            #agregarlo como un valor de retorno tambien
            self.tac.addClassElements(str(self.actual_method_type), "S")
            self.tac.add("<-",self.tac.returnSpecificRegistro(str(self.actual_method_type)), str(self.actual_method_type))
            return str(self.actual_method_type),self.tac.returnSpecificRegistro(str(self.actual_method_type))
        else:
            exist = self.symbol_table.contains_symbol(value,self.actual_class) if self.symbol_table.contains_symbol(value,self.actual_class) else self.symbol_table.contains_symbol(value,self.actualAmbit)
    
        print("existe: ", exist)
        print("=============================")
        if exist:
            if self.symbol_table.get_symbol_value(value,self.actualAmbit,"type"):
                return self.symbol_table.get_symbol_value(value,self.actualAmbit,"type"), self.tac.returnSpecificRegistro(value)
            
            elif self.symbol_table.get_symbol_value(value,self.actual_class,"type"):
                return self.symbol_table.get_symbol_value(value,self.actual_class,"type"), self.tac.returnSpecificRegistro(value)
        else:
            return "noValue", None


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        print("\nif visitado")
        self.actual_conditional = None
        print("self.tac.classElements: ", self.tac.classElements)
        print("self.tac.temporals: ", self.tac.temporals)
        print("self.tac.labels: ",self.tac.labels)
        print("self.tac.labelsCopy: ",self.tac.labelsCopy)
        expresions = ctx.expr()
        
        #if there are not three expresion return error
        if len(expresions) != 3:
            return "ifError"
        
        #agregar el if en la labels del tac
        self.tac.addLables("if",self.actualAmbit)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy("if",self.actualAmbit))
        
        #logica del if
        ifstate = expresions[0] #if
        print("corriendo el if")
        # self.actual_conditional = "if"
        ifResult,conditioners = self.visit(ifstate)
        
        if self.actual_conditional == "equal":
            tercetoResult = self.tac.add("beq",s="then",x=conditioners[0],y=conditioners[1])
        elif self.actual_conditional == "lteq":
            tercetoResult = self.tac.add("ble",s="then",x=conditioners[0],y=conditioners[1])
        elif self.actual_conditional == "lt":
            tercetoResult = self.tac.add("blt",s="then",x=conditioners[0],y=conditioners[1])
        else:
            tercetoResult = self.tac.add("beq",s="then",x=conditioners,y="1")
            
        
        print("ifResult: ",ifResult)
        
        if type(ifResult) == list:
            if "Bool" not in ifResult:
                return "ifError",None
        else:
            if ifResult != "Bool":
                return "ifError",None
            
        #obtener los resultados de elstate y thenstate
        elsestate = expresions[2] #else
        #agregar el else en la labels del tac
        self.tac.addLables("else",self.actualAmbit)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy("else",self.actualAmbit))
        
        print("Corriendo el else")
        #limpieza de los temporales
        # self.tac.clearTemporals()
        elseResult,_ = self.visit(elsestate)
        print("elseResult: ",elseResult)
        #agregar el salto hacia el fi para que finalize el if
        tercetoFi = self.tac.add("j","fi")
        
        thenstate = expresions[1] #then
        print("Corriendo el then")
        #agregar el then en la labels del tac
        self.tac.addLables("then",self.actualAmbit)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy("then",self.actualAmbit))
        
        #limpieza de los temporales
        # self.tac.clearTemporals()
        thenResult,_ = self.visit(thenstate)
        print("thenResult: ",thenResult)
        
        #agregar logica para que haga salto para el fi
        self.tac.addLables("fi",self.actualAmbit)
        self.tac.add(l=self.tac.returnSpecificLabelInCopy("fi",self.actualAmbit))
        
        #reemplazando los valores de estos por su respectivo label
        tercetoResult.s = self.tac.returnSpecificLabelInCopy("then",self.actualAmbit)
        tercetoFi.s = self.tac.returnSpecificLabelInCopy("fi",self.actualAmbit)
        #eliminarlo de la tabla de labelsCopy
        self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy("if",self.actualAmbit))
        self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy("else",self.actualAmbit))
        self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy("then",self.actualAmbit))
        self.tac.deleteSpecifiLabel(self.tac.returnSpecificLabelInCopy("fi",self.actualAmbit))
        
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
            
        return results,None
        
    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        print("\nvisitOwnMethodCall")
        message = "methodError"
        val_value = None
        temporalToAdd = None
        recievedParamsValues = None
        expresions = ctx.expr()
        
        inherist = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
        print("visitOwnMethodCall inherist: ",inherist)
        
        id = ctx.ID().getText() 
        print("visitOwnMethodCall id: ",id)

        #tiene el io inheritado
        if str(inherist) == "IO":
            if id == "out_string":
                first = expresions.pop(0)
                firstType,firstTypeValue = self.visit(first)
    
                if firstType == "String":
                    # self.symbol_table.add_symbol(id,type="SELF_TYPE",recieves=firstType,ambit=self.actualAmbit)
                    temporalToAdd = self.tac.newTemporal()
                    self.tac.add("call",temporalToAdd,"OUT_STRING",firstTypeValue)
                    message = "SELF_TYPE"
                
            elif id == "out_int":
                first = expresions.pop(0)
                firstType,firstTypeValue = self.visit(first)
                print("visitOwnMethodCall out_int")
                print("visitOwnMethodCall firstType: ",firstType)
                print("visitOwnMethodCall firstTypeValue: ",firstTypeValue)
                #obtener la temporal que se utilzara para guardar el valor de este
                if firstType == "Int":
                    temporalToAdd = self.tac.newTemporal()
                    self.tac.add("call",temporalToAdd,"OUT_INT",firstTypeValue)
                    message = "SELF_TYPE"
                    
            elif id == "in_string":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,"IN_STRING")
                message = "String"
            elif id == "in_int":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,"IN_INT")
                message = "Int"
                    
        #cumple con alguno de los string o object
        if id == "abort":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,"ABORT")
            message = "Object"
            
        elif id == "type_name":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,"TYPE_NAME")
            message = "String"
            
        elif id == "copy":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,"COPY")
            message = "SELF_TYPE"
            
        elif id == "length":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,"LENGTH")
            message = "Int"
            
        elif id == "concat":
            second = expresions.pop(0)
            secondType,secondTypeValue = self.visit(second)
            if secondType == "String":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,"CONCAT",secondTypeValue)
                message = "String"
                
        elif id == "substr":
            second = expresions.pop(0)
            secondType,secondTypeValue = self.visit(second)
            
            third = expresions.pop(0)
            thirdType,thirdTypeValue = self.visit(third)
            
            if secondType == "Int" and thirdType == "Int":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,"SUBSTR",[str(secondTypeValue),str(thirdTypeValue)])
                message = "String"
        elif id == "isNil":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,"ISNILL")
            message = "Bool"
                
        #revisar si el id es un metodo que se esta llamando que es del mismo metodo
        if self.symbol_table.contains_symbol(id,self.actual_class):
   
            print("visitOwnMethodCall si es un metodo de la clase actual")
            #revisar si este recibe parametros
            params = self.symbol_table.get_symbol_value(id,self.actual_class,"recieves")
            
            if params != None:
                newparams = []
                newparamsValue = []
                for p in params:
                    newparams.append(p[1])
                    newparamsValue.append(p[0])
                
                recievedParams = []
                recievedParamsValues = []
                for exp in expresions:
                    val,val_value = self.visit(exp)
                    recievedParams.append(val)
                    recievedParamsValues.append(val_value)
                #revisar ahora los parametros si son del mismo largo 
                print("visitOwnMethodCall params: ",params)
                print("visitOwnMethodCall newparams: ",newparams)
                print("visitOwnMethodCall newparamsValue: ",newparamsValue)
                print("visitOwnMethodCall recievedParams: ",recievedParams)
                print("visitOwnMethodCall recievedParamsValues: ",recievedParamsValues)
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
                #si todo esta bien realizar la asignacion del valor de recievedParamsValues al newparamsValue
                # for index in range(len(newparamsValue)):
                #     location = self.tac.returnSpecificRegistro(newparamsValue[index])
                #     self.tac.add("<-",location,recievedParamsValues[index])
                
            else:
                message = self.symbol_table.get_symbol_value(id,self.actual_class,"type")
                
            #agregar al self.tac para que realice un goto al mismo metodo
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,self.tac.returnSpecificLabelInCopy(id,self.actual_class),recievedParamsValues)

                
        else:
            print("visitOwnMethodCall no de la clase ver si este se esta heredando de otro")
            #revisar si es de un inhertis desde el cual se esta llamando
            #primero obtener si existe un inhertis de la clase
            inhertisExist = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
            while inhertisExist:
                print("visitOwnMethodCall si existe su metodo en la herncia")
                if self.symbol_table.contains_symbol(id, inhertisExist):
                    #revisar si recibe parametros este
                    params = self.symbol_table.get_symbol_value(id,inhertisExist,"recieves")
                    if params != None:
                        newparams = []
                        newparamsValue = []
                        for p in params:
                            newparams.append(p[1])
                            newparamsValue.append(p[0])
                        #revisar ahora los parametros si son del mismo largo 
                        recievedParams = []
                        recievedParamsValues = []
                        for exp in expresions:
                            val, val_value = self.visit(exp)
                            recievedParams.append(val)
                            recievedParamsValues.append(val_value)
                        print("visitOwnMethodCall inhertisExist: ",inhertisExist)
                        print("visitOwnMethodCall params: ",params)
                        print("visitOwnMethodCall newparams: ",newparams)
                        print("visitOwnMethodCall newparamsValue: ",newparamsValue)
                        print("visitOwnMethodCall recievedParams: ",recievedParams)
                        print("visitOwnMethodCall val_value: ",val_value)
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

                    #agregar la llamada del metodo
                    temporalToAdd = self.tac.newTemporal()
                    tacId = self.tac.returnSpecificLabel(str(id),str(inhertisExist))
                    print("visitOwnMethodCall tacId: ",tacId)
                    self.tac.add("call",temporalToAdd,id,recievedParamsValues)

                    inhertisExist = False

                else:
                    inhertisExist = self.symbol_table.get_symbol_value(inhertisExist,inhertisExist,"inherits")
        
        if str(message) == "SELF_TYPE":
            message = self.actual_method_type
                
        print("visitOwnMethodCall message: ",message)
        
        return message,temporalToAdd


    # Visit a parse tree produced by YAPLParser#INTEGER.
    def visitINTEGER(self, ctx:YAPLParser.INTEGERContext):
        print("visitINTEGER")
        value = ctx.INTEGER().getText()
        print("visitINTEGER value: ",value)
        return "Int", value


    # Visit a parse tree produced by YAPLParser#assign.
    def visitAssign(self, ctx:YAPLParser.AssignContext):
        print("\nassign visitado")
        expresion, expresion_value = self.visit(ctx.expr())
        # expresionType = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        left = ctx.ID().getText()
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.get_symbol_type(left) else "noValue"
        print("expresion: ",expresion)
        
        # expresion = self.symbol_table.get_symbol_type(expresion) if self.symbol_table.get_symbol_type(expresion) else expresion
        # print("expresion later: ",expresion)
        print("left: ",left)
        
        #agregar la asigancion en el threecode
        registro = self.tac.returnSpecificRegistro(left)
        self.tac.add("<-",registro,expresion_value)
        
        left = self.symbol_table.get_symbol_value(left,self.actualAmbit,"type") if self.symbol_table.get_symbol_value(left,self.actualAmbit,"type") else left
        print("left after search: ",left)
        
        if expresion in self.errors:
            return expresion,None
        if left in self.errors:
            return left,None

        #si no esta significa que es una clase
        # if expresion not in ["Int","String","Bool","Void","Object"]:
        #     #primero buscar si es una clase que si existe en la tabla
        #     if self.symbol_table.contains_class(expresion):
        #         pass
                # self.symbol_table.change_symbol_value(left,self.actualAmbit,"inherits",expresion)
        
        print("=============================")
        print("left: ",left)
        print("expresion: ",expresion)
        if str(left) == str(expresion):
            print("Se esta regresando este: ",left)
            return left,None
        elif str(left) == "Bool" and str(expresion) == "Int":
            return left,None
        elif str(left) == "Int" and str(expresion) == "Bool":
            return left,None
        else:
            #revisar si es una variable que se definio afuera del metodo que esta
            left = self.symbol_table.get_symbol_value(left,self.actual_class,"type") if self.symbol_table.get_symbol_value(left,self.actual_class,"type") else left
            print("left after search of newest: ",left)
            if str(left) == str(expresion):
                print("Se esta regresando este: ",left)
                return left,None
            elif str(left) == "Bool" and str(expresion) == "Int":
                return left,None
            elif str(left) == "Int" and str(expresion) == "Bool":
                return left,None
            return "assignEr",None


    # Visit a parse tree produced by YAPLParser#methodCall.
    def visitMethodCall(self, ctx:YAPLParser.MethodCallContext):
        expresions = ctx.expr()
        valValue = None
        recievedParamsValues = None
        temporalToAdd = None
        inherits = self.symbol_table.get_symbol_value(self.actual_class,self.actual_class,"inherits")
        print("visitMethodCall inherits: ",inherits)
        
        #obtener el primer tipo y segun ello trabajarlo
        first = expresions.pop(0)
        firstType,firstTypeValue = self.visit(first)
        
        print("\nvisitMethodCall")
        message = "methodError"
        # results=[] 
        
        id = ctx.ID().getText()
        print("visitMethodCall id: ",id)
        print("visitMethodCall firstType: ",firstType)
        print("visitMethodCall firstTypeValue: ",firstTypeValue)
        if firstType in self.errors:
            return firstType,None
        
        if id == "abort":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+"ABORT")
            message = "Object"
        elif id == "type_name":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+"TYPE_NAME")
            message = "String"
        elif id == "copy":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+"COPY")
            message = "SELF_TYPE"
        elif id == "length":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+"LENGTH")
            message = "Int"
        elif id == "concat":
            second = expresions.pop(0)
            secondType,secondTypeValue = self.visit(second)
            if secondType == "String":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,firstTypeValue+"."+"CONCAT",secondTypeValue)
                message = "String"
        elif id == "substr":
            second = expresions.pop(0)
            secondType,secondTypeValue = self.visit(second)
            third = expresions.pop(0)
            thirdType,thirdTypeValue = self.visit(third)
            if secondType == "Int" and thirdType == "Int":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,firstTypeValue+"."+"SUBSTR",[str(secondTypeValue),str(thirdTypeValue)])
                message = "String"
        elif id == "isNil":
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+"ISNILL")
            message = "Bool"
        
        if str(inherits) == "IO":
            if id == "out_string":
                second = expresions.pop(0)
                secondType,secondTypeValue = self.visit(second)
                if secondType == "String":
                    temporalToAdd = self.tac.newTemporal()
                    self.tac.add("call",temporalToAdd,firstTypeValue+"."+"OUT_STRING",secondTypeValue)
                    message = "SELF_TYPE"
                    
            elif id == "out_int":
                second = expresions.pop(0)
                secondType,secondTypeValue = self.visit(second)
                if secondType == "Int":
                    temporalToAdd = self.tac.newTemporal()
                    self.tac.add("call",temporalToAdd,firstTypeValue+"."+"OUT_INT",secondTypeValue)
                    message = "SELF_TYPE"
                    
            elif id == "in_string":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,firstTypeValue+"."+"IN_STRING")
                message = "String"
                
            elif id == "in_int":
                temporalToAdd = self.tac.newTemporal()
                self.tac.add("call",temporalToAdd,firstTypeValue+"."+"IN_INT")
                message = "Int"
        
        #revisar si el id es un metodo que se esta llamando que es del mismo metodo
        if self.symbol_table.contains_symbol(id,firstType):
            #obtner el label del metodo:
            methodCallLabel = self.tac.returnSpecificLabel(id,firstType)
            print("visitmethodcall methodCallLabel: ",methodCallLabel)
            
            print("visitmethodcall este metodo existe")
            #revisar si este recibe parametros
            params = self.symbol_table.get_symbol_value(id,firstType,"recieves")
            newparams = []
            newparamsValue = []
            if params != None:
                for p in params:
                    newparams.append(p[1])
                    newparamsValue.append(p[0])
                recievedParams = []
                recievedParamsValues = []
                for exp in expresions:
                    val,valValue = self.visit(exp)
                    recievedParams.append(val)
                    recievedParamsValues.append(valValue)
                print("visitmethodcall params: ",params)
                print("visitmethodcall newparams: ",newparams)
                print("visitmethodcall newparamsValue: ",newparamsValue)
                print("visitmethodcall recievedParams: ",recievedParams)   
                print("visitmethodcall recievedParamsValues: ",recievedParamsValues) 
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
                
            #agregar la llamada del metodo
            temporalToAdd = self.tac.newTemporal()
            self.tac.add("call",temporalToAdd,firstTypeValue+"."+id,recievedParamsValues)
            
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
                    #obtner el label del metodo:
                    methodCallLabel = self.tac.returnSpecificLabel(id,inhertisExist)
                    print("visitmethodcall methodCallLabel: ",methodCallLabel)
                    print("visitmethodcall si existe aqui")
                    #revisar si recibe parametros este
                    params = self.symbol_table.get_symbol_value(id,inhertisExist,"recieves")
                    newparams = []
                    newparamsValue = []
                    if params != None:
                        #revisar ahora los parametros si son del mismo largo 
                        for p in params:
                            newparams.append(p[1])
                            newparamsValue.append(p[0])
                        recievedParams = []
                        recievedParamsValues = []
                        for exp in expresions:
                            val,valValue = self.visit(exp)
                            recievedParams.append(val)
                            recievedParamsValues.append(valValue)
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
                    
                    #agregar la llamada del metodo
                    temporalToAdd = self.tac.newTemporal()
                    self.tac.add("call",temporalToAdd,firstTypeValue+"."+id,recievedParamsValues)

                else:
                    inhertisExist = self.symbol_table.get_symbol_value(inhertisExist,inhertisExist,"inherits")
                    print("visitmethodcall new inhertisExist: ",inhertisExist)
            
                    
        print("visitMethodCall message original: ",message)
        if message == "SELF_TYPE":
            message = firstType
        
        print("visitMethodCall message if SELF_TYPE: ",message)
        print("visitMethodCall temporalToAdd: ",temporalToAdd)
        return message,temporalToAdd


    # Visit a parse tree produced by YAPLParser#nestedLet.
    def visitNestedLet(self, ctx:YAPLParser.NestedLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        print("\nvisitLetIn")
        id = ctx.ID().getText()
        letinType = ctx.TYPE().getText()
        
        #agregar el variable con su registro perspectivo
        self.tac.addClassElements(id, "S")

        #agregar al tac, la asignacion de elemtno al classelement
        self.tac.add("create",id,self.tac.returnSpecificRegistro(id))

        self.let_size = 0
        print("visitLetIn valor de la cadena: ", self.bytesSize_string)
        
        #agregarlo a la tabla el nuevo valor del id
        self.symbol_table.add_symbol(id,type=letinType, ambit=self.actualAmbit)
        
        result,_ = self.visit(ctx.expr())
        
        #logica para agregar el peso 
        
        if str(letinType) == "Int":
            self.let_size=4
        elif  str(letinType) == "String":
            self.let_size = self.bytesSize_string
        elif str(letinType) == "Bool":
            self.let_size = 2
        else: 
            print("No existe este tipo por lo tanto toca buscar en la tabla")
            symbolExist = self.symbol_table.contains_symbol(letinType)
            if symbolExist:
                # symbolType = self.symbol_table.get_symbol_type(letinType)
                # if symbolType != False:
                #     if str(symbolType) == "class":
                #         pass
                # else:
                #     return "assignError"
                pass
            else:
                return "assignError",None
        
        print("visitLetIn id: ", id)
        print("visitLetIn self.actualAmbit:  ", self.actualAmbit)
        print("visitLetIn self.let_size ", self.let_size)
        #Actualizamos el peso en la tabla
        self.symbol_table.change_symbol_value(id,self.actualAmbit,"width",self.let_size)
        
        print("visitLetIn result: ",result)
        return result,None
        

    # Visit a parse tree produced by YAPLParser#letAssignLet.
    def visitLetAssignLet(self, ctx:YAPLParser.LetAssignLetContext):
        print("\nvisitLetAssignLet")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letAssignIn.
    def visitLetAssignIn(self, ctx:YAPLParser.LetAssignInContext):
        print("\nvisitLetAssignIn")
        id = ctx.ID().getText()
        typevisit = ctx.TYPE().getText()
        self.let_assign_size = 0
        print("visitLetAssignIn typevisit: ",typevisit)
        
        #agregar el variable con su registro perspectivo
        self.tac.addClassElements(id, "S")
        
        #agregar al tac, la asignacion de elemtno al classelement
        self.tac.add("create",id,self.tac.returnSpecificRegistro(id))
        
        #agregar el id de este a la tabla
        self.symbol_table.add_symbol(id,type=typevisit,ambit=self.actualAmbit)
        
        #realizar la asignacion
        expresions = ctx.expr()
        assignExpresion = expresions[0]
        
        assignType, assignValue = self.visit(assignExpresion)
        print("visitLetAssignIn assignValue: ",assignValue)
        
        #agregar la asigacion al self.tac.add
        registro = self.tac.returnSpecificRegistro(id)
        self.tac.add("<-",registro,assignValue)
        
        
        resutls = []
        if type(assignType) ==  list:
            if typevisit in assignType:
                resutls.extend(assignType)
                resutls.append(typevisit)
            else:
                resutls.append("assignEr")
        else:
            if assignType == typevisit:
                resutls.append(typevisit)
            else:
                resutls.append("assignEr")
                
                
        #Asignamos el peso según el tipo que se detecta
        if typevisit == "Int": 
            self.let_assign_size += 4
        elif typevisit == "String":
            self.let_assign_size += self.bytesSize_string
        elif typevisit == "Bool":
            self.let_assign_size += 2
        elif typevisit == "SELF_TYPE":
            self.let_assign_size += 2
        else:
            self.let_assign_size += 1
            
        #Actualizamos el peso en la tabla
        self.symbol_table.change_symbol_value(id,self.actualAmbit,"width",self.let_assign_size)
                            
        #obtener la otra expr
        exprResult = expresions[1]
        exprValue,_ = self.visit(exprResult)
        
        if type(exprValue) == list:
            resutls.extend(exprValue)
        else:
            resutls.append(exprValue)
        
        print("visitLetAssignIn results: ",resutls)
        return resutls,None



del YAPLParser