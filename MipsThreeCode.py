class Terceto():

    def __init__(self, o=None, x=None, y=None, l=None):
        self.o = o
        self.x = x
        self.y = y
        self.l = l

    def keys(self):
        print("keys visitado")
        return ["l", "o", "x", "y"]

    def values(self):
        print("values visitado")
        l = self.l if self.l != None else ""
        y = self.y if self.y != None else ""

        return [l, self.o, self.x, y]


class ThreeAddressCode():
    def __init__(self):
        self.classElements = []
        self.tercetos = []
        
    def clearClassElements(self):
        self.classElements = []
        
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
    # x ex una variable que llega a recibir
    # y es una variable que llega a recibir
    # l es el label o pues nombre de un metodo o clase.
    def add(self, o=None, x=None, y=None, l=None):

        if type(o) not in [type(None), int, str]:
            o = str(o)

        if type(x) not in [type(None), int, str]:
            x = str(x)

        if type(y) not in [type(None), int, str]:
            y = str(y)

        if type(l) not in [type(None), int, str]:
            l = str(l)

        terceto = Terceto(o, x, y, l)
        self.tercetos.append(terceto)

        return terceto
