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
        self.actual_class = None
        self.actual_method = None
        self.actual_method_type = None
        self.startType = None
        self.actualAmbit = "Global"
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
        print(self.symbol_table)
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
        
        #agregar todos las variables
        variables = ctx.feature()
        variable_array = []
        checkVariable = []
        for variable in variables:
            print("variable :", variable.ID().getText())
            if variable.ID().getText():
                #revisar si ya esta este valor definido
                if variable.ID().getText() in checkVariable:
                    return "RepeatedValue"
                variable_array.append([variable.ID().getText(),variable.TYPE().getText(),classtype])
                checkVariable.append(variable.ID().getText())
        print("checkVariable: ",checkVariable)
        print("variable_array: ",variable_array)   
        # print("tail" in variable_array) 
        
        defclaseInherits = ctx.INHERITS() #revisar si existe la funcion inherits
        # print(defclaseInherits)
        if defclaseInherits:
            inheritPosition = defclaseTypeList[1]
            
            #revisar que no sea recursivo
            if inheritPosition == classtype:
                return "recursiveInherit"
            
            #revisar si Main ya existe
            existMain = self.symbol_table.contains_symbol("Main")
            existmain = self.symbol_table.contains_symbol("main")
            if not existMain and not existmain: 
                if len(variable_array) > 0: 
                    self.symbol_table.add_symbol(classtype, defclaseClass, inherits=inheritPosition, contains=variable_array, ambit="Global")
                else:
                    self.symbol_table.add_symbol(classtype, type=defclaseClass, inherits=inheritPosition, ambit="Global")
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
                            #revisar si cuando se esta sobreescribiendo el metodo si sigan siendo del mismo tipo
                            newtypeContains = [] 
                            for tc in typeContains:
                                newtypeContains.append(tc[0])
                            newtypeInheritContains = []
                            for tic in typeInheritContains:
                                newtypeInheritContains.append(tic[0])
                            print("newtypeContains: ",newtypeContains)
                            print("newtypeInheritContains: ",newtypeInheritContains)
                            
                            # for ntc in newtypeContains:
                            #     if ntc in newtypeInheritContains:
                            #         ntcIndex = newtypeContains.index(ntc)
                            #         nticIndex = newtypeInheritContains.index(ntc)
                            #         first = typeContains[ntcIndex]
                            #         second = typeInheritContains[nticIndex]
                                    
                            #         if first != second:
                            #             print("Son distintos")
                            #             return "diferentMethodType"
                            
                            array.extend(typeContains)

                            for ntic in newtypeInheritContains:
                                if ntic not in newtypeContains:
                                    index = newtypeInheritContains.index(ntic)
                                    array.append(typeInheritContains[index])
                            
                        result = []
                        seen = set()
                        print("visitDefClase array: ",array)
                        for sublist in array:
                            if tuple(sublist) not in seen:
                                result.append(sublist)
                                seen.add(tuple(sublist))
                        print("result: ",result)
                        self.symbol_table.add_symbol(classtype,type=defclaseClass,contains=result)
                        
                        
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
                self.symbol_table.add_symbol(classtype, type=defclaseClass,ambit="Global")
        
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
        
        size_method = 0
        
        self.actualAmbit = "Local"
        self.forml_type = False
        method_name = ctx.ID().getText()
        method_type = ctx.TYPE().getText()
        # inhertisMethodType = self.symbol_table.get_symbol_type(method_name)
        # print("visitMethod inhertisMethodType: ",inhertisMethodType)
        
        methodExist = self.symbol_table.contains_symbol(method_name)

        #revisar si el method_type existe si no es tipo Int, Char, Bool, Object, Void, SELF_TYPE
        if method_type not in ["Int","String","Bool","Object","Void","SELF_TYPE"]:
            #revisar si existe
            method_type_Exist = self.symbol_table.contains_symbol(method_type)
            print("method_type_Exist: ",method_type_Exist)
            if method_type_Exist:
                method_type_class = self.symbol_table.get_symbol_type(method_type)
                print("method_type_class: ",method_type_class)
                if method_type_class != False:
                    if str(method_type_class) == "class":
                        pass
                    else:
                        return "assignError"
            else:
                return "assignError"
        else:
            if method_type == "Int":
                size_method += 4


        # print("visitMethod methodExist: ",methodExist)
        if methodExist == False:
            # print("asignando un nuevo metodo ya que no existe")
            self.symbol_table.add_symbol(method_name, method_type,ambit="Local")
        
        formlExist = ctx.formal()
        # print("method_name type: ", type(method_name))
        # print("method_type type: ", type(method_type))
        # inhertisMethodType = self.symbol_table.get_symbol_type(method_name)
        # print("visitMethod inhertisMethodType: ",inhertisMethodType)
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
        print("self.methodRecieves: ",self.methodRecieves)
        if len(self.methodRecieves) > 0:
            #revisar si el metodo existe pero tiene que el recieves es falso o none
            methodRecieving = self.symbol_table.get_recieves(method_name)
            addRecieves = []
            if methodRecieving == False:
                addRecieves.append([self.actual_class,self.methodRecieves])
            else:
                addRecieves.extend(methodRecieving)
                if self.methodRecieves not in addRecieves:
                    addRecieves.append([self.actual_class,self.methodRecieves])
            print("addRecieves: ",addRecieves)
            self.symbol_table.add_symbol(method_name,method_type,recieves=addRecieves)
            methodHasRecieve = self.symbol_table.get_recieves(method_name)
            print("visitMethod methodHasRecieve: ",methodHasRecieve)
            # if methodHasRecieve == False:
            
            #revisar si el class es un inhertis
            classIsInhertis = self.symbol_table.get_inherits(self.actual_class)
            print("visitMethod classIsInhertis: ",classIsInhertis)
            if classIsInhertis: 
                classInheritContains = self.symbol_table.get_contains(classIsInhertis)
                print("visitMethod classInheritContains: ",classInheritContains)
                newclassInheritContains = []
                if classInheritContains != None:
                    for cic in classInheritContains:
                        newclassInheritContains.append(cic[0])
                print("newclassInheritContains: ",newclassInheritContains)
                if classInheritContains:
                    if method_name in newclassInheritContains:
                        #revisar que el forml sea del mismo tipo que el que tiene adentro y el tipo de valor de regreso
                        classInhertisMethodRecieves = self.symbol_table.get_recieves(method_name)
                        print("visitMethod classInhertisMethodRecieves: ",classInhertisMethodRecieves)
                        ClassclassInhertisMethodRecieves = []
                        for cimr in classInhertisMethodRecieves:
                            ClassclassInhertisMethodRecieves.append(cimr[0])
                        
                        indexClass = ClassclassInhertisMethodRecieves.index(str(classIsInhertis))
                        classInhertisMethodRecieves = [classInhertisMethodRecieves[indexClass][1]]
                        print("newest classInhertisMethodRecieves: ",classInhertisMethodRecieves)
                        print("visitMethod self.methodRecieves: ",self.methodRecieves)
                        
                        if self.methodRecieves not in classInhertisMethodRecieves:
                            return "diferentRecievers"
                        #revisar si regresan el mismo tipo de valor
                        
                        indexClass = newclassInheritContains.index(method_name)
                        inhertisMethodType = classInheritContains[indexClass][1]
                        
                        # inhertisMethodType = self.symbol_table.get_symbol_type(method_name)
                        print("visitMethod inhertisMethodType: ",inhertisMethodType)
                        if inhertisMethodType != method_type:
                            return "diferentMethodType"
                        
        
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
        print("self.actual_method_type: ",self.actual_method_type)
        print("=============================")
        # voidBasicType = ["Void","Int","Char","Bool"]
        #revisar si tiene un valor igual al tipo del metodo 
        if type(method_expr_type) == list:
            print("es un tipo de lista")
            if str(self.actual_method_type) in method_expr_type:
                return self.actual_method_type
            else:
                print("no fue igual")
                #revisar si el self.actual_method_type es tipo Bool o Int y si es asi revisar si en las respuestas ahi un Int O Bool
                if str(self.actual_method_type) == "Int":
                    if "Bool" in method_expr_type:
                        return self.actual_method_type
                    else:
                        return "notContainsType"
                elif str(self.actual_method_type) == "Bool":
                    if "Int" in method_expr_type:
                        return self.actual_method_type
                    else:
                        return "notContainsType"
                else:
                    return "notContainsType"
        else:
            if method_expr_type in self.errors:
                return method_expr_type
            
            if self.actual_method_type == method_expr_type:
                return self.actual_method_type
            else:
                methodContians = self.symbol_table.get_contains(self.actual_method)
                print("methodContians: ",methodContians)
                classContains = self.symbol_table.get_contains(self.actual_class)
                print("classContains: ",classContains)

                newClasscontains = []
                newMethodContains = []
                
                if classContains != None:
                    for cc in classContains:
                        newClasscontains.append(cc[0])
                if methodContians != None:
                    for mc in methodContians:
                        newMethodContains.append(mc[0])
                print("visitMethod newMethodContains: ",newMethodContains)
                print("visitMethod newClasscontains: ",newClasscontains)
                print("visitMethod method_expr_type: ",method_expr_type)
                if method_expr_type in newMethodContains:
                    methodIndex = newMethodContains.index(method_expr_type)
                    method_expr_type = methodContians[methodIndex][1]
                else:
                    if method_expr_type in newClasscontains:
                        methodIndex = newClasscontains.index(method_expr_type)
                        method_expr_type = classContains[methodIndex][1]
                        if method_expr_type == "Int":
                            size_method += 4
                    else:
                        method_expr_type = method_expr_type
                print("self.actual_method_type: ",self.actual_method_type)
                print("method_expr_type: ",method_expr_type)
                
                self.symbol_table.add_symbol(self.actual_method,width=size_method)
                # method_expr_type = self.symbol_table.get_symbol_type(method_expr_type) if self.symbol_table.get_symbol_type(method_expr_type) else method_expr_type
                if self.actual_method_type == method_expr_type:
                    return self.actual_method_type
                else:
                    return "notContainsType"
       
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
        #revisar que el var_expr no sea un tipo de error
        if var_expr in self.errors:
            return var_expr
        #revisar que la variable si no es int, char o bool sea algo que exista en la tabla
        if str(var_type) not in ["Int","String","Bool","Object","Void","SELF_TYPE"]:
            print("toca buscar")
            if self.symbol_table.contains_symbol(var_type) and str(self.symbol_table.get_symbol_type(var_type)) == "class":
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
            var_expr = self.symbol_table.get_symbol_type(var_expr) if self.symbol_table.get_symbol_type(var_expr) else var_expr
            if var_type not in var_expr:
                print("assignEr")
                return "assignEr"
            
        self.symbol_table.add_symbol(var_name, type=var_type, width=width, ambit="Local")    
        
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
        if tipo not in ["Int","String","Bool","Object"]:
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
                    
                    newformContains = []
                    for fc in formContains:
                        newformContains.append(fc[0])
                    newclassContains = []
                    for cc in classContains:
                        newclassContains.append(cc[0])
                        
                    for ncc in newclassContains:
                        if ncc not in newformContains:
                            index = newclassContains.index(ncc)
                            formArray.append(classContains[index])
                result = []
                seen = set()

                for sublist in formArray:
                    if tuple(sublist) not in seen:
                        result.append(sublist)
                        seen.add(tuple(sublist))
                
                print("visitForml result: ",result)
                self.symbol_table.add_symbol(idtext,tipo,contains=result)
            else:
                print("visitForml found: TypeNotExist")
                return "TypeNotExist"
        
        print("self.actual_method: ",self.actual_method)
        # print("self.actual_method Type: ",type(self.actual_method))
        print("self.actual_method_type: ",self.actual_method_type)
        
        #agregarlo en su contains
        contains = self.symbol_table.get_contains(self.actual_method)
        array = []
        if contains == None:
            array.append([idtext,tipo,self.actual_class])
        else:
            if [idtext,tipo,self.actual_class] not in array:
                array.append([idtext,tipo,self.actual_class])
            array.extend(contains)
            
        self.methodRecieves.append([idtext,tipo])
        
        result = []
        seen = set()
        for sublist in array:
            if tuple(sublist) not in seen:
                result.append(sublist)
                seen.add(tuple(sublist))
        
        print("visitForml array: ",result)
        print("visitForml self.methodRecieves: ",self.methodRecieves)
        self.symbol_table.add_symbol(self.actual_method,contains=result)
        print("=============================")
        
        
    
    # Visit a parse tree produced by YAPLParser#or.
    def visitOr(self, ctx:YAPLParser.OrContext):
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
        
        if left_type == "noValue":
            return left_type
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
            
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
            return "BothNotBool"
    
    # Visit a parse tree produced by YAPLParser#and.
    def visitAnd(self, ctx:YAPLParser.AndContext):
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
        
        if left_type == "noValue":
            return left_type
        
        if left_type == "noValue":
            return left_type
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
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
            return "BothNotBool"

    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        print("Visiting Add node")
        
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)
        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        # print('add')
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left

        print('left add: ',left)
        print('left add type: ',left_type)
        if left_type == "noValue":
            return left_type
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        print('right add:', right)
        print('right add type:', right_type)
        if right_type == "noValue":
            return right_type
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        elif left_type == "String" and right_type == "String":
            return left_type
        elif left_type == "Bool" and right_type == "Int":
            return right_type
        elif left_type == "Int" and right_type == "Bool":
            return left_type
        elif left_type == "Bool" and right_type == "Bool":
            return left_type
        # errors
        elif left_type == "Int" and right_type == "String":
            return "intchar"
        elif left_type == "String" and right_type == "Int":
            return "intchar"
        else:
            return "ArithError"


    # Visit a parse tree produced by YAPLParser#sub.
    def visitSub(self, ctx:YAPLParser.SubContext):
        
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)
        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
                
        if left_type == "noValue":
            return left_type
        
        right = self.visit(ctx.expr(1))
        
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right_type == "noValue":
            return right_type
        

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
        elif left_type == "Bool" and right_type == "Int":
            return right_type
        elif left_type == "Int" and right_type == "Bool":
            return left_type
        elif left_type == "Bool" and right_type == "Bool":
            return left_type
        # errors
        elif left_type == "String" and right_type == "String":
            return "charAr"
        elif left_type == "Int" and right_type == "String":
            return "intchar"
        elif left_type == "String" and right_type == "Int":
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
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        value = self.visit(ctx.expr())
        
        if value in newMethodContains:
            methodIndex = newMethodContains.index(value)
            value = methodContians[methodIndex][1]
        else:
            if value in newClasscontains:
                methodIndex = newClasscontains.index(value)
                value = classContains[methodIndex][1]
            else:
                value = value
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
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        # print('mul')
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
        
        if left_type == "noValue":
            return left_type
        
        print("left mul", left)
        print('left mul type: ',left_type)

        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        if right_type == "noValue":
            return right_type
        print("right mul: ",right)
        print('right mul type:', right_type)
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        elif left_type == "Bool" and right_type == "Int":
            return right_type
        elif left_type == "Int" and right_type == "Bool":
            return left_type
        elif left_type == "Bool" and right_type == "Bool":
            return left_type
        # errors
        elif left_type == "String" and right_type == "String":
            return "charAr"
        elif left_type == "Int" and right_type == "String":
            return "intchar"
        elif left_type == "String" and right_type == "Int":
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
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
                
        left = self.visit(ctx.expr(0))
        
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        
        if left_type == "Int" and right_type == "Int":
            return "Bool"
        if left_type == "Int" and right_type == "Bool":
            return "Bool"
        if left_type == "Bool" and right_type == "Int":
            return "Bool"
        else:
            return "notLessorequal"
        

    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#lt.
    def visitLt(self, ctx:YAPLParser.LtContext):
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
                
        left = self.visit(ctx.expr(0))
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        if left_type == "Int" and right_type == "Int":
            return "Bool"
        if left_type == "Int" and right_type == "Bool":
            return "Bool"
        if left_type == "Bool" and right_type == "Int":
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
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left
            
        if left_type == "noValue":
            return left_type
        
        print("left_type: ",left_type )
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.contains_symbol(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right
        
        if right_type == "noValue":
            return right_type
        print("right_type: ",right_type )
        
        #revisar que no sean parte del algun del los errors
        if left_type in self.errors:
            return left_type
        if right_type in self.errors:
            return right_type
        
        if left_type == "Int" and right_type == "Int":
            return left_type
        elif left_type == "Bool" and right_type == "Int":
            return right_type
        elif left_type == "Int" and right_type == "Bool":
            return left_type
        elif left_type == "Bool" and right_type == "Bool":
            return left_type
        # errors
        elif left_type == "String" and right_type == "String":
            return "charAr"
        elif left_type == "Int" and right_type == "String":
            return "intchar"
        elif left_type == "String" and right_type == "Int":
            return "intchar"
        else:
            return "ArithError"


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        print("\nvisitando equal")
        
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
                
        left = self.visit(ctx.expr(0)) 
        # left_type = self.symbol_table.get_symbol_type(left) if self.symbol_table.contains_symbol(left) else left
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                left_type = left 
            
        print("left equal", left)
        print('left equal type: ',left_type)
        print("=============================")
        #si no existe
        if left_type == "noValue":
            return  left_type
        
        
        right = self.visit(ctx.expr(1))
        # right_type = self.symbol_table.get_symbol_type(right) if self.symbol_table.get_symbol_type(right) else right
        if right in newMethodContains:
            methodIndex = newMethodContains.index(right)
            right_type = methodContians[methodIndex][1]
        else:
            if right in newClasscontains:
                methodIndex = newClasscontains.index(right)
                right_type = classContains[methodIndex][1]
            else:
                right_type = right 
        # print("right equal", right)
        if right_type in ["Int","String","Bool"]:
            if left_type == right_type:
                return "Bool"
            else:
                return "notequal"
        else:
            if left_type == "Int" and right_type == "Bool":
                return "Bool"
            elif left_type == "Bool" and right_type == "Int":
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
            existNew = self.symbol_table.contains_symbol(value)
            if existNew:
                newType = self.symbol_table.get_symbol_type(value)
                if str(newType) == "class":
                    existNew = True
                else:
                    existNew = False
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
                contain = [value,self.actual_method_type,self.actual_class]
            else:
                contain.extend(contains)
                contain.append([value,self.actual_method_type,self.actual_class])
                
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
                return result
            
        return results
        
    # Visit a parse tree produced by YAPLParser#ownMethodCall.
    def visitOwnMethodCall(self, ctx:YAPLParser.OwnMethodCallContext):
        print("\nvisitOwnMethodCall")
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
        
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
                if firstType == "String":
                    message = "SELF_TYPE"
                else:
                    if firstType in newMethodContains:
                        methodIndex = newMethodContains.index(firstType)
                        firstType = methodContians[methodIndex][1]
                    else:
                        if firstType in newClasscontains:
                            methodIndex = newClasscontains.index(firstType)
                            firstType = classContains[methodIndex][1]
                        else:
                            firstType = firstType
                    if firstType == "String":
                        message = "SELF_TYPE"
                
            elif id == "out_int":
                first = expresions.pop(0)
                firstType = self.visit(first)
                if firstType == "Int":
                    message = "SELF_TYPE"
                else:
                    # firstType = self.symbol_table.get_symbol_type(firstType) if self.symbol_table.get_symbol_type(firstType) else firstType
                    if firstType in newMethodContains:
                        methodIndex = newMethodContains.index(firstType)
                        firstType = methodContians[methodIndex][1]
                    else:
                        if firstType in newClasscontains:
                            methodIndex = newClasscontains.index(firstType)
                            firstType = classContains[methodIndex][1]
                        else:
                            firstType = firstType
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
            else:
                if secondType in newMethodContains:
                    methodIndex = newMethodContains.index(secondType)
                    secondType = methodContians[methodIndex][1]
                else:
                    if secondType in newClasscontains:
                        methodIndex = newClasscontains.index(secondType)
                        secondType = classContains[methodIndex][1]
                    else:
                        secondType = secondType
                if secondType == "String":
                    message = "String"
        elif id == "substr":
            second = expresions.pop(0)
            secondType = self.visit(second)
            if secondType in newMethodContains:
                methodIndex = newMethodContains.index(secondType)
                secondType = methodContians[methodIndex][1]
            else:
                if secondType in newClasscontains:
                    methodIndex = newClasscontains.index(secondType)
                    secondType = classContains[methodIndex][1]
                else:
                    secondType = secondType
            
            third = expresions.pop(0)
            thirdType = self.visit(third)
            if thirdType in newMethodContains:
                methodIndex = newMethodContains.index(thirdType)
                thirdType = methodContians[methodIndex][1]
            else:
                if thirdType in newClasscontains:
                    methodIndex = newClasscontains.index(thirdType)
                    thirdType = classContains[methodIndex][1]
                else:
                    thirdType = thirdType
            
            if secondType == "Int" and thirdType == "Int":
                message = "String"
                
        #el id es un metodo que se esta volviendo a llamar?
        actualClassContains = self.symbol_table.get_contains(self.actual_class)
        newactualClassContains = []
        for acc in actualClassContains:
            newactualClassContains.append(acc[0])
        if actualClassContains != None:
            if id in newactualClassContains:
                first = expresions.pop(0) if len(expresions) > 0 else False
                if first != False:
                    firstType = self.visit(first)
                    print("visitOwnMethodCall firstType: ",firstType)
                    methodContians = self.symbol_table.get_contains(self.actual_method)
                    # print("methodContians: ",methodContians)
                    classContains = self.symbol_table.get_contains(self.actual_class)
                    # print("classContains: ",classContains)

                    newClasscontains = []
                    newMethodContains = []
                    
                    if classContains != None:
                        for cc in classContains:
                            newClasscontains.append(cc[0])
                    if methodContians != None:
                        for mc in methodContians:
                            newMethodContains.append(mc[0])
                    
                    if firstType in newMethodContains:
                        methodIndex = newMethodContains.index(firstType)
                        firstType = methodContians[methodIndex][1]
                    else:
                        if firstType in newClasscontains:
                            methodIndex = newClasscontains.index(firstType)
                            firstType = classContains[methodIndex][1]
                        else:
                            firstType = firstType
                    print("visitOwnMethodCall after firstType: ",firstType)
                    print("visitOwnMethodCall id: ",id , " :", type(id))
                    recieveMethod = self.symbol_table.get_recieves(id)
                    print("visitOwnMethodCall recieveMethod: ",recieveMethod)
                    ClassesrecieveMethod = []
                    for rm in recieveMethod:
                        ClassesrecieveMethod.append(rm[0])
                    
                    print("self.actual_class: ",self.actual_class)
                    print("ClassesrecieveMethod: ",ClassesrecieveMethod)
                    indexClass = ClassesrecieveMethod.index(str(self.actual_class))
                    recieveMethod = [recieveMethod[indexClass][1]]
                    print("indexClass: ",indexClass)
                    print("recieveMethod: ",recieveMethod)
                    
                    print("visitOwnMethodCall recieveMethod array")
                    newrecieveMethod = []
                    for x in recieveMethod:
                        for y in x:
                            newrecieveMethod.append(y[1])
                    print("visitOwnMethodCall newrecieveMethod: ",newrecieveMethod)
                    recieveMethod = newrecieveMethod
                    if type(firstType) != list:
                        firstType = [firstType]
                        
                    if firstType in recieveMethod:
                        index = recieveMethod.index(firstType)
                        recieveMethod = recieveMethod[index]
                    
                    if len(firstType) == len(recieveMethod):
                        for ft in firstType:
                            if ft in recieveMethod:
                                message = str(self.symbol_table.get_symbol_type(id))
                            else:
                                methodContians = self.symbol_table.get_contains(self.actual_method)
                                # print("methodContians: ",methodContians)
                                classContains = self.symbol_table.get_contains(self.actual_class)
                                # print("classContains: ",classContains)

                                newClasscontains = []
                                newMethodContains = []
                                
                                if classContains != None:
                                    for cc in classContains:
                                        newClasscontains.append(cc[0])
                                if methodContians != None:
                                    for mc in methodContians:
                                        newMethodContains.append(mc[0])
                                    
                                if ft in newMethodContains:
                                    methodIndex = newMethodContains.index(ft)
                                    ft = methodContians[methodIndex][1]
                                else:
                                    if ft in newClasscontains:
                                        methodIndex = newClasscontains.index(ft)
                                        ft = classContains[methodIndex][1]
                                    else:
                                        ft = ft
                                   
                                # ft = self.symbol_table.get_symbol_type(ft) if self.symbol_table.get_symbol_type(ft) else ft
                                if ft in recieveMethod:
                                    message = str(self.symbol_table.get_symbol_type(id))
                                else:
                                    message = "methodValuesNotSame"
                                    break
                    else:
                        message = "NotSameLenght"
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
        # print("left_type: ",left_type)
        
        #revisar que el left exista en contains del metodo o incluso de la misma clase
        methodContians = self.symbol_table.get_contains(self.actual_method)
        # print("methodContians: ",methodContians)
        classContains = self.symbol_table.get_contains(self.actual_class)
        # print("classContains: ",classContains)

        newClasscontains = []
        newMethodContains = []
        
        if classContains != None:
            for cc in classContains:
                newClasscontains.append(cc[0])
        if methodContians != None:
            for mc in methodContians:
                newMethodContains.append(mc[0])
            
        if left in newMethodContains:
            methodIndex = newMethodContains.index(left)
            left_type = methodContians[methodIndex][1]
        else:
            if left in newClasscontains:
                methodIndex = newClasscontains.index(left)
                left_type = classContains[methodIndex][1]
            else:
                return "assignError"
                    
        if expresion in newMethodContains:
            methodIndex = newMethodContains.index(expresion)
            expresionType = methodContians[methodIndex][1]
        else:
            if expresion in newClasscontains:
                methodIndex = newClasscontains.index(expresion)
                expresionType = classContains[methodIndex][1]
            else:
                expresionType = expresion
        
        print("expresionType: ",expresionType if expresionType else "Vacio")
        print("left_type: ",left_type if left_type else "Vacio")

        #revisar si existe la expresion
        # print(type(expresion))
        if str(expresion) == 'False':
            return "assignEr"
        
        if expresionType in self.errors:
            return expresionType
        
        if expresionType not in ["Int","String","Bool","Void","Object"]:
            #obtener los contains
            array = []
            expresionContains = self.symbol_table.get_contains(expresion)
            leftContains = self.symbol_table.get_contains(left)
            print("expresionContains: ",expresionContains)
            print("leftContains: ",leftContains)
            if leftContains == None:
                if expresionContains != None:
                    array.extend(expresionContains)
            else:
                array.extend(leftContains)
                
                newleftContains = []
                for lc in leftContains:
                    newleftContains.append(lc[0])
                newexpresionContains = []
                for ec in expresionContains:
                    newexpresionContains.append(ec[0])
                for nec in newexpresionContains:
                    if nec not in newleftContains:
                        index = newexpresionContains.index(nec)
                        array.append(expresionContains[index])
                
            result = []
            seen = set()
            print("assign visitado array: ",array)
            for sublist in array:
                if tuple(sublist) not in seen:
                    result.append(sublist)
                    seen.add(tuple(sublist))
            print("result: ",result)
            self.symbol_table.add_symbol(left,contains=result)
            
        #revisar si expresion inhertis de algun otro y si es asi convertirlo en lista lo de expresion
        exprInhertis = self.symbol_table.get_inherits(expresion)
        # print("expresion type: ",type(expresion))
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
            elif left_type == "Bool":
                if "Int" in expresion:
                    return left_type
            elif left_type == "Int":
                if "Bool" in expresion:
                    return left_type
            else:                    
                return "assignEr"
        else:
            print("No es una lista")
            print("left_type: ",left_type)
            print("expresion: ",expresion)
            if str(left_type) == str(expresion):
                print("Se esta regresando este: ",left_type)
                self.symbol_table.add_symbol(left,width=self.bytesSize)
                return left_type
            elif str(left_type) == "Bool" and str(expresion) == "Int":
                return left_type
            elif str(left_type) == "Int" and str(expresion) == "Bool":
                return left_type
            else:
                expresion = expresionType
                print("new expresion: ",expresion)
                if left_type == expresion:
                    return left_type
                elif str(left_type) == "Bool" and str(expresion) == "Int":
                    return left_type
                elif str(left_type) == "Int" and str(expresion) == "Bool":
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
            # print("substr secondType: ",secondType)
            # print("substr thirdType: ",thirdType)
            if secondType == "Int" and thirdType == "Int":
                message = "String"
        elif id == "isNil":
            message = "Bool"
        
        if str(inherist) == "IO":
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
             
        #revisar si el id es un metodo llamda utuilziando la primera expresion   
        firstContains = self.symbol_table.get_contains(firstType)
        print("visitMethodCall firstContains: ",firstContains)
        newfirstContains = []
        if firstContains != None:
            for fc in firstContains:
                newfirstContains.append(fc[0])

        print("visitMethodCall newfirstContains: ", newfirstContains)
        if firstContains != None:
            if id in newfirstContains:
                nextArray = []
                while(len(expresions) > 0):
                    next = expresions.pop(0) if len(expresions) > 0 else False
                    if next != False:
                        nextType = self.visit(next)
                        print("visitMethodCall nextType: ",nextType)
                        methodContians = self.symbol_table.get_contains(self.actual_method)
                        print("methodContians: ",methodContians)
                        classContains = self.symbol_table.get_contains(self.actual_class)
                        print("classContains: ",classContains)

                        newClasscontains = []
                        newMethodContains = []
                        
                        if classContains != None:
                            for cc in classContains:
                                newClasscontains.append(cc[0])
                        if methodContians != None:
                            for mc in methodContians:
                                newMethodContains.append(mc[0])
                            
                        if nextType in newMethodContains:
                            methodIndex = newMethodContains.index(nextType)
                            nextType = methodContians[methodIndex][1] if methodContians[methodIndex][1] != "class" else nextType
                        else:
                            if nextType in newClasscontains:
                                methodIndex = newClasscontains.index(nextType)
                                nextType = classContains[methodIndex][1] if classContains[methodIndex][1] != "class" else nextType
                            else:
                                nextType = nextType

                        # nextType = self.symbol_table.get_symbol_type(nextType) if self.symbol_table.get_symbol_type(nextType) and str(self.symbol_table.get_symbol_type(nextType))!="class" else nextType
                        print("visitMethodCall nextType after: ",nextType)
                        
                        if type(nextType) != list:
                            nextArray.append(nextType)
                        else:
                            nextArray.extend(nextType)
                print("id: ",id)
                
                nextArray = [firstType,nextArray]
                idRecieves = self.symbol_table.get_recieves(id)
                print("visitMethodCall idRecieves: ",idRecieves)
                print("visitMethodCall nextArray before: ",nextArray)
                
                if idRecieves != False:
                    idRecievesClasses = []
                    for ir in idRecieves:
                        idRecievesClasses.append(ir[0])
                    print("idRecievesClasses: ",idRecievesClasses)
                    print("newclassContains: ",newClasscontains)
                    
                    if nextArray[0] in idRecievesClasses:
                        indexClasses = idRecievesClasses.index(nextArray[0])
                    elif nextArray[0] in newClasscontains:
                        ind = newClasscontains.index(nextArray[0])
                        val = classContains[ind][1]
                        indexClasses = idRecievesClasses.index(val)
                    #es tipo inhertis el valor
                    else:
                        inhe = self.symbol_table.get_inherits(firstType)
                        # print("inhe: ",inhe)
                        # print("type(inhe): ",type(str(inhe)))
                        while str(inhe) != str(False):
                            print("inhe: ",inhe)
                            if str(inhe) in idRecievesClasses:
                                indexClasses = idRecievesClasses.index(str(inhe))
                                break
                            else:
                                inhe = str(self.symbol_table.get_inherits(str(inhe)))
                    # print("inherits: ",self.symbol_table.get_inherits(firstType))
                        
                    idRecieves = [idRecieves[indexClasses][1]]
                    idRecievesValues = []
                    tempidRecieves = []
                    for x in idRecieves:
                        for y in x:
                            tempidRecieves.append(y[1])
                    idRecievesValues.append(tempidRecieves)
                    
                    nextArray = nextArray[1]
                    print("visitMethodCall modified idRecieves: ",idRecieves)
                    print("visitMethodCall idRecievesValues: ",idRecievesValues)
                    print("visitMethodCall modified nextArray: ",nextArray)
                    idRecieves = idRecievesValues
                    if len(nextArray) == 1:
                        if len(nextArray) != len(idRecieves[0]):
                            return "NotSameLenght"
                        
                        if nextArray in idRecieves:
                            index = idRecieves.index(nextArray)
                        elif nextArray == ["Bool"] and ["Int"] in idRecieves:
                            index = idRecieves.index(["Int"])
                        elif nextArray == ["Int"] and ["Bool"] in idRecieves:
                            index = idRecieves.index(["Bool"])
                        else:
                            return "methodValuesNotSame"
                    else:
                        temporalIdRecieves = idRecieves[0]
                        if len(temporalIdRecieves) == len(nextArray):
                            for tir in range(len(temporalIdRecieves)):
                                if temporalIdRecieves[tir] == nextArray[tir]:
                                    pass
                                elif temporalIdRecieves[tir] == "Bool" and nextArray[tir] == "Int":
                                    pass
                                elif temporalIdRecieves[tir] == "Int" and nextArray[tir] == "Bool":
                                    pass
                                else:
                                    return "methodValuesNotSame"
                            index = idRecieves.index(temporalIdRecieves)
                        else:
                            return "NotSameLenght"
                            
                    idRecieves = idRecieves[index]
              
                print("visitMethodCall new idRecieves: ",idRecieves)
                
                if idRecieves != False:
                    print("visitMethodCall new nextArray: ",nextArray)
                    nextArray_copy = nextArray[:]  
                    newidRecieves = idRecieves[:]
                    if len(nextArray) == len(idRecieves):
                        for nt in nextArray_copy:
                            if nt in newidRecieves:
                                nextArray.remove(nt)  
                                newidRecieves.remove(nt)  
                            elif str(nt) == "Int":
                                if "Bool" in newidRecieves:
                                    nextArray.remove("Int")  
                                    newidRecieves.remove("Bool")
                            elif str(nt) == "Bool":
                                if "Int" in newidRecieves:
                                    nextArray.remove("Bool")  
                                    newidRecieves.remove("Int")
                            else:
                                message = "methodValuesNotSame"
                            
                        if len(nextArray) == 0:
                            print("visitMethodCall firstContains: ",firstContains)
                            print("visitMethodCall newfirstContains: ", newfirstContains)
                            Index = newfirstContains.index(id)
                            message = firstContains[Index][1]
                        else:
                            message = "methodValuesNotSame"

                        # for nt in nextArray:
                        #     if nt in idRecieves:
                        #         message = str(self.symbol_table.get_symbol_type(id))
                        #     else:
                        #         message = "methodError"
                        #         break
                    else:
                        message = "NotSameLenght"
                else:
                    index = newfirstContains.index(id)
                    message = firstContains[index][1]
                    # message = str(self.symbol_table.get_symbol_type(id))
                    
                    
                    
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
            width=8
        elif  str(letinType) == "String":
            width=4
        elif str(letinType) == "Bool":
            width=2
        else: 
            print("No existe este tipo por lo tanto toca buscar en la tabla")
            symbolExist = self.symbol_table.contains_symbol(letinType)
            if symbolExist:
                symbolType = self.symbol_table.get_symbol_type(letinType)
                if symbolType != False:
                    if str(symbolType) == "class":
                        width=4
                else:
                    return "assignError"
            else:
                return "assignError"
        
        # self.symbol_table.add_symbol(id,type=letinType,width=width,ambit="Local")
        
        # print("self.actual_method: ",self.actual_method)
        #agregarlo en su contains
        
        contains = self.symbol_table.get_contains(self.actual_method)
        # recieve = self.symbol_table.get_recieves(self.actual_method)
        # print("visitLetIn recieves: ",recieve)
        array = []
        if contains == None:
            array.append([id,letinType,self.actual_class])
        else:
            array.append([id,letinType,self.actual_class])
            array.extend(contains)
        print("array: ",array)
        
        result = []
        seen = set()

        for sublist in array:
            if tuple(sublist) not in seen:
                result.append(sublist)
                seen.add(tuple(sublist))    
        array = result
        
        self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        
        result = self.visit(ctx.expr())
        
        # array.pop(0)
        # self.symbol_table.add_symbol(self.actual_method,self.actual_method_type,contains=array)
        # if idClassType != None:
        # self.symbol_table.add_symbol(id,type=idClassType,width=idClassWidth,ambit=idClassAmbit)
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
        
        
        self.symbol_table.add_symbol(id,typevisit,ambit="Local")
        
        print("self.actual_method: ", self.actual_method)
        
        #agregar el nuevo simbolo en contians del metodo
        contains = self.symbol_table.get_contains(self.actual_method)
        print("contains: ",contains)
        array = []
        if contains == None:
            array.append([id,typevisit,self.actual_class])
        else:
            array.append([id,typevisit,self.actual_class])
            array.extend(contains)
            
        
        print("array: ",array)
        result = []
        seen = set()

        for sublist in array:
            if tuple(sublist) not in seen:
                result.append(sublist)
                seen.add(tuple(sublist))    
        array = result
        
        self.symbol_table.add_symbol(self.actual_method, self.actual_method_type, contains=array)
        
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
            methodContians = self.symbol_table.get_contains(self.actual_method)
            # print("methodContians: ",methodContians)
            classContains = self.symbol_table.get_contains(self.actual_class)
            # print("classContains: ",classContains)

            newClasscontains = []
            newMethodContains = []
            
            if classContains != None:
                for cc in classContains:
                    newClasscontains.append(cc[0])
            if methodContians != None:
                for mc in methodContians:
                    newMethodContains.append(mc[0])
                    
            if assignValue in newMethodContains:
                methodIndex = newMethodContains.index(assignValue)
                assignValue = methodContians[methodIndex][1]
            else:
                if assignValue in newClasscontains:
                    methodIndex = newClasscontains.index(assignValue)
                    assignValue = classContains[methodIndex][1]
                else:
                    assignValue = assignValue
            
            # assignValue = self.symbol_table.get_symbol_type(assignValue) if self.symbol_table.get_symbol_type(assignValue) else assignValue
        
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
            
        # if idClassType != None:
        #     self.symbol_table.add_symbol(id,type=idClassType,width=idClassWidth,ambit=idClassAmbit)
        
        print("visitLetAssignIn results: ",resutls)
        return resutls



del YAPLParser