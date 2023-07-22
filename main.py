import tkinter as tk
from tkinter import scrolledtext, filedialog
from antlr4 import *
from build.YAPLLexer import YAPLLexer
from build.YAPLParser import YAPLParser
from YAPLVisit import YAPLVisit
from subprocess import *

def print_tree(tree, indent=0):
    tree_str = " " * indent + str(tree.getPayload())

    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        tree_str += "\n" + print_tree(child, indent + 2)

    return tree_str

class IDE(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IDE")
        self.geometry("800x800")

        self.code_input = scrolledtext.ScrolledText(self, width=100, height=30)
        self.code_input.pack()

        self.output = scrolledtext.ScrolledText(self, width=100, height=10)
        self.output.pack()
        
        button_frame = tk.Frame(self)  # Frame para los botones
        button_frame.pack()
        
        button_font = ("Arial", 14)  # Fuente y tamaño de los botones

        self.run_button = tk.Button(self, text="Ejecutar", command=self.run_antlr, width=15, height=2)
        self.run_button.pack(side=tk.RIGHT, padx=30, pady=10)
        
        self.upload_button = tk.Button(self, text="Upload File", command=self.upload_file, width=15, height=2)
        self.upload_button.pack(side=tk.LEFT, padx=30, pady=10)
        
        # Centrar el button_frame
        button_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)

    def run_antlr(self):
        input_code = self.code_input.get("1.0", tk.END)
        process = Popen(['antlr4-parse', 'YAPL.g4', 'program', '-gui'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(input_code.encode())
        error_occurred = False

        # Crear el lexer y el stream de tokens
        lexer = YAPLLexer(InputStream(input_code))
        stream = CommonTokenStream(lexer)

        # Crear el parser y construir el árbol sintáctico
        parser = YAPLParser(stream)
        parser.removeErrorListeners()  # Desactivar los listeners de errores para evitar mensajes por consola
        
        try:
            tree = parser.program()
            # print(print_tree(tree))
            print("=====")

             # Crear una instancia del visitor y visitar el árbol sintáctico
            visitor = YAPLVisit()
            result = visitor.visit(tree)
            if result != None:
                print("visit result: ", result)
                print("All good")
            else:
                print("Error de tipo ")
             # Imprimir el resultado del análisis semántico
            print(visitor.symbol_table.symbols)

        except RecognitionException as e:
            error_occurred = True

        # self.output.delete("1.0", tk.END)
        if error_occurred and error:
            self.output.insert(tk.END, str(e) + "\n", "red")
        else:
            self.output.insert(tk.END, output.decode())
            # self.output.insert(tk.END, tree.toStringTree(recog=parser))

if __name__ == "__main__":
    ide = IDE()
    ide.mainloop()

