import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.tree.Trees import Trees
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.resultTextEdit = QTextEdit()  # Nuevo cuadro de texto para el resultado
        self.resultTextEdit.setReadOnly(True)  # Establecer como solo lectura
        self.resultTextEdit.setStyleSheet("background-color: lightgray")  # Establecer el color de fondo

        self.setCentralWidget(self.textEdit)

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.showFileDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.runButton = QPushButton("Run")
        self.runButton.clicked.connect(self.runANTLR)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        # Agregar ambos cuadros de texto a un layout horizontal
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.resultTextEdit)
        result_layout.addWidget(self.runButton)

        # Agregar el layout horizontal al layout principal
        layout.addLayout(result_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('ANTLR4 GUI')
        self.show()

    def showFileDialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open file", "", "ANTLR Grammar Files (*.g4)")
        if file:
            with open(file, "r") as f:
                content = f.read()
                self.textEdit.setPlainText(content)

    def runANTLR(self):
        code = self.textEdit.toPlainText()

        # Aquí se puede generar y compilar el lexer y el parser utilizando ANTLR4
        input_stream = InputStream(code)
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)

        # Obtener el árbol sintáctico
        # tree = parser.program()
        tree = parser.prog()

        # Mostrar el árbol sintáctico
        tree_str = tree.toStringTree(recog=parser)
        self.resultTextEdit.setPlainText(tree_str)  # Establecer el resultado en el cuadro de texto de resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
