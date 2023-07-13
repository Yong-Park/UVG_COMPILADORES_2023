import sys
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
import tkinter as tk

# def main(argv):
#     input_stream = FileStream(argv[1])
#     lexer = YAPLLexer(input_stream) 
#     stream = CommonTokenStream(lexer)
#     parser = YAPLParser(stream)
#     tree = parser.startRule()
 
# if __name__ == '__main__':
#     main(sys.argv)

def compilar():
    # Obtiene el texto ingresado en el cuadro de texto editable
    codigo = texto_editable.get("1.0", "end-1c")
    print(codigo)
    # Muestra el contenido en el cuadro de texto de resultados
    texto_resultados.config(state=tk.NORMAL)  # Habilita la edición
    texto_resultados.delete("1.0", tk.END)    # Borra el contenido anterior
    texto_resultados.insert(tk.END, codigo)   # Muestra el código en el cuadro de resultados
    texto_resultados.config(state=tk.DISABLED)  # Deshabilita la edición

# Crear ventana principal
ventana = tk.Tk()

# Crear cuadro de texto editable
texto_editable = tk.Text(ventana)
texto_editable.pack()

# Crear cuadro de texto de resultados
texto_resultados = tk.Text(ventana, state=tk.DISABLED)
texto_resultados.pack()

# Crear botón de compilación
boton_compilar = tk.Button(ventana, text="Compilar", command=compilar)
boton_compilar.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
