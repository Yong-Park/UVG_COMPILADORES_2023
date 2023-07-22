class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, type):
        self.symbols[name] = type

    def get_symbol_type(self, name):
        return self.symbols.get(name)
    
    def contains_symbol(self, name):
        return name in self.symbols

    def __str__(self):
        table_str = "Symbol Table:\n"
        for name, type in self.symbols.items():
            table_str += f"{name}: {type}\n"
        return table_str
