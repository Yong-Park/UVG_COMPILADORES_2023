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
        return False
                
    def contains_symbol(self,name,ambit):
        symbols = self.symbols.get(name)
        # print("symbols: ",symbols)
        if symbols:
            for symbol in symbols:
                # print("symbol['ambit']: ",symbol['ambit'])
                if str(symbol['ambit']) == ambit:
                    return True
        return False
    
    def contains_class(self,name):
        symbols = self.symbols.get(name)
        if symbols:
            for symbol in symbols:
                # print("symbol: ",symbol)
                if str(symbol["type"]) == "class":
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
    
    def contains_mains(self):
        # MainExist = False
        # mainExist = False
        # for name, _ in self.symbols.items():
        #     if str(name) == "Main":
        #         MainExist = True
        
        # if MainExist:
        #     for name, _ in self.symbols.items():
        #         if str(name) == "Main":
        #             for values in self.contains[name]:
        #                 if str(values[0]) == "main":
        #                     mainExist = True
        # else:
        #     return False
        
        # if mainExist:
        #     return True
        # else:
        #     return False
        return True

    
    

