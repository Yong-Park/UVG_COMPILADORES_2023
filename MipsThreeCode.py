class Terceto():

    def __init__(self, o=None, x=None, y=None, l=None):
        self.o = o
        self.x = x
        self.y = y
        self.l = l

    def keys(self):
        return ["l", "o", "x", "y"]

    def values(self):
        l = self.l if self.l != None else ""
        y = self.y if self.y != None else ""

        return [l, self.o, self.x, y]


class ThreeAddressCode():
    def __init__(self):
        self.tercetos = []
        
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

        if not r:
            # Compiler Three Address Code Reference
            r = "_r{i}".format(i=len(self.tercetos))

        # if not l:
        #     # Compiler Three Address Code Label
        #     l = "l_{i}".format(i=len(self.tercetos))

        terceto = Terceto(o, x, y, l)
        self.tercetos.append(terceto)

        return terceto, r
