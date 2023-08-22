class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.inherits = {}
        self.width = {}
        self.displacement = {}
        self.contains = {}
        self.ambit = {}
        self.recieves = {}

    def add_symbol(self, name, type=None, inherits=None, width=None, displacement=None, contains=None, ambit=None, recieves=None):
        # print("new contains: ",contains)
        # print("new recieves: ",recieves)
        if type is not None:
            self.symbols[name] = type
        if inherits is not None:
            self.inherits[name] = inherits
        if width is not None:
            self.width[name] = width
        if displacement is not None:
            self.displacement[name] = displacement
        if contains is not None:
            self.contains[name] = contains
        if ambit is not None:
            self.ambit[name] = ambit
        if recieves is not None:
            self.recieves[name] = recieves
        # print("name: ",name)
        # print("self.recieves[name]: ",self.recieves[name])
        
        
    def get_recieves(self,name):
        return self.recieves.get(name, False)
        
    def get_contains(self, name):
        for Sname,_ in self.symbols.items():
            if str(Sname) == str(name):
                if self.contains.get(Sname or name):
                    return self.contains[Sname]
        # return self.contains[name] 
    
    def get_inherits(self,name):
        return self.inherits.get(name, False)

    def get_symbol_type(self, name):
        for Sname, type in self.symbols.items():
            if str(Sname) == name:
                return type 
        
        return False
        # return self.symbols.get(name)
    
    def variable_class(self,classname, name):
        if classname in self.contains and name in self.contains[classname]:
            return True 
        else:
            return False  
    
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
            table_str += f"\trecieves: {self.recieves.get(name, 'N/A')}\n"
        return table_str
    

