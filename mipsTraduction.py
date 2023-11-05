class mipsTraduction():
    
    def __init__(self,direction):
        self.diccionario = {}
        self.controller = []
        with open(direction, "r") as file:
            self.lines = file.readlines()
            
    def adaptToMips(self):
        for line in self.lines:
            clean_line = line.split(" ")
            if ":=" in clean_line[0] and "EndTask:=" not in clean_line[0]:
                # agregar controlador y comenzar el diccionario correspondiente a ello
                self.controller.append(clean_line[0].split(":=")[0])
                self.diccionario[self.controller[len(self.controller)-1]] = [] 
                if "if_" in clean_line[0]:
                    # self.controller.pop(len(self.controller)-1)
                    # del self.diccionario[clean_line[0].split(":=")[0]]
                    if self.controller[len(self.controller)-2].split("_")[0] not in ["if","else","then","fi"]:
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                    else:
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tjr $ra\n")
                elif "else_" in clean_line[0]:
                    # self.diccionario["if_"+str(clean_line[0].split("_")[1].split(":")[0])].append("\tjr $ra\n")
                    self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                    
                elif "fi_" in clean_line[0]:
                    self.diccionario[self.controller[len(self.controller)-2]].append("\tj " +clean_line[0].split(":=")[0] + "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjr $ra\n")
                    
                    #eliminar todos los _algo de logica
                    self.controller.remove("if_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("then_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("else_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("fi_"+clean_line[0].split(":=")[0].split("_")[1])
                    
                    # self.diccionario["then_"+str(clean_line[0].split("_")[1].split(":")[0])].append("\tjr $ra\n")
                    # self.controller.remove("then_"+str(clean_line[0].split("_")[1].split(":")[0]))
                    # self.controller.pop(len(self.controller)-1)
                    # del self.diccionario[clean_line[0].split(":=")[0]]
                else:
                    self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                    if "main:=" in clean_line[0]:
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla $sp, 0x7FFFFFC0\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsub $sp, $sp, 40\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($sp)\n")
                
                #Ahora aplicamos la misma lógica para el while
                if "while_" in clean_line[0]:
                    #print("Holaaaaaaaaaaaaaaaaaaa")
                    if self.controller[len(self.controller)-2].split("_")[0] not in ["while","loop","pool"]:
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                    else:
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                #Detectamos si se encuentra la etiqueta loop
                elif "loop_" in clean_line[0]:
                    self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                #Detectamos si se encuentra la etiqueta pool
                elif "pool_" in clean_line[0]:
                    self.diccionario[self.controller[len(self.controller)-2]].append("\tj " +clean_line[0].split(":=")[0] + "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjr $ra\n")
                    
                    #eliminar todos los _algo de logica
                    self.controller.remove("while_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("loop_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("pool_"+clean_line[0].split(":=")[0].split("_")[1])

                
                    
            elif "EndTask:=" in clean_line[0]:
                newText = clean_line[0].split("_")
                if str(newText[0]) != "main":
                    self.diccionario[newText[0]].append("\tjr $ra\n")
                    self.controller.remove(newText[0])
                else:
                    # con v0, 1 es para cuando es un entero; v0, 4 es para una cadena
                    self.diccionario["main"].append("\tli $v0, 1\n")
                    self.diccionario["main"].append("\tmove $a0, $t0\n")
                    self.diccionario["main"].append("\tsyscall\n")
                    self.diccionario["main"].append("\tlw $ra, 0($sp)\n")
                    self.diccionario["main"].append("\tadd $sp, $sp, 40\n")
                    self.diccionario["main"].append("\tli $v0, 10\n")
                    self.diccionario["main"].append("\tsyscall\n")
                    self.controller.remove("main")
            elif clean_line[0].strip() == "CALL":
                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[1].strip() + "\n")
            
            elif len(clean_line) == 2:
                if "GOTO" in clean_line[0] and "fi" in clean_line[1]:
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tj "+ str(clean_line[1].strip()) +"\n")
                    # self.controller.pop(len(self.controller)-1)
                    
            elif len(clean_line) == 3:
                if clean_line[1] == "<-":
                    if "$s0" in clean_line[0] and "$t" in clean_line[2]:
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                    elif "$s0" in clean_line[0] and "0($sp)" == clean_line[2].strip():
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                    elif "$s1" in clean_line[0] and "$t" in clean_line[2]:
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                    elif "$s1" in clean_line[0] and "4($sp)" == clean_line[2].strip():
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                    elif "$t" in clean_line[0] and "$s0" not in clean_line[2] and "s1" not in clean_line[2]:
                        if "text_" in clean_line[2]:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tla " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                        else:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tli " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                    elif "$t" in clean_line[0] and "$s1" in str(clean_line[2]):
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                    elif "$t" in clean_line[0] and "$s0" in str(clean_line[2]):
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                else:
                    lineAgroup = ' '.join(clean_line)
                    self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
            elif len(clean_line) == 4:
                if clean_line[1] == "<-":
                    if clean_line[2] == "CALL":
                        if "." in clean_line[3]:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                else:
                    lineAgroup = ' '.join(clean_line)
                    self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
                    
            elif len(clean_line) == 5:
                if clean_line[1] == "<-":
                    if clean_line[3] == "+":
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tadd " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                    elif clean_line[3] == "-":
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsub " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                    elif clean_line[3] == "/":
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tdiv " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                    elif clean_line[3] == "*":
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tmul " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                elif clean_line[1] == "==":
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tbeq "+ str(clean_line[0].strip())+ ", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                elif clean_line[1] == "!=":
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tbne "+ str(clean_line[0].strip())+ ", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                elif clean_line[1] == ">=":
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tbge "+ str(clean_line[0].strip())+ ", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                elif clean_line[1] == "<=":
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tble "+ str(clean_line[0].strip())+ ", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                else:
                    lineAgroup = ' '.join(clean_line)
                    self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
                        
            else:
                lineAgroup = ' '.join(clean_line)
                self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
            print(clean_line)
            
            print("controller: ",self.controller, "\n")
            
        with open("output/resultMips.a", 'w') as file:
            for clave, valor in self.diccionario.items():
                if clave  != "main":
                    for x in valor:
                        file.write(x)
                    print(f'Clave: {clave}, Valor: {valor}')
            for clave, valor in self.diccionario.items():
                if clave  == "main":
                    for x in valor:
                        file.write(x)
                    print(f'Clave: {clave}, Valor: {valor}')
                
            
    # def adaptToMips(self):
    #     with open("output/resultMips.a", 'w') as file:
    #         for line in self.lines:
    #             clean_line = line.split(" ")
    #             if ":=" in clean_line[0] and "EndTask:=" not in clean_line[0]:
    #                 if "if_" in clean_line[0]:
    #                     pass
    #                 elif "else_" in clean_line[0]:
    #                     file.write("\tjal " + clean_line[0].split(":=")[0] + "\n")
    #                     file.write(".text\n")
    #                     file.write(str(clean_line[0].replace(":=",":")))
    #                 else:
    #                     file.write(".text\n")
    #                     file.write(str(clean_line[0].replace(":=",":")))
    #                     if "main:=" in clean_line[0]:
    #                         file.write("\tla $sp, 0x7FFFFFC0\n")
    #                         file.write("\tsub $sp, $sp, 40\n")
    #                         file.write("\tsw $ra, 0($sp)\n")
 
                        
                
    #             elif "EndTask:=" in clean_line[0]:
    #                 newText = clean_line[0].split("_")
    #                 if str(newText[0]) != "main":
    #                     file.write("\tjr $ra\n")
    #                 else:
    #                     file.write("\tli $v0, 1\n") # con v0, 1 es para cuando es un entero; v0, 4 es para una cadena
    #                     file.write("\tmove $a0, $t0\n")
    #                     file.write("\tsyscall\n")
    #                     file.write("\tlw $ra, 0($sp)\n")
    #                     file.write("\tadd $sp, $sp, 40\n")
    #                     file.write("\tli $v0, 10\n")
    #                     file.write("\tsyscall\n")
    #             elif clean_line[0].strip() == "CALL":
    #                     file.write("\tjal " + clean_line[1].strip() + "\n")
                        
    #             elif len(clean_line) == 3:
    #                 if clean_line[1] == "<-":
    #                     if "$s0" in clean_line[0] and "$t" in clean_line[2]:
    #                         file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
    #                     elif "$s0" in clean_line[0] and "0($sp)" == clean_line[2].strip():
    #                         file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
    #                     elif "$s1" in clean_line[0] and "$t" in clean_line[2]:
    #                         file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
    #                     elif "$s1" in clean_line[0] and "4($sp)" == clean_line[2].strip():
    #                         file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
    #                     elif "$t" in clean_line[0] and "$s0" not in clean_line[2] and "s1" not in clean_line[2]:
    #                         if "text_" in clean_line[2]:
    #                             file.write("\tla " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
    #                         else:
    #                             file.write("\tli " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
    #                     elif "$t" in clean_line[0] and "$s1" in str(clean_line[2]):
    #                         file.write("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
    #                     elif "$t" in clean_line[0] and "$s0" in str(clean_line[2]):
    #                         file.write("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
    #                 else:
    #                     lineAgroup = ' '.join(clean_line)
    #                     file.write(lineAgroup)
    #             elif len(clean_line) == 4:
    #                 if clean_line[1] == "<-":
    #                     if clean_line[2] == "CALL":
    #                         if "." in clean_line[3]:
    #                             file.write("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
    #                 else:
    #                     lineAgroup = ' '.join(clean_line)
    #                     file.write(lineAgroup)
                        
    #             elif len(clean_line) == 5:
    #                 if clean_line[1] == "<-":
    #                     if clean_line[3] == "+":
    #                         file.write("\tadd " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
    #                     elif clean_line[3] == "-":
    #                         file.write("\tsub " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
    #                     elif clean_line[3] == "/":
    #                         file.write("\tdiv " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
    #                     elif clean_line[3] == "*":
    #                         file.write("\tmul " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
    #                 else:
    #                     lineAgroup = ' '.join(clean_line)
    #                     file.write(lineAgroup)
                         
    #             else:
    #                 lineAgroup = ' '.join(clean_line)
    #                 file.write(lineAgroup)
    #             print(clean_line)
                

    