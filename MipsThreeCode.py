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
        
    def clearClassElements(self):
        self.classElements = []
    
    def clearTemporals(self):
        self.temporals = []
        
    def clearLabels(self):
        self.labelsCopy = []
        
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
    def addClassElements(self,value,registro):
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
                self.classElements.append([str(value),str(label)])
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
    
        
    def returnSpecificRegistro(self,value):
        registrosList = []
        for registro in self.classElements:
            if registro[0] == str(value):
                registrosList.append(registro[1])

        if len(registrosList) > 0:
            return registrosList[len(registrosList)-1]
        else:
            return None
    
    
    def printTac(self):
        print("Three Direction Code")
        for tac in self.tercetos:
            if tac.l != None: 
                print(str(tac.l) + ":=")
            elif tac.o == "<-":
                print("\t" + str(tac.s) + " " + str(tac.o) + " " + str(tac.x))
            elif tac.o == "add":
                print("\t" + str(tac.s) + " <- " + str(tac.x) + " + " + str(tac.y))
            elif tac.o == "sub":
                print("\t" + str(tac.s) + " <- " + str(tac.x) + " - " + str(tac.y))
            elif tac.o == "div":
                print("\t" + str(tac.s) + " <- " + str(tac.x) + " / " + str(tac.y))
            elif tac.o == "mul":
                print("\t" + str(tac.s) + " <- " + str(tac.x) + " * " + str(tac.y))
            elif tac.o == "beq":
                print("\t" + str(tac.x) + " == " + str(tac.y) + " GOTO " + str(tac.s))
            elif tac.o == "ble":
                print("\t" + str(tac.x) + " <= " + str(tac.y) + " GOTO " + str(tac.s))
            elif tac.o == "blt":
                print("\t" + str(tac.x) + " < " + str(tac.y) + " GOTO " + str(tac.s))
            elif tac.o == "j":
                print("\t" + "GOTO " + str(tac.s))
            elif tac.o == "not":
                print("\t" + str(tac.s) + " <- " + " not " + str(tac.x))
            else:
                print("\t" + str(tac.o) + " " + str(tac.s) + " " + str(tac.x) + " " + str(tac.y))
        print("=============================")
        
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
