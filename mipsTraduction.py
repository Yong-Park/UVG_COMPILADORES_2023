class mipsTraduction():
    
    def __init__(self,direction):
        with open(direction, "r") as file:
            self.lines = file.readlines()
            
    def adaptToMips(self):
        with open("output/resultMips.a", 'w') as file:
            for line in self.lines:
                clean_line = line.split(" ")
                if ":=" in clean_line[0] and "EndTask:=" not in clean_line[0]:
                    file.write(".text\n")
                    file.write(str(clean_line[0].replace(":=",":")))
                    
                elif "EndTask:=" in clean_line[0]:
                    newText = clean_line[0].split("_")
                    if str(newText[0]) != "main":
                        file.write("\tjr $ra\n")
                    else:
                        file.write("\tli $v0, 1\n")
                        file.write("\tmove $a0, $t0\n")
                        file.write("\tsyscall\n")
                        file.write("\tli $v0, 10\n")
                        file.write("\tsyscall\n")
                elif clean_line[0].strip() == "CALL":
                        file.write("\tjal " + clean_line[1].strip() + "\n")
                        
                elif len(clean_line) == 3:
                    if clean_line[1] == "<-":
                        if "$s0" in clean_line[0] and "$t" in clean_line[2]:
                            file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                        elif "$s0" in clean_line[0] and "GP" == clean_line[2].strip():
                            file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                        elif "$s1" in clean_line[0] and "$t" in clean_line[2]:
                            file.write("\tsw " + str(clean_line[2].strip()) +", "+ str(clean_line[0].strip())+ "\n")
                        elif "$s1" in clean_line[0] and "LP" == clean_line[2].strip():
                            file.write("\tla " + str(clean_line[0].strip()) +", "+ str(clean_line[2].strip())+ "\n")
                        elif "$t" in clean_line[0] and "$s0" not in clean_line[2]:
                            if "s1" not in clean_line[2]:
                                file.write("\tli " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                        elif "$t" in clean_line[0] and "$s0" in clean_line[2] or "$t" in clean_line[0] and "$s1" in clean_line[2]:
                            file.write("\tlw " + str(clean_line[0].strip()) + ", " + str(clean_line[2].strip()) + "\n")
                    else:
                        lineAgroup = ' '.join(clean_line)
                        file.write(lineAgroup)
                        
                else:
                    lineAgroup = ' '.join(clean_line)
                    file.write(lineAgroup)
                print(clean_line)
                

    