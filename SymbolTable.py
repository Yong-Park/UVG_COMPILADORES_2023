class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, type=None, inherits=None, width=None, displacement=None, ambit=None, recieves=None):
        symbol = {
            'type': str(type) if type!= None else None,
            'inherits': str(inherits) if inherits!=None else None,
            'width': str(width) if width!=None else None,
            'displacement': str(displacement) if displacement!=None else None,
            'ambit': str(ambit) if ambit!=None else None,
            'recieves': recieves if recieves!=None else None
        }
        symbols = self.symbols.get(str(name))
        # print("tablesymbol symbols: ",symbols)
        symbolNameExist = False
        if symbols:
            for symbolCheck in symbols:
                # print("symbol['ambit']: ",symbol['ambit'])
                if str(symbolCheck['ambit']) == str(ambit) and str(symbolCheck['type']) == str(type):
                    symbolNameExist = True
            # se agregara si este es Falso ya que significa que no existe
            if symbolNameExist == False:
                self.symbols.setdefault(str(name), []).append(symbol)
        else:
            self.symbols.setdefault(str(name), []).append(symbol)
        
        
        
    def get_ambit_symbols(self,ambit):
        filtered_symbols = {k: v for k, v in self.symbols.items() if any(d['ambit'] == str(ambit) for d in v)}
        return filtered_symbols

    
    def change_symbol_value(self, name, ambit, element ,value):
        symbols = self.symbols.get(str(name))
        if symbols:
            for symbol in symbols:
                if symbol['ambit'] == str(ambit):
                    symbol[str(element)] = value
                    break
                
    def get_symbol_value(self,name,ambit,element):
        # print("ambit: ",ambit)
        symbols = self.symbols.get(str(name))
        if symbols:
            # print("symbols: ",symbols)
            for symbol in symbols:
                # print("symbol['ambit']: ",symbol['ambit'])
                if symbol['ambit'] == str(ambit):
                    return symbol[str(element)] 
        return False
                
    def contains_symbol(self,name,ambit):
        symbols = self.symbols.get(str(name))
        # print("symbols: ",symbols)
        if symbols:
            for symbol in symbols:
                # print("symbol['ambit']: ",symbol['ambit'])
                if symbol['ambit'] == str(ambit):
                    return True
        return False
    
    def contains_class(self,name):
        symbols = self.symbols.get(str(name))
        if symbols:
            for symbol in symbols:
                # print("symbol: ",symbol)
                if symbol["type"] == "class":
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
        symbols = self.symbols.get("main")
        if symbols:
            for symbol in symbols:
                if symbol["ambit"] == "Main":
                    return True
        return False

    
    

