import tkinter as tk
from tkinter import scrolledtext
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from subprocess import *

class IDE(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IDE")
        self.geometry("800x600")

        self.code_input = scrolledtext.ScrolledText(self, width=100, height=30)
        self.code_input.pack()

        self.output = scrolledtext.ScrolledText(self, width=100, height=10)
        self.output.pack()

        self.run_button = tk.Button(self, text="Ejecutar", command=self.run_antlr)
        self.run_button.pack()

    """def run_antlr(self):
        try:
            input_code = self.code_input.get("1.0", tk.END)
            process = Popen(['antlr4-parse', 'Expr.g4', 'prog', '-gui'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, error = process.communicate(input_code.encode())

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, output.decode())
        except Exception as e:
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, str(e))
"""
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
        except RecognitionException as e:
            error_occurred = True

        if error_occurred and error:
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, str(e))
        else:
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, output.decode())

if __name__ == "__main__":
    ide = IDE()
    ide.mainloop()

