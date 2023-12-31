import tkinter as tk
from tkinter import scrolledtext, filedialog
from antlr4 import *
from build.YAPLLexer import YAPLLexer
from build.YAPLParser import YAPLParser
from YAPLVisit import YAPLVisit
from subprocess import *
from tkinter import ttk

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
        
        self.upload_button = tk.Button(self, text="Show tree", command=self.display_tree, width=15, height=2)
        self.upload_button.pack(side=tk.LEFT, padx=30, pady=10)
        
        self.upload_button = tk.Button(self, text="Upload File", command=self.upload_file, width=15, height=2)
        self.upload_button.pack(side=tk.LEFT, padx=30, pady=10)
        
        # Centrar el button_frame
        button_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
    def display_tree(self):
        input_code = self.code_input.get("1.0", tk.END)
        process = Popen(['antlr4-parse', 'YAPL.g4', 'program', '-gui'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(input_code.encode())
        error_occurred = False
  

        
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)

    def SymbolTablePrint(self, visitor):
        # Crear una ventana
        ventana = tk.Tk()
        ventana.title("Symbol Table")

        # Crear un Treeview (Tabla)
        tabla = ttk.Treeview(ventana)
        tabla["columns"] = ("Tipo", "Inherits", "Width", "Displacement", "Ambit", "Recieves")
        tabla.heading("#0", text="Variable")
        tabla.heading("Tipo", text="Tipo")
        tabla.heading("Inherits", text="Inherits")
        tabla.heading("Width", text="Width")
        tabla.heading("Displacement", text="Displacement")
        tabla.heading("Ambit", text="Ambit")
        tabla.heading("Recieves", text="Recieves")
        

        # Agregar datos al Treeview
        for name, symbols in visitor.symbol_table.symbols.items():
            for symbol in symbols:
                clave = name
                elementos = []
                for attr, value in symbol.items():
                    elementos.append(value)
                tabla.insert("", "end", text=clave, values=(elementos[0], elementos[1], elementos[2], elementos[3], elementos[4], elementos[5]))

        # Ajustar el ancho de las columnas para que se vean correctamente los datos
        tabla.column("#0" )
        tabla.column("Tipo")
        tabla.column("Inherits")
        tabla.column("Width")
        tabla.column("Displacement")
        tabla.column("Ambit")
        tabla.column("Recieves")

        # Empaquetar el Treeview
        tabla.pack(fill="both", expand=True)

        # Ejecutar la ventana
        ventana.mainloop()
        
    def run_antlr(self):
        input_code = self.code_input.get("1.0", tk.END)

        # Crear el lexer y el stream de tokens
        lexer = YAPLLexer(InputStream(input_code))
        stream = CommonTokenStream(lexer)

        # Crear el parser y construir el árbol sintáctico
        parser = YAPLParser(stream)
        parser.removeErrorListeners()  # Desactivar los listeners de errores para evitar mensajes por consola
        
        try:
            tree = parser.program()
            # print(print_tree(tree))
            # print("=====")

             # Crear una instancia del visitor y visitar el árbol sintáctico
            visitor = YAPLVisit()
            result = visitor.visit(tree)
            print("result: ",result)
            self.output.delete(1.0, tk.END)
            # print("tipo de result: ", result)
            # print("visitor.errors: ", visitor.errors)
            if len(result) == 0:
                #Generamos la información en la consola
                self.output.insert(tk.END, "Código correcto")
                """print("visit result: ", result)
                print("All good")"""
            else:
                for r in result:
                    self.output.insert(tk.END, "Código incorrecto, error de tipo: " + r, "red") if result != [] else self.output.insert(tk.END, "Código incorrecto, error de tipo", "red")
             # Imprimir el resultado del análisis semántico
            self.SymbolTablePrint(visitor)
            #print(visitor.symbol_table.symbols)

        except RecognitionException as e:
            print("Error ocurred")

        # self.output.delete("1.0", tk.END)
       
if __name__ == "__main__":
    ide = IDE()
    ide.mainloop()

