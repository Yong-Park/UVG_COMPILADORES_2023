class mipsTraduction():
    
    def __init__(self,direction,result):
        self.diccionario = {}
        self.controller = []
        self.returnPosition = []
        self.result = result
        with open(direction, "r") as file:
            self.lines = file.readlines()
            
    def newPosition(self):
        value = 0
        while value in self.returnPosition:
            value += 4
        self.returnPosition.append(value)
        
        return value
    
    def clearPosition(self):
        self.returnPosition = []
            
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
                    if self.controller[len(self.controller)-2].split("_")[0] not in ["if","else","then","fi","while","loop","pool"]:
                        if self.controller[len(self.controller)-2].split("_")[0] == "main":
                            self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                        else:
                            position = self.newPosition()
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, -4\n")
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, 0($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $sp, $sp, -4\n")
                            self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, 0($sp)\n")
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, " + str(position) +"($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, " + str(position) +"($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, 0($sp)\n")
                            self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $sp, $sp, 4\n")
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, 0($s3)\n")
                            # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, 4\n")
                    elif self.controller[len(self.controller)-2].split("_")[0] in ["while","loop","pool"]:
                        position = self.newPosition()
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, -4\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, 0($s3)\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, " + str(position) +"($s3)\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append(".text\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, 0($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, 4\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, " + str(position) +"($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\tmove $ra, $t9\n")
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
                    if "main:=" in clean_line[0]:
                        self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla $sp, 0x7FFFFFC0\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tsub $sp, $sp, 40\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($sp)\n")
                    #logica para guardra mas valores en caso que tenga mas 
                    elif "[" in clean_line[0]:
                        self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].split("[")[0] + ":\n"))
                        values = clean_line[0].split("[")[1].split("]")[0].split(",")
                        # print("method values recieves: ",values)
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s4, $s4, -"+str((len(values)+1)*4)+"\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s4)\n")
                        # for x in range(len(values)):
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $t0, "+str(x*4)+"($s1)\n")
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $t0, "+ str((x+1)*4)+"($s4)\n")
                        pass
                    else:
                        self.diccionario[self.controller[len(self.controller)-1]].append(str(clean_line[0].replace(":=",":")))
                        
                    
                
                #Ahora aplicamos la misma lógica para el while
                if "while_" in clean_line[0]:
                    #print("Holaaaaaaaaaaaaaaaaaaa")
                    if self.controller[len(self.controller)-2].split("_")[0] in ["main"]:
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                    else:
                        position = self.newPosition()
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, -4\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, 0($s3)\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tsw $ra, " + str(position) +"($s3)\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tjal " + clean_line[0].split(":=")[0] + "\n")
                        self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, " + str(position) +"($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\tlw $ra, 0($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-2]].append("\taddi $s3, $s3, 4\n")
                    #     self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                #Detectamos si se encuentra la etiqueta loop
                elif "loop_" in clean_line[0]:
                    self.diccionario[self.controller[len(self.controller)-2]].append("\tj " + clean_line[0].split(":=")[0] + "\n")
                #Detectamos si se encuentra la etiqueta pool
                elif "pool_" in clean_line[0]:
                    # self.diccionario[self.controller[len(self.controller)-2]].append("\tj " +clean_line[0].split(":=")[0] + "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjr $ra\n")
                    
                    #eliminar todos los _algo de logica
                    self.controller.remove("while_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("loop_"+clean_line[0].split(":=")[0].split("_")[1])
                    self.controller.remove("pool_"+clean_line[0].split(":=")[0].split("_")[1])

            elif ".data" in clean_line[0]:
                self.controller.append(clean_line[0])
                self.diccionario[self.controller[len(self.controller)-1]] = [] 
                self.diccionario[self.controller[len(self.controller)-1]].append(".data\n")
                    
            elif "EndTask:=" in clean_line[0]:
                newText = clean_line[0].split("_")
                if str(newText[0]) != "main":
                    self.diccionario[newText[0]].append("\tjr $ra\n")
                    self.controller.remove(newText[0])
                else:
                    # # con v0, 1 es para cuando es un entero; v0, 4 es para una cadena
                    # if self.result == "Int":
                    #     self.diccionario["main"].append("\tli $v0, 1\n")
                    # elif self.result == "String":
                    #     self.diccionario["main"].append("\tli $v0, 4\n")
                    # else:
                    #     self.diccionario["main"].append("\tli $v0, 1\n")
                    
                    # self.diccionario["main"].append("\tmove $a0, $t0\n")
                    # self.diccionario["main"].append("\tsyscall\n")
                    self.diccionario["main"].append("\tlw $ra, 0($sp)\n")
                    # self.diccionario["main"].append("\tadd $sp, $sp, 40\n")
                    self.diccionario["main"].append("\tli $v0, 10\n")
                    self.diccionario["main"].append("\tsyscall\n")
                    self.controller.remove("main")
                # self.clearPosition()
            elif clean_line[0].strip() == "CALL":
                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[1].strip() + "\n")
            
            elif len(clean_line) == 2:
                if "GOTO" in clean_line[0] and "fi" in clean_line[1]:
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tj "+ str(clean_line[1].strip()) +"\n")
                    # self.controller.pop(len(self.controller)-1)
                elif "GOTO" in clean_line[0] and "while" in clean_line[1]:
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tj "+ str(clean_line[1].strip()) +"\n")
                    
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
                        elif "true" in clean_line[2]:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tli " + str(clean_line[0].strip()) + ", 1\n")
                        elif "false" in clean_line[2]:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tli " + str(clean_line[0].strip()) + ", 0\n")
                        else:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tli " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                    elif "$s2" in clean_line[0] and "8($sp)" == clean_line[2].strip():
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                    elif "$s3" in clean_line[0] and "12($sp)" == clean_line[2].strip():
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                    elif "$s4" in clean_line[0] and "$sp" == clean_line[2].strip():
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tmove " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
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
                            if "TYPE_NAME" in clean_line[3]:
                                if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split(".")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split(".")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                else:
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split(".")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                            elif "SUBSTR" in clean_line[3]:
                                if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $a0, " + clean_line[3].split(".")[0].strip()+ "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[1].replace(")","").strip()+ ", 4($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tla $a1, substring\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].split("(")[0].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $a0, " + clean_line[3].split(".")[0].strip()+ "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[1].replace(")","").strip()+ ", 4($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tla $a1, substring\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].split("(")[0].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                else:
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $a0, " + clean_line[3].split(".")[0].strip()+ "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(",")[1].replace(")","").strip()+ ", 4($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tla $a1, substring\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split(".")[1].split("(")[0].strip() + "\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw " + clean_line[0].strip() + ", 0($s2)\n")
                            elif "OUT_STRING" in clean_line[3]:
                                if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].split(".")[1].strip() + "\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                                    position = self.newPosition()
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].split(".")[1].strip() + "\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                    # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                    # self.returnPosition.pop()
                                else:
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                    self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].split(".")[1].strip() + "\n")
                            elif "ABORT" in clean_line[3]:
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].split(".")[1].strip() + "\n")
                            else:
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                        elif "OUT_STRING" in clean_line[3]:
                            if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                position = self.newPosition()
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                # self.returnPosition.pop()
                            elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                position = self.newPosition()
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                # self.returnPosition.pop()
                            else:
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                        elif "OUT_INT" in clean_line[3]:
                            if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                position = self.newPosition()
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                # self.returnPosition.pop()
                            elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                                position = self.newPosition()
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                                # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                                # self.returnPosition.pop()
                            else:
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split("(")[1].split(")")[0].strip()+ ", 0($s2)\n")
                                self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                    elif clean_line[2] == "ISVOID": #logica para isvoid
                        if self.controller[len(self.controller)-1].split("_")[0] in ["while","loop","pool","if","then","else","fi"]:
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                            position = self.newPosition()
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tsw "+ clean_line[3].strip() + ", 0($s2)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tjal ISVOID\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tlw "+ clean_line[0].strip() + ", 0($s2)\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                            # self.returnPosition.pop()
                        elif self.controller[len(self.controller)-1].split("_")[0] not in ["main"]:
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $t9, $ra\n")
                            position = self.newPosition()
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, " + str(position) +"($s3)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tsw "+ clean_line[3].strip() + ", 0($s2)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tjal ISVOID\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tlw "+ clean_line[0].strip() + ", 0($s2)\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tmove $ra, $t9\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                            # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, " + str(position) +"($s3)\n")
                            # self.returnPosition.pop()
                        else:
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tsw "+ clean_line[3].strip() + ", 0($s2)\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tjal ISVOID\n")
                            self.diccionario[self.controller[len(self.controller)-1]].append("\tlw "+ clean_line[0].strip() + ", 0($s2)\n")
                    elif clean_line[2] == "CALL_OWN":
                        position = self.newPosition()
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, -4\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tsw " + clean_line[3].split(".")[0].strip()+ ", 0($s2)\n")
                        self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("[")[0].strip() + "\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s4)\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $t1, 4($s4)\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s4, $s4, 8\n")
                        # val = clean_line[3].split("[")[1].split("]")[0]
                        # for x in range(len(val)):
                        #     self.diccionario[self.controller[len(self.controller)-1]].append()
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s3)\n")
                        # self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s3, $s3, 4\n")

                        # sendValue = clean_line[3].split("(")[1].split(")")[0].strip().split(",")
                        # if len(sendValue) > 0:
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s4, $s4, -"+ str((len(sendValue)+1)*4) + "\n")
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $ra, 0($s4)\n")
                        #     for i in range(len(sendValue)):
                        #         self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $t0, "+str(i)+"($s1)\n")
                        #         self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $t0, "+str((i+1)*4)+"($s4)\n")
                                
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $ra, 0($s4)\n")
                        #     for i in range(len(sendValue)):
                        #         self.diccionario[self.controller[len(self.controller)-1]].append("\tlw $t0, "+str((i+1)*4)+"($s4)\n")
                        #         self.diccionario[self.controller[len(self.controller)-1]].append("\tsw $t0, "+str(i)+"($s1)\n")
                        #     self.diccionario[self.controller[len(self.controller)-1]].append("\taddi $s4, $s4, "+ str((len(sendValue)+1)*4) + "\n")
                        
                else:
                    # print("clean_line: ",clean_line)
                    lineAgroup = ' '.join(clean_line)
                    print("lineAgroup: ",lineAgroup)
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
                elif clean_line[1] == "<":
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tslt $t0, "+ str(clean_line[0].strip())+ ", "+ str(clean_line[2].strip())+ "\n")
                    self.diccionario[self.controller[len(self.controller)-1]].append("\tbeq $t0, 1"+ ", "+ str(clean_line[4].strip()) +"\n")
                else:
                    lineAgroup = ' '.join(clean_line)
                    self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
                        
            else:
                lineAgroup = ' '.join(clean_line)
                self.diccionario[self.controller[len(self.controller)-1]].append(lineAgroup)
            print(clean_line)
            
            print("controller: ",self.controller, "\n")
            
        with open("output/resultMips.a", 'w') as file:
            file.write(".text\n")
            file.write("OUT_STRING:\n")         # logica de out_string
            file.write("\tlw $a0, 0($s2)\n")
            file.write("\tli $v0, 4\n")         # para regresar un string
            file.write("\tsyscall\n")
            file.write("\tjr $ra\n")
            
            file.write("OUT_INT:\n")         # logica de out_int
            file.write("\tlw $a0, 0($s2)\n")
            file.write("\tli $v0, 1\n")        # para regresar un int
            file.write("\tsyscall\n")
            file.write("\tjr $ra\n")
            
            file.write("TYPE_NAME:\n")         # logica de TYPE_NAME
            file.write("\tlw $t0, 0($s2)\n")
            file.write("\tla $t1, object_str\n")
            file.write("\tbeq $t0, $t1, is_Object\n") #logica para revisar si es tipo Object
            file.write("\tla $t1, bool_str\n")          
            file.write("\tbeq $t0, $t1, is_Bool\n")   # logica para ver si es tipo booleano
            # agregas mas lineas de logica si es necesario
            file.write("\tjr $ra\n")
            
            file.write("is_Object:\n")         # para asignar la palabra Object
            file.write("\tla $t0, object_str\n")
            file.write("\tsw $t0, 0($s2)\n")
            file.write("\tjr $ra\n")
            
            file.write("is_Bool:\n")         # para asignar la palabra Object
            file.write("\tla $t0, bool_str\n")
            file.write("\tsw $t0, 0($s2)\n")
            file.write("\tjr $ra\n")
            
            file.write("SUBSTR:\n")         # logica de SUBSTR
            file.write("\tlw $t0, 0($s2)\n")
            file.write("\tlw $t1, 4($s2)\n")
            file.write("\tbge $t0, $t1, SWAP\n") # si t1 es mayor que t2 cambiarlos
            file.write("\tj NO_SWAP\n")
            
            file.write("SWAP:\n")
            file.write("\tlw $t0, 4($s2)\n")
            file.write("\tlw $t1, 0($s2)\n")
            file.write("\tj NO_SWAP\n")
            
            file.write("NO_SWAP:\n")
            file.write("\tmove $t3, $t0\n")
            file.write("\tadd $t4, $a0, $t0\n")
            file.write("\tmove $t5, $a1\n")
            
            file.write("\tCOOPY_LOOP:\n")
            file.write("\t\tlb $t6, 0($t4)\n")
            file.write("\t\tsb $t6, 0($t5)\n")
            file.write("\t\taddi $t4, $t4, 1\n")
            file.write("\t\taddi $t5, $t5, 1\n")
            file.write("\t\taddi $t3, $t3, 1\n")
            file.write("\t\tbne $t3, $t1, COOPY_LOOP\n")
            
            file.write("\tli $t6, 0\n")
            file.write("\tsb $t6, 0($t5)\n")
            file.write("\tsw $a1, 0($s2)\n")
            file.write("\tjr $ra\n")
            
            file.write("ISVOID:\n")             #logica de ISVOID
            file.write("\tlw $t0, 0($s2)\n")
            file.write("\tla $t1, void_str\n")
            
            file.write("\tCOMPARE_VOID:\n")
            file.write("\t\tlb $t2, 0($t0)\n")
            file.write("\t\tlb $t3, 0($t1)\n")
            file.write("\t\tbeq $t2, $t3, CONTINUE_VOID\n")
            file.write("\t\tj NOT_EQUAL_VOID\n")
            
            file.write("\tCONTINUE_VOID:\n")
            file.write("\t\taddi $t0, $t0, 1\n")
            file.write("\t\taddi $t1, $t1, 1\n")
            file.write("\t\tbeq $t2, 0, IS_EQUAL_VOID\n")
            file.write("\t\tj COMPARE_VOID\n")
            
            file.write("\tIS_EQUAL_VOID:\n")
            file.write("\tla $t0, true_str\n")
            file.write("\tj END_COMPARE_VOID\n")
            
            file.write("\tNOT_EQUAL_VOID:\n")
            file.write("\tla $t0, false_str\n")
            
            file.write("\tEND_COMPARE_VOID:\n")
            file.write("\tsw $t0, 0($s2)\n")
            
            file.write("\tjr $ra\n")
            
            file.write("ABORT:\n")              #logica del ABORT
            file.write("\tli $v0, 10\n")
            file.write("\tsyscall\n")
            
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
                

    