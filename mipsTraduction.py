class mipsTraduction():
    
    def __init__(self,direction):
        with open(direction, "r") as file:
            self.lines = file.readlines()
            
    def adaptToMips(self):
        with open("output/resultMips.a", 'w') as file:
            for line in self.lines:
                clean_line = line.split(" ")
                if ":=" in clean_line[0] and "EndTask:=" not in clean_line[0]:
                    if "if_" in clean_line[0]:
                        pass
                    elif "else_" in clean_line[0]:
                        file.write("\tjal " + clean_line[0].split(":=")[0] + "\n")
                        file.write(".text\n")
                        file.write(str(clean_line[0].replace(":=",":")))
                    else:
                        file.write(".text\n")
                        file.write(str(clean_line[0].replace(":=",":")))
                        if "main:=" in clean_line[0]:
                            file.write("\tla $sp, 0x7FFFFFC0\n")
                            file.write("\tsub $sp, $sp, 40\n")
                            file.write("\tsw $ra, 0($sp)\n")
 
                        
                
                elif "EndTask:=" in clean_line[0]:
                    newText = clean_line[0].split("_")
                    if str(newText[0]) != "main":
                        file.write("\tjr $ra\n")
                    else:
                        file.write("\tli $v0, 1\n") # con v0, 1 es para cuando es un entero; v0, 4 es para una cadena
                        file.write("\tmove $a0, $t0\n")
                        file.write("\tsyscall\n")
                        file.write("\tlw $ra, 0($sp)\n")
                        file.write("\tadd $sp, $sp, 40\n")
                        file.write("\tli $v0, 10\n")
                        file.write("\tsyscall\n")
                elif clean_line[0].strip() == "CALL":
                        file.write("\tjal " + clean_line[1].strip() + "\n")
                        
                elif len(clean_line) == 3:
                    if clean_line[1] == "<-":
                        if "$s0" in clean_line[0] and "$t" in clean_line[2]:
                            file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                        elif "$s0" in clean_line[0] and "0($sp)" == clean_line[2].strip():
                            file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                        elif "$s1" in clean_line[0] and "$t" in clean_line[2]:
                            file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                        elif "$s1" in clean_line[0] and "4($sp)" == clean_line[2].strip():
                            file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                        elif "$t" in clean_line[0] and "$s0" not in clean_line[2] and "s1" not in clean_line[2]:
                            if "text_" in clean_line[2]:
                                file.write("\tla " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                            else:
                                file.write("\tli " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                        elif "$t" in clean_line[0] and "$s1" in str(clean_line[2]):
                            file.write("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                        elif "$t" in clean_line[0] and "$s0" in str(clean_line[2]):
                            file.write("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                    else:
                        lineAgroup = ' '.join(clean_line)
                        file.write(lineAgroup)
                elif len(clean_line) == 4:
                    if clean_line[1] == "<-":
                        if clean_line[2] == "CALL":
                            if "." in clean_line[3]:
                                file.write("\tjal " + clean_line[3].split("(")[0].strip() + "\n")
                    else:
                        lineAgroup = ' '.join(clean_line)
                        file.write(lineAgroup)
                        
                elif len(clean_line) == 5:
                    if clean_line[1] == "<-":
                        if clean_line[3] == "+":
                            file.write("\tadd " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                        elif clean_line[3] == "-":
                            file.write("\tsub " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                        elif clean_line[3] == "/":
                            file.write("\tdiv " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                        elif clean_line[3] == "*":
                            file.write("\tmul " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ ", "+ str(clean_line[4].strip()) +"\n")
                    else:
                        lineAgroup = ' '.join(clean_line)
                        file.write(lineAgroup)
                         
                else:
                    lineAgroup = ' '.join(clean_line)
                    file.write(lineAgroup)
                print(clean_line)
                

    