class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.inherits = {}
        self.width = {}
        self.displacement = {}
        self.contains = {}

    def add_symbol(self, name, type, inherits=None, width=None, displacement=None, contains=None):
        self.symbols[name] = type
        self.inherits[name] = inherits
        self.width[name] = width
        self.displacement[name] = displacement
        self.contains[name] = contains

    def get_symbol_type(self, name):
        return self.symbols.get(name)
    
    def variable_class(self,classname, name):
        return name in self.contains[classname]

    def contains_symbol(self, name):
        return name in self.symbols

    def __str__(self):
        table_str = "Symbol Table:\n"
        for name, type in self.symbols.items():
            table_str += f"{name}: {type}\n"
            table_str += f"\tInherits: {self.inherits.get(name, 'N/A')}\n"
            table_str += f"\tWidth: {self.width.get(name, 'N/A')}\n"
            table_str += f"\tDisplacement: {self.displacement.get(name, 'N/A')}\n"
            table_str += f"\tContains: {self.contains.get(name, 'N/A')}\n"
        return table_str
    

