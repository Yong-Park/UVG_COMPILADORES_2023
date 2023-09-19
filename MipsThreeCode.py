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
        self.temporals = []
        self.tercetos = []
        
    def clearClassElements(self):
        self.classElements = []
    
    def clearTemporals(self):
        self.temporals = []
        
    #value es el nombre de la variable
    #regirsto es el tipo, digamos es s0,t0,l1 y asi
    def addClassElements(self,value,registro):
        self.classElements.append([str(value),str(registro)])
        
    def returnSpecificRegistro(self,value):
        for registro in self.classElements:
            if registro[0] == str(value):
                return registro[1]
        
    def returnRegistro(self):
        registros = []
        for registro in self.classElements:
            registros.append(registro[1])
            
        return registros
        
    # o es el tipo de operacion
    # s es donde se guardara el valor
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

        # return terceto
