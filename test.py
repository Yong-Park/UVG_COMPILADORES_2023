class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, type=None, inherits=None, width=None, displacement=None, ambit=None, recieves=None):
        symbol = {
            'type': type,
            'inherits': inherits,
            'width': width,
            'displacement': displacement,
            'ambit': ambit,
            'recieves': recieves
        }
        self.symbols.setdefault(name, []).append(symbol)
    
    def change_symbol_value(self, name, ambit, element ,value):
        symbols = self.symbols.get(name)
        if symbols:
            for symbol in symbols:
                if symbol['ambit'] == ambit:
                    symbol[element] = value
                    break
                
    def get_symbol_value(self,name,ambit,element):
        symbols = self.symbols.get(name)
        if symbols:
            for symbol in symbols:
                if symbol['ambit'] == ambit:
                    return symbol[element] 
                
                
    def contains_symbol(self,name,ambit):
        symbols = self.symbols.get(name)
        if symbols:
            for symbol in symbols:
                if symbol['ambit'] == ambit:
                    return True
        return False
                    

    def __str__(self):
        table_str = "Symbol Table:\n"
        for name, symbols in self.symbols.items():
            for symbol in symbols:
                table_str += f"Name: {name}, "
                for attr, value in symbol.items():
                    table_str += f"{attr.capitalize()}: {value}, "
                table_str = table_str.rstrip(', ')  # Remove trailing comma and space
                table_str += "\n"
        return table_str

tabla = SymbolTable()

tabla.add_symbol('n', type="int", width=4, ambit='A')
tabla.add_symbol('n', type="str", width=8, ambit='B', inherits = "IO")
tabla.add_symbol('a', type="bool", width=2, ambit='B.method5')

print(tabla)
print(tabla.get_symbol_value("a","B.method5","width"))

tabla.change_symbol_value('a', 'B.method5', "width",8)
print(tabla)
print(tabla.get_symbol_value("a","B.method5","width"))
print(tabla.contains_symbol("a","B.method5"))
print(tabla.contains_symbol("a","B"))
