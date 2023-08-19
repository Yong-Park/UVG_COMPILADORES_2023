class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.inherits = {}
        self.width = {}
        self.displacement = {}
        self.contains = {}
        self.ambit = {}

    def add_symbol(self, name, type, inherits=None, width=None, displacement=None, contains=None,ambit=None):
        self.symbols[name] = type
        self.inherits[name] = inherits
        self.width[name] = width
        self.displacement[name] = displacement
        self.contains[name] = contains
        self.ambit[name] = ambit
        
    def get_contains(self, name):
        for Sname,_ in self.symbols.items():
            if str(Sname) == str(name):
                if self.contains.get(Sname or name):
                    return self.contains[Sname]
        # return self.contains[name] 
    
    def get_inherits(self,name):
        return self.inherits[name] if self.inherits[name] else False

    def get_symbol_type(self, name):
        for Sname, type in self.symbols.items():
            if str(Sname) == name:
                return type 
        
        return False
        # return self.symbols.get(name)
    
    def variable_class(self,classname, name):
        return name in self.contains[classname]
    
    def contains_element(self,name, value):
        print("name: ",name)
        print("value: ",value)
        for Sname,_ in self.symbols.items():
            if str(Sname) == name:
                print("Sname: ",Sname)
                print("name: ",name)
                if self.contains.get(Sname):
                    for values in self.contains.get(Sname):
                        if str(values) == str(value):
                            print("values: ",values)
                            print("value: ",value)
                            return True
            else:
                return False
        
    
    def contains_mains(self):
        MainExist = False
        mainExist = False
        for name, _ in self.symbols.items():
            if str(name) == "Main":
                MainExist = True
        
        if MainExist:
            for name, _ in self.symbols.items():
                if str(name) == "Main":
                    for values in self.contains.get(name):
                        if str(values) == "main":
                            mainExist = True
        else:
            return False
        
        if mainExist:
            return True
        else:
            return False


    def contains_symbol(self, name):
        for Sname, _ in self.symbols.items():
            if str(Sname) == str(name):
                return True 
        
        return False

    def __str__(self):
        table_str = "Symbol Table:\n"
        for name, type in self.symbols.items():
            table_str += f"{name}: {type}\n"
            table_str += f"\tInherits: {self.inherits.get(name, 'N/A')}\n"
            table_str += f"\tWidth: {self.width.get(name, 'N/A')}\n"
            table_str += f"\tDisplacement: {self.displacement.get(name, 'N/A')}\n"
            table_str += f"\tContains: {self.contains.get(name, 'N/A')}\n"
            table_str += f"\tAmbit: {self.ambit.get(name, 'N/A')}\n"
        return table_str
    

