import os
class Terceto():

    def __init__(self, o=None, s=None, x=None, y=None, l=None):
        self.o = o
        self.s = s
        self.x = x
        self.y = y
        self.l = l

class ThreeAddressCode():
    def __init__(self):
        self.classElements = []
        self.labels = []
        self.labelsCopy = []
        self.temporals = []
        self.tercetos = []
        self.text_data = []
        self.visitProperties = []
        
    def addVisitProperties(self,value):
        self.visitProperties.append(str(value))
        
    def clearVisitProperties(self):
        self.visitProperties = []
        
    def clearClassElements(self):
        self.classElements = []
    
    def clearTemporals(self):
        self.temporals = []
        
    def clearLabels(self):
        self.labelsCopy = []
        
    def newTemporal(self):
        temporals = self.temporals
        num = 0
        while True:
            temporalToAdd = "$t" + str(num)
            if str(temporalToAdd) in temporals:
                num += 1
            else:
                self.temporals.append(str(temporalToAdd))
                break
        return str(temporalToAdd)
    
    def newTextPositionAdd(self,recieved):
        texts = self.text_data
        text = []
        for t in texts:
            text.append(t[0])
        
        num = 0
        while True:
            textToAdd = "text_" + str(num)
            if str(textToAdd) in text:
                num += 1
            else:
                self.text_data.append([str(textToAdd),str(recieved)])
                break
        return str(textToAdd)

    #para obtener desde el label tal hasta su label_endtask
    def getLabelsArray(self,label):
        addLables = False
        labelArray = []
        for tac in self.tercetos:
            if tac.l == str(label):
                addLables = True
            if tac.l == str(str(label)+"_EndTask"):
                labelArray.append(tac)
                addLables = False
            if addLables:
                labelArray.append(tac)
        return labelArray
                
        
        
    #para guardar los que sean tipo labels 
    def addLables(self, value, ambit):
        registros = []
        for registross in self.labels:
            registros.append(registross[1])
            
        num = 0
        while True:
            label = str("L") + str(num)
            if label in registros:
                num += 1
            else:
                #agregar este elementos en elementos de la clase actual
                self.labels.append([str(value),str(label),str(ambit)])
                self.labelsCopy.append([str(value),str(label),str(ambit)])
                break
        
    #value es el nombre de la variable
    #regirsto es el tipo, digamos es s0,t0 y asi
    def addClassElements(self,value,registro,displacement):
        registros = []
        for registross in self.classElements:
            registros.append(registross[1])
            
        num = 0
        while True:
            label = str(registro) + str(num)
            if label in registros:
                num += 1
            else:
                #agregar este elementos en elementos de la clase actual
                self.classElements.append([str(value),str(label),str(displacement)])
                break
        
        # self.classElements.append([str(value),str(registro)])
    def deleteSpecifiLabel(self,label):
        registrosList = []
        for registro in self.labelsCopy:
            registrosList.append(registro[1])
        
        indice = registrosList.index(str(label))
        self.labelsCopy.pop(indice)
        
    #uso principalente para el if ya que de esta forma puedo tener un orden mejor de los if para obtener el label correcto
    def returnSpecificLabelInCopy(self,value,ambit):
        # print("value: ",value)
        # print("self.labelsCopy: ",self.labelsCopy)
        registrosList = []
        for registro in self.labelsCopy:
            if registro[0] == str(value) and registro[2] == str(ambit):
                registrosList.append(registro[1])
                
        if len(registrosList) > 0:
            return registrosList[len(registrosList)-1]
        else:
            return None
    #este se usa para busacar en todo el label. Idealmente no deberia de haber repetidos, a excepcion de los if.
    def returnSpecificLabel(self,value,ambit):
        # print("value: ",value)
        # print("self.labelsCopy: ",self.labelsCopy)
        registrosList = []
        for registro in self.labels:
            if registro[0] == str(value) and registro[2] == str(ambit):
                registrosList.append(registro[1])
                
        if len(registrosList) > 0:
            return registrosList[len(registrosList)-1]
        else:
            return None
    
    #para regresar el valor del label
    def returnLabelValue(self,label):
        for ll in self.labels:
            if str(ll[1]) == str(label):
                return ll[0]
        if "_EndTask" in label:
            return label 
        
    def returnSpecificRegistroByLabel(self,label):
        for registro in self.labels:
            if registro[1] == str(label):
                return registro[0]
    
        
    def returnSpecificRegistro(self,value):
        registrosList = []
        for registro in self.classElements:
            if registro[0] == str(value):
                registrosList.append(registro[2])

        if len(registrosList) > 0:
            return registrosList[len(registrosList)-1]
        else:
            return None
        
    def printTacLabel(self):
        with open("output/tacResultLabel.txt", 'w') as file:
            # file.write("Three Direction Code"+ "\n")
            file.write(".data\n")
            file.write("\tGP: .space 0\n")
            file.write("\tLP: .space 0\n")
    
            for tac in self.tercetos:
                if tac.l != None and "_EndTask" in tac.l: 
                    file.write(str(tac.l).split("_")[0]+"_"+str(tac.l).split("_")[1] + ":="+ "\n")
                elif tac.l != None and "_EndTask" not in tac.l:
                    file.write(str(tac.l) + ":="+ "\n")
                elif tac.o == "<-":
                    file.write("\t" + str(tac.s) + " " + str(tac.o) + " " + str(tac.x) + "\n")
                elif tac.o == "add":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " + " + str(tac.y)+ "\n")
                elif tac.o == "sub":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " - " + str(tac.y)+ "\n")
                elif tac.o == "div":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " / " + str(tac.y)+ "\n")
                elif tac.o == "mul":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " * " + str(tac.y)+ "\n")
                elif tac.o == "beq":
                    file.write("\t" + str(tac.x) + " == " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "ble":
                    file.write("\t" + str(tac.x) + " <= " + str(tac.y) + " GOTO " + str(tac.s) + "\n")
                elif tac.o == "blt":
                    file.write("\t" + str(tac.x) + " < " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "and":
                    file.write("\t" + str(tac.x) + " & " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "or":
                    file.write("\t" + str(tac.x) + " | " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "call" and not tac.x and not tac.y:
                    file.write("\t" + "CALL " + str(tac.s)+ "\n")
                elif tac.o == "call" and not tac.y:
                    # file.write("\t" + str(tac.s) + " <- " + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.x)) if "." not in str(tac.x) else str(tac.x)) + "\n")
                    file.write("\t" + str(tac.s) + " <- " + "CALL " + str(tac.x) + "\n")
                elif tac.o == "call" and tac.y:
                    file.write("\t" + str(tac.s) + " <- " + "CALL " + str(tac.x if "." not in str(tac.x) else str(tac.x)) +  "(" + str(str(tac.y)[1:-1].replace("'","") if str(tac.y)[0] == "[" else str(tac.y)) +")"+ "\n")
                elif tac.o == "j":
                    file.write("\t" + "GOTO " + str(tac.s)+ "\n")
                elif tac.o == "not":
                    file.write("\t" + str(tac.s) + " <- " + " NOT " + str(tac.x)+ "\n")
                elif tac.o == "isvoid":
                    file.write("\t" + str(tac.s) + " <- " + "ISVOID " + str(tac.x)+ "\n")
                elif tac.o == "invert":
                    file.write("\t" + str(tac.s) + " <- " + "INVERT " + str(tac.x)+ "\n")
                elif tac.o == "create":
                    file.write("\t" + str(tac.s) + " CREATED AS "+ str(tac.x)+ "\n")
                elif tac.o == "bnq": 
                    file.write("\t" + str(tac.x) + " != " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "bg":
                    file.write("\t" + str(tac.x) + " > " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                elif tac.o == "bgt":
                    file.write("\t" + str(tac.x) + " >= " + str(tac.y) + " GOTO " + str(tac.s)+ "\n")
                else:
                    file.write("\t" + str(tac.o) + " " + str(tac.s) + " " + str(tac.x) + " " + str(tac.y)+ "\n")
            if len(self.text_data) != 0:
                file.write(".data: " + "\n")
                for texts in self.text_data:
                    file.write("\t" + str(texts[0]) + ': .asciiz "' + str(texts[1]) + '"\n')
    
    def printTac(self):
        allLabels = []
        for l in self.labels:
            allLabels.append(l[1])
        
        with open("output/tacResult.txt", 'w') as file:
            # file.write("Three Direction Code"+ "\n")
            file.write(".data\n")
            file.write("\tGP: .space 40\n")
            file.write("\tLP: .space 40\n")
            for tac in self.tercetos:
                if tac.l != None and "_EndTask" in tac.l: 
                    file.write(str(self.returnSpecificRegistroByLabel(str(tac.l).split("_")[0]))+"_"+str(tac.l).split("_")[1] + ":="+ "\n")
                elif tac.l != None and "_EndTask" not in tac.l:
                    file.write(str(self.returnSpecificRegistroByLabel(str(tac.l))) + ":="+ "\n")
                elif tac.o == "<-":
                    file.write("\t" + str(tac.s) + " " + str(tac.o) + " " + str(tac.x) + "\n")
                elif tac.o == "add":
                    file.write("\tadd " + str(tac.s) + ", " + str(tac.x) + ", " + str(tac.y)+ "\n")
                elif tac.o == "sub":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " - " + str(tac.y)+ "\n")
                elif tac.o == "div":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " / " + str(tac.y)+ "\n")
                elif tac.o == "mul":
                    file.write("\t" + str(tac.s) + " <- " + str(tac.x) + " * " + str(tac.y)+ "\n")
                elif tac.o == "beq":
                    file.write("\t" + str(tac.x) + " == " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "ble":
                    file.write("\t" + str(tac.x) + " <= " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s))) + "\n")
                elif tac.o == "blt":
                    file.write("\t" + str(tac.x) + " < " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "bnq": 
                    file.write("\t" + str(tac.x) + " != " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "bg":
                    file.write("\t" + str(tac.x) + " > " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "bgt":
                    file.write("\t" + str(tac.x) + " >= " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "and":
                    file.write("\t" + str(tac.x) + " & " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "or":
                    file.write("\t" + str(tac.x) + " | " + str(tac.y) + " GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "call" and not tac.x and not tac.y:
                    file.write("\t" + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "call" and not tac.y:
                    if tac.x not in allLabels:
                    # file.write("\t" + str(tac.s) + " <- " + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.x)) if "." not in str(tac.x) else str(tac.x)) + "\n")
                        file.write("\t" + str(tac.s) + " <- " + "CALL " + str(tac.x) + "\n")
                    else:
                        file.write("\t" + str(tac.s) + " <- " + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.x))) + "\n")
                elif tac.o == "call" and tac.y:
                    if tac.x not in allLabels:
                    # file.write("\t" + str(tac.s) + " <- " + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.x)) if "." not in str(tac.x) else str(tac.x)) +  "(" + str(str(tac.y)[1:-1].replace("'","") if str(tac.y)[0] == "[" else str(tac.y)) +")"+ "\n")
                        file.write("\t" + str(tac.s) + " <- " + "CALL " + str(tac.x) +  "(" + str(str(tac.y)[1:-1].replace("'","") if str(tac.y)[0] == "[" else str(tac.y)) +")"+ "\n")
                    else:
                        file.write("\t" + str(tac.s) + " <- " + "CALL " + str(self.returnSpecificRegistroByLabel(str(tac.x))) + "(" + str(str(tac.y)[1:-1].replace("'","") if str(tac.y)[0] == "[" else str(tac.y)) +")"+ "\n")
                elif tac.o == "j":
                    file.write("\t" + "GOTO " + str(self.returnSpecificRegistroByLabel(str(tac.s)))+ "\n")
                elif tac.o == "not":
                    file.write("\t" + str(tac.s) + " <- " + " NOT " + str(tac.x)+ "\n")
                elif tac.o == "isvoid":
                    file.write("\t" + str(tac.s) + " <- " + "ISVOID " + str(tac.x)+ "\n")
                elif tac.o == "invert":
                    file.write("\t" + str(tac.s) + " <- " + "INVERT " + str(tac.x)+ "\n")
                elif tac.o == "create":
                    file.write("\t" + str(tac.s) + " CREATED AS "+ str(tac.x)+ "\n")
                else:
                    file.write("\t" + str(tac.o) + " " + str(tac.s) + " " + str(tac.x) + " " + str(tac.y)+ "\n")
            if len(self.text_data) != 0:
                file.write(".data: " + "\n")
                for texts in self.text_data:
                    file.write("\t" + str(texts[0]) + ': .asciiz "' + str(texts[1]) + '"\n')
        
    # o es el tipo de operacion
    # s es donde se guardara el valor o el goto que realizara esto depende del o
    # x ex una variable que llega a recibir
    # y es una variable que llega a recibir
    # l es el label o pues nombre de un metodo o clase.
    def add(self, o=None, s=None, x=None, y=None, l=None):

        if type(o) not in [type(None), int, str]:
            o = str(o)
        
        if type(s) not in [type(None), int, str]:
            s = str(s)

        if type(x) not in [type(None), int, str]:
            x = str(x)

        if type(y) not in [type(None), int, str]:
            y = str(y)

        if type(l) not in [type(None), int, str]:
            l = str(l)

        terceto = Terceto(o, s, x, y, l)
        self.tercetos.append(terceto)

        return terceto
